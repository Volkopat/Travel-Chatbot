from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from typing import Dict, Text, Any, List, Union, Optional, Tuple

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from datetime import datetime

import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, AllSlotsReset, Restarted

logger = logging.getLogger(__name__)

class ActionSlotReset(Action):  
    def name(self):         
        return 'action_slot_reset' 
    
    def run(self, dispatcher, tracker, domain):         
        return[AllSlotsReset()]
class ActionRestarted(Action):
    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]
class FormActionTrainsPNR(FormAction):
    def name(self):
        return "action_trains_pnr"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["pnr_number"]

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def slot_mappings(self):
        return {"pnr_number":  [self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                                self.from_entity(entity="no_of_people", intent="inform_age"), 
                                self.from_entity(entity="no_of_people", intent="inform_pnr"),
                                self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                                self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                                self.from_entity(entity="age", intent="inform_no_of_adults"), 
                                self.from_entity(entity="age", intent="inform_no_of_children"), 
                                self.from_entity(entity="age", intent="inform_no_of_infants"), 
                                self.from_entity(entity="age", intent="inform_age"), 
                                self.from_entity(entity="age", intent="inform_pnr"), 
                                self.from_entity(entity="age", intent="inform_train_number"), 
                                self.from_entity(entity="age", intent="inform_flight_date"),
                                self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="pnr_number", intent="inform_age"), 
                                self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                                self.from_entity(entity="pnr_number", intent="inform_train_number"),
                                self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="train_number", intent="inform_age"), 
                                self.from_entity(entity="train_number", intent="inform_pnr"), 
                                self.from_entity(entity="train_number", intent="inform_train_number"),
                                self.from_entity(entity="train_number", intent="inform_flight_date"),
                                self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                                self.from_entity(entity="flight_date", intent="inform_age"), 
                                self.from_entity(entity="flight_date", intent="inform_pnr"), 
                                self.from_entity(entity="flight_date", intent="inform_train_number"),
                                self.from_entity(entity="flight_date", intent="inform_flight_date")]}
    
    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'pnr_number':            
                if not self.is_int(value):
                    dispatcher.utter_template('utter_wrong_pnr_number', tracker)
                    slot_values[slot] = None
                    
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        pnr_number = tracker.get_slot('pnr_number')
        base_url = "http://api.railwayapi.com/v2/pnr-status/pnr/"
        complete_url = str(base_url) + str(pnr_number) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 :  
            train_name = result["train"]["name"] 
            train_number = result["train"]["number"]  
            from_station = result["from_station"]["name"]
            to_station = result["to_station"]["name"]
            boarding_point = result["boarding_point"]["name"]
            reservation_upto = result["reservation_upto"]["name"] 
            pnr_num = result["pnr"]
            date_of_journey = result["doj"]
            total_passengers = result["total_passengers"]
            passengers_list = result["passengers"]
            chart_prepared = result["chart_prepared"]
            response1 = """PNR Number - {} \nTrain Number - {} \nTrain Name - {} \nSource Station - {} \nDestination Station - {} \nBoarding Station - {} \nReservation Upto - {} \nDate of Journey - {} \nNo of Passengers - {} \nChart Prepared - {}\n""".format(pnr_num, train_number, train_name, from_station, to_station, boarding_point, reservation_upto, date_of_journey, total_passengers, chart_prepared)
            response = response1
            for passenger in passengers_list:
                passenger_num = passenger["no"]
                current_status = passenger["current_status"]
                booking_status = passenger["booking_status"]
                response2 = """Passenger Number - {} \tCurrent Status - {} \tBooking Status - {}\n""".format(passenger_num, current_status, booking_status)
                response += response2
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('pnr_number',pnr_number)]
class FormActionTrainsLive(FormAction):
    def name(self):
        return "action_trains_live"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [ "train_number","train_date","source_station_name"]

    def slot_mappings(self):
        return {"train_number":[self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                                self.from_entity(entity="no_of_people", intent="inform_age"), 
                                self.from_entity(entity="no_of_people", intent="inform_pnr"),
                                self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                                self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                                self.from_entity(entity="age", intent="inform_no_of_adults"), 
                                self.from_entity(entity="age", intent="inform_no_of_children"), 
                                self.from_entity(entity="age", intent="inform_no_of_infants"), 
                                self.from_entity(entity="age", intent="inform_age"), 
                                self.from_entity(entity="age", intent="inform_pnr"), 
                                self.from_entity(entity="age", intent="inform_train_number"), 
                                self.from_entity(entity="age", intent="inform_flight_date"),
                                self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="pnr_number", intent="inform_age"), 
                                self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                                self.from_entity(entity="pnr_number", intent="inform_train_number"),
                                self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="train_number", intent="inform_age"), 
                                self.from_entity(entity="train_number", intent="inform_pnr"), 
                                self.from_entity(entity="train_number", intent="inform_train_number"),
                                self.from_entity(entity="train_number", intent="inform_flight_date"),
                                self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                                self.from_entity(entity="flight_date", intent="inform_age"), 
                                self.from_entity(entity="flight_date", intent="inform_pnr"), 
                                self.from_entity(entity="flight_date", intent="inform_train_number"),
                                self.from_entity(entity="flight_date", intent="inform_flight_date")],
        "source_station_name" : [self.from_entity(entity="city", intent="inform_source_airport"), 
                                 self.from_entity(entity="city", intent="inform_destination_airport"), 
                                 self.from_entity(entity="city", intent="inform_city"), 
                                 self.from_entity(entity="city", intent="inform_source_station_name"), 
                                 self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                 self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                 self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                 self.from_entity(entity="station_name", intent="inform_city"), 
                                 self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                 self.from_entity(entity="station_name", intent="inform_destination_station_name")]}

    @staticmethod
    def station_db():
        textfile = open("data/lookup/railwaystations.txt","r")
        stations = textfile.readlines()
        stations = [item.replace("\n", "") for item in stations]
        return stations
    
    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'source_station_name' :
                if value.upper() not in self.station_db():
                    dispatcher.utter_template('utter_wrong_station_name', tracker)
                    slot_values[slot] = None
            elif slot == 'train_number':
                if not self.is_int(value) or int(value) < 10000 or int(value) > 99999:
                    dispatcher.utter_template('utter_wrong_train_number', tracker)
                    slot_values[slot] = None
            elif slot == 'train_date':
                try:
                    datetime.strptime(value, '%d-%m-%Y')
                except ValueError:
                    dispatcher.utter_template('utter_wrong_train_date', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        train_number = tracker.get_slot('train_number')
        train_date = tracker.get_slot('train_date')
        source_station_name = tracker.get_slot('source_station_name')
        with open('data/validate/railwaystations.json') as railway_data:
            railways = json.load(railway_data)
            for railway in railways["features"]:
                if source_station_name.upper() == railway["properties"]["name"].upper():
                    station_code = railway["properties"]["code"]
        base_url = "http://api.railwayapi.com/v2/live/train/"
        complete_url = str(base_url) + str(train_number) + "/station/" + str(station_code) + "/date/" + str(train_date) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 :  
            train_name = result["train"]["name"] 
            station_name = result["station"]["name"]
            status = result["position"]
            scheduled_arrival = result["status"]["scharr"]
            actual_arrival = result["status"]["actarr"]
            scheduled_departure = result["status"]["schdep"]
            actual_departure = result["status"]["actdep"]
            scheduled_arrival_date = result["status"]["scharr_date"]
            actual_arrival_date = result["status"]["actarr_date"]
            has_arrived = result["status"]["has_arrived"]
            has_departed = result["status"]["has_departed"]
            latemin = result["status"]["latemin"]
            response = """Train Number - {} \nTrain Name - {} \nDate - {} \nStation Name - {} \nStation Code - {} \nScheduled Arrival - {} \nActual Arrival - {} \nScheduled Departure - {} \nActual Departure - {} \nScheduled Arrival Date - {} \nActual Arrival Date - {}  \nHas Arrived - {} \nHas Departed - {} \nLate by Minutes - {} \nCurremt Status - {}""".format(train_number, train_name, train_date, station_code, station_name, scheduled_arrival, actual_arrival, scheduled_departure, actual_departure, scheduled_arrival_date, actual_arrival_date, has_arrived, has_departed, latemin, status)
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('train_number',train_number),SlotSet('train_date',train_date),SlotSet('source_station_name',source_station_name)]
class FormActionTrainsRoute(FormAction):
    def name(self):
        return "action_trains_route"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [ "train_number"]

    def slot_mappings(self):
        return {"train_number":[self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                                self.from_entity(entity="no_of_people", intent="inform_age"), 
                                self.from_entity(entity="no_of_people", intent="inform_pnr"),
                                self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                                self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                                self.from_entity(entity="age", intent="inform_no_of_adults"), 
                                self.from_entity(entity="age", intent="inform_no_of_children"), 
                                self.from_entity(entity="age", intent="inform_no_of_infants"), 
                                self.from_entity(entity="age", intent="inform_age"), 
                                self.from_entity(entity="age", intent="inform_pnr"), 
                                self.from_entity(entity="age", intent="inform_train_number"), 
                                self.from_entity(entity="age", intent="inform_flight_date"),
                                self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="pnr_number", intent="inform_age"), 
                                self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                                self.from_entity(entity="pnr_number", intent="inform_train_number"),
                                self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="train_number", intent="inform_age"), 
                                self.from_entity(entity="train_number", intent="inform_pnr"), 
                                self.from_entity(entity="train_number", intent="inform_train_number"),
                                self.from_entity(entity="train_number", intent="inform_flight_date"),
                                self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                                self.from_entity(entity="flight_date", intent="inform_age"), 
                                self.from_entity(entity="flight_date", intent="inform_pnr"), 
                                self.from_entity(entity="flight_date", intent="inform_train_number"),
                                self.from_entity(entity="flight_date", intent="inform_flight_date")]}

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'train_number':
                if not self.is_int(value) or int(value) < 10000 or int(value) > 99999:
                    dispatcher.utter_template('utter_wrong_train_number', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        train_number = tracker.get_slot('train_number')
        base_url = "http://api.railwayapi.com/v2/route/train/"
        complete_url = str(base_url) + str(train_number) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            train_name = result["train"]["name"] 
            train_number = result["train"]["number"] 
            routes_list = result["route"]
            response1 = """Train Number - {} \nTrain Name - {} \n\n""".format(train_number, train_name)
            response = response1
            for route in routes_list:
                station_number = route["no"]
                station_name = route["station"]["name"]
                station_code = route["station"]["code"]
                scheduled_arrival = route["scharr"]
                scheduled_departure = route["schdep"]
                distance = route["distance"]
                response2 = """Station Number - {} \nStation Name - {} \nStation Code - {} \nScheduled Arrival - {} \nScheduled Departure - {} \nDistance - {} \n\n""".format(station_number, station_name, station_code, scheduled_arrival, scheduled_departure, distance)
                response += response2
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('train_number',train_number)]
class FormActionTrainsFare(FormAction):
    def name(self):
        return "action_trains_fare"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["train_number","source_station_name","destination_station_name","train_date","class_code","quota_code","age"]

    def slot_mappings(self):
        return {"train_number": [self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                                self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                                self.from_entity(entity="no_of_people", intent="inform_age"), 
                                self.from_entity(entity="no_of_people", intent="inform_pnr"),
                                self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                                self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                                self.from_entity(entity="age", intent="inform_no_of_adults"), 
                                self.from_entity(entity="age", intent="inform_no_of_children"), 
                                self.from_entity(entity="age", intent="inform_no_of_infants"), 
                                self.from_entity(entity="age", intent="inform_age"), 
                                self.from_entity(entity="age", intent="inform_pnr"), 
                                self.from_entity(entity="age", intent="inform_train_number"), 
                                self.from_entity(entity="age", intent="inform_flight_date"),
                                self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="pnr_number", intent="inform_age"), 
                                self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                                self.from_entity(entity="pnr_number", intent="inform_train_number"),
                                self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                                self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                                self.from_entity(entity="train_number", intent="inform_age"), 
                                self.from_entity(entity="train_number", intent="inform_pnr"), 
                                self.from_entity(entity="train_number", intent="inform_train_number"),
                                self.from_entity(entity="train_number", intent="inform_flight_date"),
                                self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                                self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                                self.from_entity(entity="flight_date", intent="inform_age"), 
                                self.from_entity(entity="flight_date", intent="inform_pnr"), 
                                self.from_entity(entity="flight_date", intent="inform_train_number"),
                                self.from_entity(entity="flight_date", intent="inform_flight_date")],
        "source_station_name" : [self.from_entity(entity="city", intent="inform_source_airport"), 
                                 self.from_entity(entity="city", intent="inform_destination_airport"), 
                                 self.from_entity(entity="city", intent="inform_city"), 
                                 self.from_entity(entity="city", intent="inform_source_station_name"), 
                                 self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                 self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                 self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                 self.from_entity(entity="station_name", intent="inform_city"), 
                                 self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                 self.from_entity(entity="station_name", intent="inform_destination_station_name")],
        "destination_station_name": [self.from_entity(entity="city", intent="inform_source_airport"), 
                                     self.from_entity(entity="city", intent="inform_destination_airport"), 
                                     self.from_entity(entity="city", intent="inform_city"), 
                                     self.from_entity(entity="city", intent="inform_source_station_name"), 
                                     self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                     self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                     self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                     self.from_entity(entity="station_name", intent="inform_city"), 
                                     self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                     self.from_entity(entity="station_name", intent="inform_destination_station_name")],
        "class_code": [self.from_entity(entity="seating_class", intent="inform_seating_class"), 
                       self.from_entity(entity="class_code", intent="inform_seating_class"), 
                       self.from_entity(entity="quota_code", intent="inform_seating_class"), 
                       self.from_entity(entity="station_code", intent="inform_seating_class"), 
                       self.from_entity(entity="seating_class", intent="inform_class_code"), 
                       self.from_entity(entity="class_code", intent="inform_class_code"), 
                       self.from_entity(entity="quota_code", intent="inform_class_code"), 
                       self.from_entity(entity="station_code", intent="inform_class_code"), 
                       self.from_entity(entity="seating_class", intent="inform_quota_code"), 
                       self.from_entity(entity="class_code", intent="inform_quota_code"), 
                       self.from_entity(entity="quota_code", intent="inform_quota_code"), 
                       self.from_entity(entity="station_code", intent="inform_quota_code"), 
                       self.from_entity(entity="seating_class", intent="inform_station_code"), 
                       self.from_entity(entity="class_code", intent="inform_station_code"), 
                       self.from_entity(entity="quota_code", intent="inform_station_code"), 
                       self.from_entity(entity="station_code", intent="inform_station_code")],
        "quota_code": [self.from_entity(entity="seating_class", intent="inform_seating_class"), 
                       self.from_entity(entity="class_code", intent="inform_seating_class"), 
                       self.from_entity(entity="quota_code", intent="inform_seating_class"), 
                       self.from_entity(entity="station_code", intent="inform_seating_class"), 
                       self.from_entity(entity="seating_class", intent="inform_class_code"), 
                       self.from_entity(entity="class_code", intent="inform_class_code"), 
                       self.from_entity(entity="quota_code", intent="inform_class_code"), 
                       self.from_entity(entity="station_code", intent="inform_class_code"), 
                       self.from_entity(entity="seating_class", intent="inform_quota_code"), 
                       self.from_entity(entity="class_code", intent="inform_quota_code"), 
                       self.from_entity(entity="quota_code", intent="inform_quota_code"), 
                       self.from_entity(entity="station_code", intent="inform_quota_code"), 
                       self.from_entity(entity="seating_class", intent="inform_station_code"), 
                       self.from_entity(entity="class_code", intent="inform_station_code"), 
                       self.from_entity(entity="quota_code", intent="inform_station_code"), 
                       self.from_entity(entity="station_code", intent="inform_station_code")],
        "age": [self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                self.from_entity(entity="no_of_people", intent="inform_age"), 
                self.from_entity(entity="no_of_people", intent="inform_pnr"),
                self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                self.from_entity(entity="age", intent="inform_no_of_adults"), 
                self.from_entity(entity="age", intent="inform_no_of_children"), 
                self.from_entity(entity="age", intent="inform_no_of_infants"), 
                self.from_entity(entity="age", intent="inform_age"), 
                self.from_entity(entity="age", intent="inform_pnr"), 
                self.from_entity(entity="age", intent="inform_train_number"), 
                self.from_entity(entity="age", intent="inform_flight_date"),
                self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                self.from_entity(entity="pnr_number", intent="inform_age"), 
                self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                self.from_entity(entity="pnr_number", intent="inform_train_number"),
                self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                self.from_entity(entity="train_number", intent="inform_age"), 
                self.from_entity(entity="train_number", intent="inform_pnr"), 
                self.from_entity(entity="train_number", intent="inform_train_number"),
                self.from_entity(entity="train_number", intent="inform_flight_date"),
                self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                self.from_entity(entity="flight_date", intent="inform_age"), 
                self.from_entity(entity="flight_date", intent="inform_pnr"), 
                self.from_entity(entity="flight_date", intent="inform_train_number"),
                self.from_entity(entity="flight_date", intent="inform_flight_date")]}

    @staticmethod
    def station_db():
        textfile = open("data/lookup/railwaystations.txt","r")
        stations = textfile.readlines()
        stations = [item.replace("\n", "") for item in stations]
        return stations
    
    @staticmethod
    def class_db():
        textfile = open("data/lookup/classes.txt","r")
        classes = textfile.readlines()
        classes = [item.replace("\n", "") for item in classes]
        return classes

    @staticmethod
    def quota_db():
        textfile = open("data/lookup/quotas.txt","r")
        quotas = textfile.readlines()
        quotas = [item.replace("\n", "") for item in quotas]
        return quotas
    
    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'source_station_name' or slot == 'destination_station_name':
                if value not in self.station_db():
                    dispatcher.utter_template('utter_wrong_station_name', tracker)
                    slot_values[slot] = None
            elif slot == 'train_number':
                if not self.is_int(value) or int(value) < 10000 or int(value) > 99999:
                    dispatcher.utter_template('utter_wrong_train_number', tracker)
                    slot_values[slot] = None
            elif slot == 'age':
                if not self.is_int(value) or int(value) < 1 or int(value) > 100:
                    dispatcher.utter_template('utter_wrong_age', tracker)
                    slot_values[slot] = None
            elif slot == 'train_date':
                try:
                    datetime.strptime(value, '%d-%m-%Y')
                except ValueError:
                    dispatcher.utter_template('utter_wrong_train_date', tracker)
                    slot_values[slot] = None
            elif slot == 'class_code':
                if value not in self.class_db():
                    dispatcher.utter_template('utter_wrong_class_code', tracker)
                    slot_values[slot] = None
            elif slot == 'quota_code':
                if value not in self.quota_db():
                    dispatcher.utter_template('utter_wrong_quota_code', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        train_number = tracker.get_slot('train_number')
        source_station_name = tracker.get_slot('source_station_name')
        destination_station_name = tracker.get_slot('destination_station_name')
        with open('data/validate/railwaystations.json') as railway_data:
            railways = json.load(railway_data)
            for railway in railways["features"]:
                if source_station_name.upper() == railway["properties"]["name"].upper():
                    source_station_code = railway["properties"]["code"]
                if destination_station_name.upper() == railway["properties"]["name"].upper():
                    destination_station_code = railway["properties"]["code"]
        train_date = tracker.get_slot('train_date')
        class_code = tracker.get_slot('class_code')
        with open('data/validate/classes.json') as class_data:
            classes = json.load(class_data)
            for classe in classes["class"]:
                for c in classe.keys():
                    if class_code == c:
                        class_code2 = classe[c]
        quota_code = tracker.get_slot('quota_code')
        with open('data/validate/quotas.json') as quota_data:
            quotas = json.load(quota_data)
            for quota in quotas["quota"]:
                for q in quota.keys():
                    if quota_code == q:
                        quota_code2 = quota[q]
        age = tracker.get_slot('age')
        base_url = "http://api.railwayapi.com/v2/fare/train/"
        complete_url = str(base_url) + str(train_number) + "/source/" + str(source_station_code) + "/dest/" + str(destination_station_code) + "/age/" + str(age) + "/pref/" + str(class_code2) + "/quota/" + str(quota_code2) + "/date/" + str(train_date) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            source_station_name = result["from_station"]["name"]
            destination_station_name = result["to_station"]["name"]
            quota_name = result["quota"]["name"]
            class_name = result["journey_class"]["name"]
            train_name = result["train"]["name"]
            fare = result["fare"]
            days = result["train"]["days"]
            classes = result["train"]["classes"]
            response1 = """Train Number - {} \nTrain Name - {} \nDate - {} \nSource Station Name - {} \nSource Station Code - {} \nDestination Station Name - {} \nDestination Station Code - {} \nClass Name - {} \nClass Code - {} \nQuota Name - {} \nQuota Code - {}  \nAge - {} \nFare - {} \n\n""".format(train_number, train_name, train_date, source_station_name, source_station_code, destination_station_name, destination_station_code, class_name, class_code, quota_name, quota_code, age, fare)
            response = response1
            for day in days:
                day_runs = day["runs"]
                day_code = day["code"]
                response2 = """Day - {} \t Runs - {} \n""".format(day_code, day_runs)
                response += response2
            for clas in classes:
                clas_name = clas["name"]
                clas_code = clas["code"]
                clas_available = clas["available"]
                response3 = """Class Name - {} \t Class Code - {} \t Available - {}\n""".format(clas_name, clas_code, clas_available)
                response += response3
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('train_number',train_number), SlotSet('source_station_name',source_station_name), SlotSet('destination_station_name',destination_station_name), SlotSet('class_code',class_code), SlotSet('quota_code',quota_code), SlotSet('train_date',train_date), SlotSet('age',age)]
class FormActionTrainsSeat(FormAction):
    def name(self):
        return "action_trains_seat"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["train_number","source_station_name","destination_station_name","train_date","class_code","quota_code"]

    def slot_mappings(self):
        return {"source_station_name": [self.from_entity(entity="city", intent="inform_source_airport"), 
                                        self.from_entity(entity="city", intent="inform_destination_airport"), 
                                        self.from_entity(entity="city", intent="inform_city"), 
                                        self.from_entity(entity="city", intent="inform_source_station_name"), 
                                        self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                        self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                        self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                        self.from_entity(entity="station_name", intent="inform_city"), 
                                        self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                        self.from_entity(entity="station_name", intent="inform_destination_station_name")],
        "destination_station_name": [self.from_entity(entity="city", intent="inform_source_airport"), 
                                     self.from_entity(entity="city", intent="inform_destination_airport"), 
                                     self.from_entity(entity="city", intent="inform_city"), 
                                     self.from_entity(entity="city", intent="inform_source_station_name"), 
                                     self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                     self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                     self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                     self.from_entity(entity="station_name", intent="inform_city"), 
                                     self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                     self.from_entity(entity="station_name", intent="inform_destination_station_name")],
        "train_number": [self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                         self.from_entity(entity="no_of_people", intent="inform_age"), 
                         self.from_entity(entity="no_of_people", intent="inform_pnr"),
                         self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                         self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                         self.from_entity(entity="age", intent="inform_no_of_adults"), 
                         self.from_entity(entity="age", intent="inform_no_of_children"), 
                         self.from_entity(entity="age", intent="inform_no_of_infants"), 
                         self.from_entity(entity="age", intent="inform_age"), 
                         self.from_entity(entity="age", intent="inform_pnr"), 
                         self.from_entity(entity="age", intent="inform_train_number"), 
                         self.from_entity(entity="age", intent="inform_flight_date"),
                         self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="pnr_number", intent="inform_age"), 
                         self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                         self.from_entity(entity="pnr_number", intent="inform_train_number"),
                         self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="train_number", intent="inform_age"), 
                         self.from_entity(entity="train_number", intent="inform_pnr"), 
                         self.from_entity(entity="train_number", intent="inform_train_number"),
                         self.from_entity(entity="train_number", intent="inform_flight_date"),
                         self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                         self.from_entity(entity="flight_date", intent="inform_age"), 
                         self.from_entity(entity="flight_date", intent="inform_pnr"), 
                         self.from_entity(entity="flight_date", intent="inform_train_number"),
                         self.from_entity(entity="flight_date", intent="inform_flight_date")],
        "class_code":    [self.from_entity(entity="seating_class", intent="inform_seating_class"), 
                          self.from_entity(entity="class_code", intent="inform_seating_class"), 
                          self.from_entity(entity="quota_code", intent="inform_seating_class"), 
                          self.from_entity(entity="station_code", intent="inform_seating_class"), 
                          self.from_entity(entity="seating_class", intent="inform_class_code"), 
                          self.from_entity(entity="class_code", intent="inform_class_code"), 
                          self.from_entity(entity="quota_code", intent="inform_class_code"), 
                          self.from_entity(entity="station_code", intent="inform_class_code"), 
                          self.from_entity(entity="seating_class", intent="inform_quota_code"), 
                          self.from_entity(entity="class_code", intent="inform_quota_code"), 
                          self.from_entity(entity="quota_code", intent="inform_quota_code"), 
                          self.from_entity(entity="station_code", intent="inform_quota_code"), 
                          self.from_entity(entity="seating_class", intent="inform_station_code"), 
                          self.from_entity(entity="class_code", intent="inform_station_code"), 
                          self.from_entity(entity="quota_code", intent="inform_station_code"), 
                          self.from_entity(entity="station_code", intent="inform_station_code")],
        "quota_code":    [self.from_entity(entity="seating_class", intent="inform_seating_class"), 
                          self.from_entity(entity="class_code", intent="inform_seating_class"), 
                          self.from_entity(entity="quota_code", intent="inform_seating_class"), 
                          self.from_entity(entity="station_code", intent="inform_seating_class"), 
                          self.from_entity(entity="seating_class", intent="inform_class_code"), 
                          self.from_entity(entity="class_code", intent="inform_class_code"), 
                          self.from_entity(entity="quota_code", intent="inform_class_code"), 
                          self.from_entity(entity="station_code", intent="inform_class_code"), 
                          self.from_entity(entity="seating_class", intent="inform_quota_code"), 
                          self.from_entity(entity="class_code", intent="inform_quota_code"), 
                          self.from_entity(entity="quota_code", intent="inform_quota_code"), 
                          self.from_entity(entity="station_code", intent="inform_quota_code"), 
                          self.from_entity(entity="seating_class", intent="inform_station_code"), 
                          self.from_entity(entity="class_code", intent="inform_station_code"), 
                          self.from_entity(entity="quota_code", intent="inform_station_code"), 
                          self.from_entity(entity="station_code", intent="inform_station_code")]}

    @staticmethod
    def station_db():
        textfile = open("data/lookup/railwaystations.txt","r")
        stations = textfile.readlines()
        stations = [item.replace("\n", "") for item in stations]
        return stations
    
    @staticmethod
    def class_db():
        textfile = open("data/lookup/classes.txt","r")
        classes = textfile.readlines()
        classes = [item.replace("\n", "") for item in classes]
        return classes

    @staticmethod
    def quota_db():
        textfile = open("data/lookup/quotas.txt","r")
        quotas = textfile.readlines()
        quotas = [item.replace("\n", "") for item in quotas]
        return quotas
    
    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'source_station_name' or slot == 'destination_station_name':
                if value not in self.station_db():
                    dispatcher.utter_template('utter_wrong_station_name', tracker)
                    slot_values[slot] = None
            elif slot == 'train_number':
                if not self.is_int(value) or int(value) < 10000 or int(value) > 99999:
                    dispatcher.utter_template('utter_wrong_train_number', tracker)
                    slot_values[slot] = None
            elif slot == 'train_date':
                try:
                    datetime.strptime(value, '%d-%m-%Y')
                except ValueError:
                    dispatcher.utter_template('utter_wrong_train_date', tracker)
                    slot_values[slot] = None
            elif slot == 'class_code':
                if value not in self.class_db():
                    dispatcher.utter_template('utter_wrong_class_code', tracker)
                    slot_values[slot] = None
            elif slot == 'quota_code':
                if value not in self.quota_db():
                    dispatcher.utter_template('utter_wrong_quota_code', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        train_number = tracker.get_slot('train_number')
        source_station_name = tracker.get_slot('source_station_name')
        destination_station_name = tracker.get_slot('destination_station_name')
        with open('data/validate/railwaystations.json') as railway_data:
            railways = json.load(railway_data)
            for railway in railways["features"]:
                if source_station_name.upper() == railway["properties"]["name"].upper():
                    source_station_code = railway["properties"]["code"]
                if destination_station_name.upper() == railway["properties"]["name"].upper():
                    destination_station_code = railway["properties"]["code"]
        train_date = tracker.get_slot('train_date')
        class_code = tracker.get_slot('class_code')
        with open('data/validate/classes.json') as class_data:
            classes = json.load(class_data)
            for classe in classes["class"]:
                for c in classe.keys():
                    if class_code == c:
                        class_code2 = classe[c]
        quota_code = tracker.get_slot('quota_code')
        with open('data/validate/quotas.json') as quota_data:
            quotas = json.load(quota_data)
            for quota in quotas["quota"]:
                for q in quota.keys():
                    if quota_code == q:
                        quota_code2 = quota[q]
        base_url = "http://api.railwayapi.com/v2/check-seat/train/"
        complete_url = str(base_url) + str(train_number) + "/source/" + str(source_station_code) + "/dest/" + str(destination_station_code) + "/date/" + str(train_date) + "/pref/" + str(class_code2) + "/quota/" + str(quota_code2) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            source_station_name = result["from_station"]["name"]
            destination_station_name = result["to_station"]["name"]
            quota_name = result["quota"]["name"]
            class_name = result["journey_class"]["name"]
            train_name = result["train"]["name"]
            availability = result["availability"]
            response1 = """Train Number - {} \nTrain Name - {} \nDate - {} \nSource Station Name - {} \nSource Station Code - {} \nDestination Station Name - {} \nDestination Station Code - {} \nClass Name - {} \nClass Code - {} \nQuota Name - {} \nQuota Code - {} \n\n""".format(train_number, train_name, train_date, source_station_name, source_station_code, destination_station_name, destination_station_code, class_name, class_code, quota_name, quota_code)
            response = response1
            for avail in availability:
                availstatus = avail["status"]
                response2 = """Availability - {} \n""".format(availstatus)
                response += response2
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('train_number',train_number), SlotSet('source_station_name',source_station_name), SlotSet('destination_station_name',destination_station_name), SlotSet('class_code',class_code), SlotSet('quota_code',quota_code), SlotSet('train_date',train_date)]
class FormActionStation(FormAction):
    def name(self):
        return "action_trains_station"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [ "source_station_name","destination_station_name","train_date"]

    def slot_mappings(self):
        return {"source_station_name": [self.from_entity(entity="city", intent="inform_source_airport"), 
                                        self.from_entity(entity="city", intent="inform_destination_airport"), 
                                        self.from_entity(entity="city", intent="inform_city"), 
                                        self.from_entity(entity="city", intent="inform_source_station_name"), 
                                        self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                        self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                        self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                        self.from_entity(entity="station_name", intent="inform_city"), 
                                        self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                        self.from_entity(entity="station_name", intent="inform_destination_station_name")],
        "destination_station_name": [self.from_entity(entity="city", intent="inform_source_airport"), 
                                     self.from_entity(entity="city", intent="inform_destination_airport"), 
                                     self.from_entity(entity="city", intent="inform_city"), 
                                     self.from_entity(entity="city", intent="inform_source_station_name"), 
                                     self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                     self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                     self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                     self.from_entity(entity="station_name", intent="inform_city"), 
                                     self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                     self.from_entity(entity="station_name", intent="inform_destination_station_name")]}

    @staticmethod
    def station_db():
        textfile = open("data/lookup/railwaystations.txt","r")
        stations = textfile.readlines()
        stations = [item.replace("\n", "") for item in stations]
        return stations

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'source_station_name' or slot == 'destination_station_name':
                if value.upper() not in self.station_db():
                    dispatcher.utter_template('utter_wrong_station_name', tracker)
                    slot_values[slot] = None
            elif slot == 'train_date':
                try:
                    datetime.strptime(value, '%d-%m-%Y')
                except ValueError:
                    dispatcher.utter_template('utter_wrong_train_date', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        source_station_name = tracker.get_slot('source_station_name')
        destination_station_name = tracker.get_slot('destination_station_name')
        with open('data/validate/railwaystations.json') as railway_data:
            railways = json.load(railway_data)
            for railway in railways["features"]:
                if source_station_name.upper() == railway["properties"]["name"].upper():
                    source_station_code = railway["properties"]["code"]
                if destination_station_name.upper() == railway["properties"]["name"].upper():
                    destination_station_code = railway["properties"]["code"]
        train_date = tracker.get_slot('train_date')
        base_url = "http://api.railwayapi.com/v2/between/source/"
        complete_url = str(base_url) + str(source_station_code) + "/dest/" + str(destination_station_code) + "/date/" + str(train_date) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            totalno = result["total"]
            trains = result["trains"]
            response = """Trains Between Stations: \n"""
            for train in trains:
                source_station_name = train["from_station"]["name"]
                destination_station_name = train["to_station"]["name"]
                train_name = train["name"]
                train_number = train["number"]
                source_departure_time = train["src_departure_time"]
                destination_arrival_time = train["dest_arrival_time"]
                travel_time = train["travel_time"]
                response1 = """Train Number - {} \nTrain Name - {} \nDate - {} \nSource Station Name - {} \nSource Station Code - {} \nDestination Station Name - {} \nDestination Station Code - {} \nTotal Stations - {} \nSource Departure Time - {} \nDestination Arrival Time - {} \nTravel Time - {} \n\n""".format(train_number, train_name, train_date, source_station_name, source_station_code, destination_station_name, destination_station_code, totalno, source_departure_time, destination_arrival_time, travel_time)
                response += response1
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('source_station_name',source_station_name), SlotSet('destination_station_name',destination_station_name), SlotSet('train_date',train_date)]
class FormActionTrainsCancel(FormAction):
    def name(self):
        return "action_trains_cancel"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["train_date"]

    def slot_mappings(self):
        return {"train_date": [self.from_entity(entity="train_date", intent="inform_train_date"), self.from_entity(entity="no_of_people", intent="inform_train_date")]}
    
    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'train_date':            
                try:
                    datetime.strptime(value, '%d-%m-%Y')
                except ValueError:
                    dispatcher.utter_template('utter_wrong_train_date', tracker)
                    slot_values[slot] = None
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        train_date = tracker.get_slot('train_date')
        base_url = "http://api.railwayapi.com/v2/cancelled/date/"
        complete_url = str(base_url) + str(train_date) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            trains = result["trains"]
            limit = 0
            response = """Trains Cancelled: \n"""
            for train in trains:
                source_station_name = train["source"]["name"]
                destination_station_name = train["dest"]["name"]
                source_station_code = train["source"]["code"]
                destination_station_code = train["dest"]["code"]
                train_name = train["name"]
                train_number = train["number"]
                start_time = train["start_time"]
                response1 = """Train Number - {} \nTrain Name - {} \nDate - {} \nSource Station Name - {} \nSource Station Code - {} \nDestination Station Name - {} \nDestination Station Code - {} \nStart Time - {} \n\n""".format(train_number, train_name, train_date, source_station_name, source_station_code, destination_station_name, destination_station_code, start_time)
                response += response1
                limit += 1
                if(limit == 10):
                    break	
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('train_date',train_date)]
class FormActionTrainsReschedule(FormAction):
    def name(self):
        return "action_trains_reschedule"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["train_date"]

    def slot_mappings(self):
        return {"train_date": [self.from_entity(entity="train_date", intent="inform_train_date"), self.from_entity(entity="no_of_people", intent="inform_train_date")]}

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'train_date':
                try:
                    datetime.strptime(value, '%d-%m-%Y')
                except ValueError:
                    dispatcher.utter_template('utter_wrong_train_date', tracker)
                    slot_values[slot] = None
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        train_date = tracker.get_slot('train_date')
        base_url = "http://api.railwayapi.com/v2/rescheduled/date/"
        complete_url = str(base_url) + str(train_date) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            trains = result["trains"]
            limit = 0
            response = """Trains Rescheduled: \n"""
            for train in trains:
                source_station_name = train["from_station"]["name"]
                destination_station_name = train["to_station"]["name"]
                source_station_code = train["from_station"]["code"]
                destination_station_code = train["to_station"]["code"]
                train_name = train["name"]
                train_number = train["number"]
                rescheduled_time = train["rescheduled_time"]
                rescheduled_date = train["rescheduled_date"]
                time_diff = train["time_diff"]
                response1 = """Train Number - {} \nTrain Name - {} \nDate - {} \nSource Station Name - {} \nSource Station Code - {} \nDestination Station Name - {} \nDestination Station Code - {} \nRescheduled Time - {} \nRescheduled Date - {} \nTime Difference - {} \n\n""".format(train_number, train_name, train_date, source_station_name, source_station_code, destination_station_name, destination_station_code, rescheduled_time, rescheduled_date, time_diff)
                response += response1
                limit += 1
                if(limit == 10):
                    break	
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('train_date',train_date)]
class FormActionTrainsStationCode(FormAction):
    def name(self):
        return "action_trains_station_code"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["city"]

    def slot_mappings(self):
        return {"city": [self.from_entity(entity="city", intent="inform_source_airport"), 
                         self.from_entity(entity="city", intent="inform_destination_airport"), 
                         self.from_entity(entity="city", intent="inform_city"), 
                         self.from_entity(entity="city", intent="inform_source_station_name"), 
                         self.from_entity(entity="city", intent="inform_destination_station_name"), 
                         self.from_entity(entity="station_name", intent="inform_source_airport"), 
                         self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                         self.from_entity(entity="station_name", intent="inform_city"), 
                         self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                         self.from_entity(entity="station_name", intent="inform_destination_station_name")]}

    @staticmethod
    def city_db():
        textfile=open("./data/validate/indiancities.json","r")
        cities = textfile.readlines()
        cities = [item.replace("\n", "") for item in cities]
        return cities

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'city' :
                if value not in self.city_db():
                    dispatcher.utter_template('utter_wrong_city', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        city = tracker.get_slot('city')
        base_url = "http://api.railwayapi.com/v2/name-to-code/station/"
        complete_url = str(base_url) + str(city) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            stations = result["stations"]
            response = """Station Name to Station Code\n\n"""
            for station in stations:
                station_name = station["name"]
                station_code = station["code"]
                response1 = """Station Name - {} \tStation Code - {} \n\n""".format(station_name, station_code)
                response += response1
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('city',city)]
class FormActionTrainsStationName(FormAction):
    def name(self):
        return "action_trains_station_name"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["station_code"]

    def slot_mappings(self):
        return {"station_code": [self.from_entity(entity="seating_class", intent="inform_seating_class"), 
                                 self.from_entity(entity="class_code", intent="inform_seating_class"), 
                                 self.from_entity(entity="quota_code", intent="inform_seating_class"), 
                                 self.from_entity(entity="station_code", intent="inform_seating_class"), 
                                 self.from_entity(entity="seating_class", intent="inform_class_code"), 
                                 self.from_entity(entity="class_code", intent="inform_class_code"), 
                                 self.from_entity(entity="quota_code", intent="inform_class_code"), 
                                 self.from_entity(entity="station_code", intent="inform_class_code"), 
                                 self.from_entity(entity="seating_class", intent="inform_quota_code"), 
                                 self.from_entity(entity="class_code", intent="inform_quota_code"), 
                                 self.from_entity(entity="quota_code", intent="inform_quota_code"), 
                                 self.from_entity(entity="station_code", intent="inform_quota_code"), 
                                 self.from_entity(entity="seating_class", intent="inform_station_code"), 
                                 self.from_entity(entity="class_code", intent="inform_station_code"), 
                                 self.from_entity(entity="quota_code", intent="inform_station_code"), 
                                 self.from_entity(entity="station_code", intent="inform_station_code")]}

    @staticmethod
    def stationcode_db():
        textfile=open("data/lookup/trainstationcodes.txt","r")
        codes = textfile.readlines()
        codes = [item.replace("\n", "") for item in codes]
        return codes

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'station_code' :
                if value not in self.stationcode_db():
                    dispatcher.utter_template('utter_wrong_station_code', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        api_key = "*railwayapi key*"
        station_code = tracker.get_slot('station_code')
        base_url = "http://api.railwayapi.com/v2/code-to-name/code/"
        complete_url = str(base_url) + str(station_code) + "/apikey/" + str(api_key) + "/"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        if result["response_code"] == 200 : 
            stations = result["stations"]
            response = """Station Code to Station Name\n\n"""
            for station in stations:
                station_name = station["name"]
                station_codee = station["code"]
                response1 = """Station Name - {} \tStation Code - {} \n\n""".format(station_name, station_codee)
                response += response1
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('station_code',station_code)]
class ActionTrainClassInformation(Action):
    def name(self):
        return "action_trains_class_info"

    def run(self, dispatcher, tracker, domain):
        response0 = """Here are some classes:\n\n"""
        response1 = """1) 1A - AC First Class:\nThis is the most expensive class, where the fares are almost on par with airfare. There are eight cabins (including two coupes) in the full AC First Class coach and three cabins (including one coupe) in the half AC First Class coach. This air-conditioned coach is present only on popular routes and can carry 18 passengers (full coach) or 10 passengers (half coach). The sleeper berths are extremely wide, carpeted, have sleeping accommodations and have privacy features like personal coupes.\n"""
        response2 = """2) 2A - AC Two-Tier:\nThese air-conditioned coaches have sleeping berths across eight bays. Berths are usually arranged in two tiers in bays of six, four across the width of the coach and two berths longways on the other side of the corridor, with curtains along the gangway or corridor. Bedding is included with the fare. A coach can carry 48 passengers (full coach) or 20 passengers (half coach).\n"""
        response3 = """3) 3A - AC Three-Tier:\nAir conditioned coaches with 64 sleeping berths. Berths are usually arranged as in 2AC but with three tiers across the width and two longways as before giving eight bays of eight. They are slightly less well-appointed, usually no reading lights or curtained off gangways. Bedding is included with fare. It carries 64 passengers per coach.\n"""
        response4 = """4) FC - First Class:\nSimilar as 1AC, but without air conditioning. No bedding is available in this class. The berths are not as wide and spacious as in 1AC. There is one coach attendant to help the passengers. This class has been phased out completely. However, heritage trains still have this class.\n"""
        response5 = """5) 3E - AC Three-Tier (Economy):\nAir conditioned coaches with sleeping berths, present in Garib Rath Express trains. Berths are usually arranged as in 3A but with three tiers across the width and three longways. They are slightly less well-appointed, usually no reading lights or curtained off gangways. Bedding is not included with fare.\n"""
        response6 = """6) EC - Executive Chair Car:\nAn air-conditioned coach with large spacious seats and legroom. It has a total of four seats in a row used for day travel between cities. This class of travel is available on Tejas Express and Shatabdi Express trains.\n"""
        response7 = """7) CC - AC Chair Car:\nAn air-conditioned seater coach with a total of five seats in a row used for day travel between cities. AC Double Deck seater coaches are used in Double Decker Express.\n"""
        response8 = """8) SL - Sleeper Class\nThe sleeper class is the most common coach in the Indian Railways with ten or more coaches of this type attached to the train. These are regular sleeping coaches with three berths across the width and two longways, without air conditioning. It carries 72 passengers per coach.\n"""
        image1 = "https://erail.in/blog/Images/Post/railway-coach-class_1.jpg"
        image2 = "https://erail.in/blog/Images/Post/railway-coach-class_3.jpg"
        image3 = "https://erail.in/blog/Images/Post/railway-coach-class_5.jpg"
        image4 = "https://erail.in/blog/Images/Post/railway-coach-class_2.jpg"
        image5 = "https://erail.in/blog/Images/Post/railway-coach-class_10.jpg"
        image6 = "https://erail.in/blog/Images/Post/railway-coach-class_8.jpg"
        image7 = "https://erail.in/blog/Images/Post/railway-coach-class_7.jpg"
        image8 = "https://erail.in/blog/Images/Post/railway-coach-class_9.jpg"
        dispatcher.utter_message(response0)
        dispatcher.utter_message(response1)
        dispatcher.utter_message(image1)
        dispatcher.utter_message(response2)
        dispatcher.utter_message(image2)
        dispatcher.utter_message(response3)
        dispatcher.utter_message(image3)
        dispatcher.utter_message(response4)
        dispatcher.utter_message(image4)
        dispatcher.utter_message(response5)
        dispatcher.utter_message(image5)
        dispatcher.utter_message(response6)
        dispatcher.utter_message(image6)
        dispatcher.utter_message(response7)
        dispatcher.utter_message(image7)
        dispatcher.utter_message(response8)
        dispatcher.utter_message(image8)
        return []
