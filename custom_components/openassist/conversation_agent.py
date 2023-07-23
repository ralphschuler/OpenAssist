from homeassistant.helpers import intent
from homeassistant.components.conversation import agent


async def async_setup(hass, config):
    """Initialize your integration."""
    conversation.async_set_agent(hass, OpenAssistAgent())


class OpenAssistAgent(agent.AbstractConversationAgent):

    @property
    def attribution(self) -> agent.Attribution:
        """Return the attribution."""
        return {
            "name": "OpenAssist Agent",
            "url": "https://example.com",
        }

    @abstractmethod
    async def async_process(self, user_input: agent.ConversationInput) -> agent.ConversationResult:
        """Process a sentence."""
        response = intent.IntentResponse(language=user_input.language)
        response.async_set_speech("Test response")
        return agent.ConversationResult(
            conversation_id=None,
            response=response
        )