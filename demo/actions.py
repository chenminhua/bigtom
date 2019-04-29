from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
    ConversationPaused, FollowupAction, Form

# class ActionCheckRestaurants(Action):
#    def name(self):
#       # type: () -> Text
#       return "action_check_restaurants"

#    def run(self, dispatcher, tracker, domain):
#       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

#       cuisine = tracker.get_slot('cuisine')
#       q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
#       result = db.query(q)

#       return [SlotSet("matches", result if result is not None else [])]

class ActionChitchat(Action):
  """闲聊"""

  def name(self):
    return "action_chitchat"

  def run(self, dispatcher, tracker, domain):
    intent = tracker.latest_message['intent'].get('name')

    if intent in ['ask_whoisit']:
      dispatcher.utter_template('utter_' + intent, tracker)
    return []

class ActionDefaultFallback(Action):

  def name(self):
    return "my_default_fallback"

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_template('utter_default', tracker)
    return [UserUtteranceReverted()]