class ActionTrainQuotaInformation(Action):
    def name(self):
        return "action_trains_quota_info"

    def run(self, dispatcher, tracker, domain):
        response0 = """Here are some quotas:\n\n"""
        response1 = """1) General Quota (GN):\nA railways reservation General quota (GN) can be defined as the total number of tickets that can be issued for travel from the originating station issued by booking offices of the originating and other nearby stations. Majority of these seats in a particular train are reserved for long distances.\n"""
        response2 = """2) Ladies Quota (LD):\nLadies Quota is the one under which only ladies travelling alone or with a child less than 12 years of age are eligible to book. In some trains, a total number of 6 berths are earmarked under ladies quota in Sleeper Class (SL) and Second Seating Class (2S) for ladies irrespective of age. There is no any additional charge for using this quota for females.\n"""
        response3 = """3) High Official Quota (HO):\nRailways reservation head quarters/high official Quota includes small number of seats and berths set aside for the rail officials, VIPs, high bureaucrats, etc. The allotment is done on first and first served basis. The request for booking train tickets under such quota should be made in advance to the quota controlling authority.\n"""
        response4 = """4) Defence Quota (DF):\nRailways reservation Defense Quota can only be availed by the defense officials. The defense staff can book the tickets in any particular train in defense quota with the use of their ID cards.\n"""
        response5 = """5) Parliament House Quota (PH):\nRailways reservation Parliament house Quota represents the number of seats allotted to members of Parliament in order to meet their urgent travel requirements. It can be availed by Centre and State ministers, judges of Supreme of India, high court judges of various states and MLAs.\n"""
        response6 = """6) Foreign Tourist Quota (FT):\nRailways reservation Foreign Tourist Quota is a special number of seats or berths reserved for international tourists in almost all the important trains and in different classes.\n"""
        response7 = """7) Duty Pass Quota (DP):\Railways reservation Duty pass quota is meant for railways staffs on duty. All those railway staffs that need to travel in trains to perform their duty have a duty pass through which they can board the trains.\n"""
        response8 = """8) Tatkal Quota (TQ)\nRailways reservation Tatkal quota was introduced to help the passengers to book train tickets in different classes in case of emergencies. Except First Class AC and Executive Class, the Tatkal Booking are available to all class. Tatkal booking does not allow opting for Ladies and General Quota. Find details here about ITCTC Tatkal quota.\n"""
        response9 = """9) Premium Tatkal Quota (PT)\nPremium Tatkal Quota is a reservation quota introduced by Railways with dynamic fare pricing in a limited number of trains on experimental basis. The main difference of premium tatkal scheme, with all other ticketing including the regular Tatkal tickets, is the dynamic nature of ticket cost. Price of premium tatkal tickets increase as the demand increases, especially towards the the end of the reservation period. If there is no demand, the price of the premium Tatkal would be comparable with the Tatkal fares.\n"""
        response10 = """10) Female(above 45 Year)/Senior Citizen/Travelling alone Quota (SS):\nUnder Railways reservation Female (above 45 Year)/Senior Citizen/Travelling alone quota (SS Quota), lower berths are provided to those senior citizens and female above 45 years who are travelling alone. Special trains have been provided for those senior citizens who use wheel chair.\n"""
        response11 = """11) Physically Handicapped Quota (HP):\nRailways reservation physically handicapped quota provides various additional facilities to the passengers who are physically challenged. They are provided with different reservation counters at the railway reservation centers. Two sleeper class berths are been allotted in all the trains for those who are travelling on handicapped concessional ticket.\n"""
        response12 = """12) Railway Employee Staff on Duty for the train Quota (RE):\nRailways reservation Employee Staff on Duty for the train is the quota, for employees of railways, which facilitates its employees by providing exclusive journey passes.\n"""
        response13 = """13) General Quota Road Side (GNRS):\nThis is also termed as remote location quota. Railways reservation General Road Side Quota (GNRS) describes of those railway stations that are still not connected to Passenger Reservation System. PRS maintains the database of reservation and many stations, not being connected to PRS maintain the records manually.\n"""
        response14 = """14) Out Station Quota (OS):\nRailways reservation Out Station Quota is being operated even after provision of computerized PRS facility. Out station quota may be immediately withdrawn and merged with the database of the nearest remote location having no PRS. This quota requires a confirmation from zonal Railways. This quota is also general quota but can not be booked online.\n"""
        response15 = """15) Pooled Quota (PQ):\nRailway reservation Pooled Quota(PQ) consists of small number of berths. This quota is been charted at the starting station of the train. A traveler seeking reservation from the starting station is been allotted the reservation under this quota. There is no provision of Reservation Against Cancellation (RAC) in pooled Quota. Only confirmed tickets are issued for passengers travelling under head of this Pooled Quota of Indian Railway.\n"""
        response16 = """16) Reservation Against Cancellation (RAC):\nRailway reservation Against Cancellation(RAC) is the quota of Indian railways which accommodates two passengers on a berth. A traveler bearing a RAC ticket can travel in the respective train but a person in waiting list is not allowed to do so. Generally tickets issued under RAC quota get confirmed after passing of some stations or could also become confirmed ticket in case of cancellation of confirmed or RAC tickets. The holder of RAC ticket remains after cancellation of tickets by other passengers enjoy full berth for rest of journey.\n"""
        response17 = """17) Road Side Quota (RS)\nSmaller intermediate stations that do not participate in the networked computerized reservation system issue tickets from specific quotas, known as Road Side Quotas (‘RS’).\n"""
        response18 = """18) Yuva Quota (YU):\nRailways Yuva reservation quota provides the facility of reservation to the unemployed travelers, aged between 15-45 years, certified by National Rural Employment Guarantee (NAREGA). The tickets for Yuva quota could be reserved on the general reservation counters. The certificate is mandatory for concessions.\n"""
        response19 = """19) Lower Berth Quota (LB)\nRailways reservation Lower Berth Quota is reserved for a lady who is above 45 years and travelling alone, for a senior citizen and for a pregnant lady.\n"""
        dispatcher.utter_message(response0)
        dispatcher.utter_message(response1)
        dispatcher.utter_message(response2)
        dispatcher.utter_message(response3)
        dispatcher.utter_message(response4)
        dispatcher.utter_message(response5)
        dispatcher.utter_message(response6)
        dispatcher.utter_message(response7)
        dispatcher.utter_message(response8)
        dispatcher.utter_message(response9)
        dispatcher.utter_message(response10)
        dispatcher.utter_message(response11)
        dispatcher.utter_message(response12)
        dispatcher.utter_message(response13)
        dispatcher.utter_message(response14)
        dispatcher.utter_message(response15)
        dispatcher.utter_message(response16)
        dispatcher.utter_message(response17)
        dispatcher.utter_message(response18)
        dispatcher.utter_message(response19)
        return []
