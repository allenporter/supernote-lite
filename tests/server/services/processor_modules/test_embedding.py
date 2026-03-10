import json
from unittest.mock import MagicMock

import pytest
from sqlalchemy import select

from supernote.server.db.models.file import UserFileDO
from supernote.server.db.models.note_processing import NotePageContentDO, SystemTaskDO
from supernote.server.db.session import DatabaseSessionManager
from supernote.server.services.file import FileService
from supernote.server.services.processor_modules.embedding import EmbeddingModule


@pytest.fixture
def embedding_module(
    file_service: FileService,
    mock_ai_service: MagicMock,
) -> EmbeddingModule:
    return EmbeddingModule(
        file_service=file_service,
        ai_service=mock_ai_service,
    )


async def test_process_embedding_success(
    embedding_module: EmbeddingModule,
    session_manager: DatabaseSessionManager,
    mock_ai_service: MagicMock,
) -> None:
    user_id = 100
    file_id = 999
    page_index = 0
    storage_key = "test_note_storage_key"

    async with session_manager.session() as session:
        user_file = UserFileDO(
            id=file_id,
            user_id=user_id,
            storage_key=storage_key,
            file_name="real.note",
            directory_id=0,
        )
        session.add(user_file)

        content = NotePageContentDO(
            file_id=file_id,
            page_index=page_index,
            page_id="p0",
            content_hash="somehash",
            text_content="This is the text to embed.",
        )
        session.add(content)
        await session.commit()

    mock_ai_service.embed_text.return_value = [0.1, 0.2, 0.3]

    await embedding_module.run(
        file_id, session_manager, page_index=page_index, page_id="p0"
    )

    # Verify embed_text was called with the correct text
    mock_ai_service.embed_text.assert_called_once_with("This is the text to embed.")

    # Verify DB Updates
    async with session_manager.session() as session:
        updated_content = (
            (
                await session.execute(
                    select(NotePageContentDO)
                    .where(NotePageContentDO.file_id == file_id)
                    .where(NotePageContentDO.page_index == page_index)
                )
            )
            .scalars()
            .first()
        )

        assert updated_content is not None
        assert updated_content.embedding is not None
        embedding_list = json.loads(updated_content.embedding)
        assert embedding_list == [0.1, 0.2, 0.3]

        task = (
            (
                await session.execute(
                    select(SystemTaskDO)
                    .where(SystemTaskDO.file_id == file_id)
                    .where(SystemTaskDO.task_type == "EMBEDDING_GENERATION")
                    .where(SystemTaskDO.key == "page_p0")
                )
            )
            .scalars()
            .first()
        )

        assert task is not None
        assert task.status == "COMPLETED"


async def test_embedding_run_if_needed_disabled(
    embedding_module: EmbeddingModule,
    session_manager: DatabaseSessionManager,
    mock_ai_service: MagicMock,
) -> None:
    mock_ai_service.is_configured = False

    assert (
        await embedding_module.run_if_needed(
            1, session_manager, page_index=0, page_id="p0"
        )
        is False
    )

    assert (
        await embedding_module.run(
            1, session_manager, page_index=0, page_id="p0"
        )
        is True
    )
