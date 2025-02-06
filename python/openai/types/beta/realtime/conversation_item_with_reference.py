# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .conversation_item_content import ConversationItemContent

__all__ = ["ConversationItemWithReference"]


class ConversationItemWithReference(BaseModel):
    id: Optional[str] = None
    """
    For an item of type (`message` | `function_call` | `function_call_output`) this
    field allows the client to assign the unique ID of the item. It is not required
    because the server will generate one if not provided.

    For an item of type `item_reference`, this field is required and is a reference
    to any item that has previously existed in the conversation.
    """

    arguments: Optional[str] = None
    """The arguments of the function call (for `function_call` items)."""

    call_id: Optional[str] = None
    """
    The ID of the function call (for `function_call` and `function_call_output`
    items). If passed on a `function_call_output` item, the server will check that a
    `function_call` item with the same ID exists in the conversation history.
    """

    content: Optional[List[ConversationItemContent]] = None
    """The content of the message, applicable for `message` items.

    - Message items of role `system` support only `input_text` content
    - Message items of role `user` support `input_text` and `input_audio` content
    - Message items of role `assistant` support `text` content.
    """

    name: Optional[str] = None
    """The name of the function being called (for `function_call` items)."""

    object: Optional[Literal["realtime.item"]] = None
    """Identifier for the API object being returned - always `realtime.item`."""

    output: Optional[str] = None
    """The output of the function call (for `function_call_output` items)."""

    role: Optional[Literal["user", "assistant", "system"]] = None
    """
    The role of the message sender (`user`, `assistant`, `system`), only applicable
    for `message` items.
    """

    status: Optional[Literal["completed", "incomplete"]] = None
    """The status of the item (`completed`, `incomplete`).

    These have no effect on the conversation, but are accepted for consistency with
    the `conversation.item.created` event.
    """

    type: Optional[Literal["message", "function_call", "function_call_output", "item_reference"]] = None
    """
    The type of the item (`message`, `function_call`, `function_call_output`,
    `item_reference`).
    """