class FormActionFlightSearch(FormAction):
    def name(self):
        return "action_flight_search"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [ "source_airport", "destination_airport", "flight_date", "seating_class", "no_of_adults", "no_of_children", "no_of_infants"]

    def slot_mappings(self):
        return {"source_airport": [self.from_entity(entity="city", intent="inform_source_airport"), 
                                   self.from_entity(entity="city", intent="inform_destination_airport"), 
                                   self.from_entity(entity="city", intent="inform_city"), 
                                   self.from_entity(entity="city", intent="inform_source_station_name"), 
                                   self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                   self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                   self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                   self.from_entity(entity="station_name", intent="inform_city"), 
                                   self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                   self.from_entity(entity="station_name", intent="inform_destination_station_name")],
        "destination_airport": [self.from_entity(entity="city", intent="inform_source_airport"), 
                                self.from_entity(entity="city", intent="inform_destination_airport"), 
                                self.from_entity(entity="city", intent="inform_city"), 
                                self.from_entity(entity="city", intent="inform_source_station_name"), 
                                self.from_entity(entity="city", intent="inform_destination_station_name"), 
                                self.from_entity(entity="station_name", intent="inform_source_airport"), 
                                self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                                self.from_entity(entity="station_name", intent="inform_city"), 
                                self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                                self.from_entity(entity="station_name", intent="inform_destination_station_name")],
        "seating_class": [self.from_entity(entity="seating_class", intent="inform_seating_class"), 
                          self.from_entity(entity="class_code", intent="inform_seating_class"), 
                          self.from_entity(entity="quota_code", intent="inform_seating_class"), 
                          self.from_entity(entity="station_code", intent="inform_seating_class"), 
                          self.from_entity(entity="seating_class", intent="inform_class_code"), 
                          self.from_entity(entity="class_code", intent="inform_class_code"), 
                          self.from_entity(entity="quota_code", intent="inform_class_code"), 
                          self.from_entity(entity="station_code", intent="inform_class_code"), 
                          self.from_entity(entity="seating_class", intent="inform_quota_code"), 
                          self.from_entity(entity="class_code", intent="inform_quota_code"), 
                          self.from_entity(entity="quota_code", intent="inform_quota_code"), 
                          self.from_entity(entity="station_code", intent="inform_quota_code"), 
                          self.from_entity(entity="seating_class", intent="inform_station_code"), 
                          self.from_entity(entity="class_code", intent="inform_station_code"), 
                          self.from_entity(entity="quota_code", intent="inform_station_code"), 
                          self.from_entity(entity="station_code", intent="inform_station_code")],
        "no_of_adults": [self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                         self.from_entity(entity="no_of_people", intent="inform_age"), 
                         self.from_entity(entity="no_of_people", intent="inform_pnr"),
                         self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                         self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                         self.from_entity(entity="age", intent="inform_no_of_adults"), 
                         self.from_entity(entity="age", intent="inform_no_of_children"), 
                         self.from_entity(entity="age", intent="inform_no_of_infants"), 
                         self.from_entity(entity="age", intent="inform_age"), 
                         self.from_entity(entity="age", intent="inform_pnr"), 
                         self.from_entity(entity="age", intent="inform_train_number"), 
                         self.from_entity(entity="age", intent="inform_flight_date"),
                         self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="pnr_number", intent="inform_age"), 
                         self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                         self.from_entity(entity="pnr_number", intent="inform_train_number"),
                         self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="train_number", intent="inform_age"), 
                         self.from_entity(entity="train_number", intent="inform_pnr"), 
                         self.from_entity(entity="train_number", intent="inform_train_number"),
                         self.from_entity(entity="train_number", intent="inform_flight_date"),
                         self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                         self.from_entity(entity="flight_date", intent="inform_age"), 
                         self.from_entity(entity="flight_date", intent="inform_pnr"), 
                         self.from_entity(entity="flight_date", intent="inform_train_number"),
                         self.from_entity(entity="flight_date", intent="inform_flight_date")],
        "no_of_children": [self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                         self.from_entity(entity="no_of_people", intent="inform_age"), 
                         self.from_entity(entity="no_of_people", intent="inform_pnr"),
                         self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                         self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                         self.from_entity(entity="age", intent="inform_no_of_adults"), 
                         self.from_entity(entity="age", intent="inform_no_of_children"), 
                         self.from_entity(entity="age", intent="inform_no_of_infants"), 
                         self.from_entity(entity="age", intent="inform_age"), 
                         self.from_entity(entity="age", intent="inform_pnr"), 
                         self.from_entity(entity="age", intent="inform_train_number"), 
                         self.from_entity(entity="age", intent="inform_flight_date"),
                         self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="pnr_number", intent="inform_age"), 
                         self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                         self.from_entity(entity="pnr_number", intent="inform_train_number"),
                         self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="train_number", intent="inform_age"), 
                         self.from_entity(entity="train_number", intent="inform_pnr"), 
                         self.from_entity(entity="train_number", intent="inform_train_number"),
                         self.from_entity(entity="train_number", intent="inform_flight_date"),
                         self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                         self.from_entity(entity="flight_date", intent="inform_age"), 
                         self.from_entity(entity="flight_date", intent="inform_pnr"), 
                         self.from_entity(entity="flight_date", intent="inform_train_number"),
                         self.from_entity(entity="flight_date", intent="inform_flight_date")],
        "no_of_infants": [self.from_entity(entity="no_of_people", intent="inform_no_of_adults"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_children"), 
                         self.from_entity(entity="no_of_people", intent="inform_no_of_infants"), 
                         self.from_entity(entity="no_of_people", intent="inform_age"), 
                         self.from_entity(entity="no_of_people", intent="inform_pnr"),
                         self.from_entity(entity="no_of_people", intent="inform_train_number"), 
                         self.from_entity(entity="no_of_people", intent="inform_flight_date"),
                         self.from_entity(entity="age", intent="inform_no_of_adults"), 
                         self.from_entity(entity="age", intent="inform_no_of_children"), 
                         self.from_entity(entity="age", intent="inform_no_of_infants"), 
                         self.from_entity(entity="age", intent="inform_age"), 
                         self.from_entity(entity="age", intent="inform_pnr"), 
                         self.from_entity(entity="age", intent="inform_train_number"), 
                         self.from_entity(entity="age", intent="inform_flight_date"),
                         self.from_entity(entity="pnr_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="pnr_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="pnr_number", intent="inform_age"), 
                         self.from_entity(entity="pnr_number", intent="inform_pnr"), 
                         self.from_entity(entity="pnr_number", intent="inform_train_number"),
                         self.from_entity(entity="pnr_number", intent="inform_flight_date"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_adults"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_children"), 
                         self.from_entity(entity="train_number", intent="inform_no_of_infants"), 
                         self.from_entity(entity="train_number", intent="inform_age"), 
                         self.from_entity(entity="train_number", intent="inform_pnr"), 
                         self.from_entity(entity="train_number", intent="inform_train_number"),
                         self.from_entity(entity="train_number", intent="inform_flight_date"),
                         self.from_entity(entity="flight_date", intent="inform_no_of_adults"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_children"), 
                         self.from_entity(entity="flight_date", intent="inform_no_of_infants"), 
                         self.from_entity(entity="flight_date", intent="inform_age"), 
                         self.from_entity(entity="flight_date", intent="inform_pnr"), 
                         self.from_entity(entity="flight_date", intent="inform_train_number"),
                         self.from_entity(entity="flight_date", intent="inform_flight_date")]}

    @staticmethod
    def city_db():
        textfile=open("data/lookup/internationalcities.txt","r")
        cities = textfile.readlines()
        cities = [item.replace("\n", "") for item in cities]
        return cities

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'source_airport' or slot == 'destination_airport':
                if value not in self.city_db():
                    dispatcher.utter_template('utter_wrong_city', tracker)
                    slot_values[slot] = None

            elif slot == 'no_of_adults':
                if not self.is_int(value) or int(value) < 1 or int(value) > 9:
                    dispatcher.utter_template('utter_wrong_no_of_people', tracker)
                    slot_values[slot] = None
            
            elif slot == 'no_of_children' or slot == 'no_of_infants':
                if not self.is_int(value) or int(value) < 0 or int(value) > 9:
                    dispatcher.utter_template('utter_wrong_no_of_people', tracker)
                    slot_values[slot] = None

            elif slot == 'seating_class':
                if isinstance(value, str):
                    if value in ['Economy','economy','ECONOMY','e','E']:
                        slot_values[slot] = 'E'
                    elif value in ['Business','business','BUSINESS','b','B']:
                        slot_values[slot] = 'B'
                    else:
                        dispatcher.utter_template('utter_wrong_seating_class', tracker)
                        slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        app_id = "*goibibo id*"
        app_key = "*goibibo key*"
        source_airport = tracker.get_slot('source_airport')
        destination_airport = tracker.get_slot('destination_airport')
        flight_date = tracker.get_slot('flight_date')
        seating_class = tracker.get_slot('seating_class')
        no_of_adults = tracker.get_slot('no_of_adults')
        no_of_children = tracker.get_slot('no_of_children')
        no_of_infants = tracker.get_slot('no_of_infants')
        with open('./data/validate/airports.json') as airport_data:
            airports = json.load(airport_data)
            for airport in airports["airport"]:
                if source_airport == airport["city"]:
                    source_airport_code = airport["code"]
                    source_country = airport["country"]
                    source_airport_name = airport["airportname"]
                if destination_airport == airport["city"]:
                    destination_airport_code = airport["code"]
                    destination_country = airport["country"]
                    destination_airport_name = airport["airportname"]
        base_url = "http://developer.goibibo.com/api/search/?app_id="
        complete_url = str(base_url) + str(app_id) + "&app_key=" + str(app_key) + "&format=json&source=" + str(source_airport_code) + "&destination=" + str(destination_airport_code) + "&dateofdeparture=" + str(flight_date) + "&seatingclass=" + str(seating_class) + "&adults=" + str(no_of_adults) + "&children=" + str(no_of_children) + "&infants=" + str(no_of_infants) + "&counter=100"
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        limit = 0
        if response_ob.status_code == 200 : 
            response = """Flight Search:\n\n"""
            terminals = result["data"]["onwardflights"]
            for terminal in terminals:
                flight_code = terminal["flightcode"]
                source_departure_time = terminal["deptime"]
                destination_arrival_time = terminal["arrtime"]
                source_departure_date = terminal["depdate"]
                destination_arrival_date = terminal["arrdate"]
                duration = terminal["duration"]
                airline = terminal["airline"]
                stops = terminal["stops"]
                fare = terminal["fare"]["totalfare"]
                response1 = """Source City - {} \nSource City Code - {} \nSource City Airport Name - {} \nSource City Country - {} \nDestination City - {} \nDestination City Code - {} \nDestination City Airport Name - {} \nDestination City Country - {} \nDate - {} \nSource Departure Time - {} \nSource Departure Date - {} \nDestination Departure Time - {} \nDestination Departure Date - {} \nAirline - {} \nFlight Code - {} \nSeating Class - {} \nNumber of Adults - {} \nNumber of Children - {} \nNumber of Infants - {} \nDuration - {} \nStops - {} \nFare - Rs.{} \n\n""".format(source_airport, source_airport_code, source_airport_name, source_country, destination_airport, destination_airport_code, destination_airport_name, destination_country, flight_date, source_departure_time, source_departure_date, destination_arrival_time, destination_arrival_date, airline, flight_code, seating_class, no_of_adults, no_of_children, no_of_infants, duration, stops, fare)
                response += response1	
                limit += 1
                if(limit == 10):
                    break			
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('source_airport',source_airport),SlotSet('destination_airport',destination_airport),SlotSet('flight_date',flight_date),SlotSet('seating_class',seating_class),SlotSet('no_of_adults',no_of_adults),SlotSet('no_of_children',no_of_children),SlotSet('no_of_infants',no_of_infants)]
class ActionFlightClassInformation(Action):
    def name(self):
        return "action_flight_class_info"

    def run(self, dispatcher, tracker, domain):
        response0 = """Here are some classes:\n\n"""
        response1 = """1) E - Economy Class:\nThis class is designed for budgeted traveler in each and every major airlines. Economy class is the lowest travel class seat of air travel. It provides small screen in front of your seat for videos, one blanket, head phone, magazines, one pillow, meal, and limited beverage.\n"""
        response2 = """2) B - Business Class:\nThe Business Class ticket entitles a traveller to a higher level of travel class than the regular economy class ticket. Available on a number of airlines, it is known by different brand names, but is uniformly more expensive than an economy class ticket. Originally, business class was designed as a travel class between economy and first class, but of late it has replaced or been merged with first class, often being the highest class of travel on many airlines. The benefits of a business class ticket include quality seating, food, drinks, service, ground service, privileges while boarding and differences in waiting time.\n"""
        image1 = "https://c1.momondo.net/content/articles/4d/4ddcbbae-9a89-3f1e-93d1-5ef178398945.jpg"
        image2 = "https://c1.momondo.net/content/articles/5f/5f1f4a50-8153-36cd-8b2f-da1e882e3615.jpg"
        dispatcher.utter_message(response0)
        dispatcher.utter_message(response1)
        dispatcher.utter_message(image1)
        dispatcher.utter_message(response2)
        dispatcher.utter_message(image2)
        return []
class FormActionHotelSearch(FormAction):
    def name(self):
        return "action_hotels_search"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["city"]

    def slot_mappings(self):
        return {"city": [self.from_entity(entity="city", intent="inform_source_airport"), 
                         self.from_entity(entity="city", intent="inform_destination_airport"), 
                         self.from_entity(entity="city", intent="inform_city"), 
                         self.from_entity(entity="city", intent="inform_source_station_name"), 
                         self.from_entity(entity="city", intent="inform_destination_station_name"), 
                         self.from_entity(entity="station_name", intent="inform_source_airport"), 
                         self.from_entity(entity="station_name", intent="inform_destination_airport"), 
                         self.from_entity(entity="station_name", intent="inform_city"), 
                         self.from_entity(entity="station_name", intent="inform_source_station_name"), 
                         self.from_entity(entity="station_name", intent="inform_destination_station_name")]}

    @staticmethod
    def city_db():
        textfile=open("data/lookup/hotelcities.txt","r",encoding = "utf-16")
        cities = textfile.readlines()
        cities = [item.replace("\n", "") for item in cities]
        return cities

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),"Failed to validate slot {0} with action {1}".format(slot_to_fill,self.name()))
        for slot, value in slot_values.items():
            if slot == 'city':
                if value not in self.city_db():
                    dispatcher.utter_template('utter_wrong_city', tracker)
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        app_id = "*goibibo id*"
        app_key = "*goibibo key*"
        city = tracker.get_slot('city')
        with open('./data/validate/hotelcities.json',encoding='utf-16', errors='ignore') as hotel_data:
            hotels = json.load(hotel_data)
            for hotel in hotels:
                if city == hotel["City name"]:
                    city_id = hotel['City ID']
        base_url = "https://developer.goibibo.com/api/voyager/get_hotels_by_cityid/?app_id="
        complete_url = str(base_url) + str(app_id) + "&app_key=" + str(app_key) + "&city_id=" + str(city_id)
        response_ob = requests.get(complete_url) 
        result = response_ob.json() 
        limit = 0
        response = """Here are some Hotels at {}:\n\n""".format(city)
        if response_ob.status_code == 200 : 
            for hotel in result['data']:
                name = result['data'][hotel]['hotel_data_node']['name']
                property_type = result['data'][hotel]['hotel_data_node']['property_type']
                no_of_rooms = result['data'][hotel]['hotel_data_node']['no_of_rooms']
                facilities = result['data'][hotel]['hotel_data_node']['facilities']['mapped']
                hrating = result['data'][hotel]['hotel_data_node']['rating']
                address = result['data'][hotel]['hotel_data_node']['loc']['vendor_location']
                state = result['data'][hotel]['hotel_data_node']['loc']['state']
                location = result['data'][hotel]['hotel_data_node']['loc']['location']
                country = result['data'][hotel]['hotel_data_node']['loc']['country']
                pin = result['data'][hotel]['hotel_data_node']['loc']['pin']
                image = result['data'][hotel]['hotel_data_node']['img_selected']['g']['l']
                response1 = """Hotel Name - {} \nProperty Type - {} \nNumber of Rooms - {} \nFacilities - {} \nHotel Rating - {} \nAddress - {},{},{},{},{},{} - {} \nImage - \n{} \n\n""".format(name, property_type, no_of_rooms, ', '.join(facilities), hrating, address, location, city, state, country, city, pin, image)        	
                response += response1	
                limit += 1
                if(limit == 10):
                    break	
        elif result["response_code"] == 405 :
            response = """Internet Problem!"""
        else:
            response = """Record is not found for given request"""
        dispatcher.utter_message(response)
        return [SlotSet('city',city)]
