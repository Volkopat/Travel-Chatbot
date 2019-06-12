
## Generated Story Flight1
* greet
    - utter_greet
* enquire_flight_details
    - action_flight_search
    - form{"name": "action_flight_search"}
    - slot{"requested_slot": "source_airport"}
* form: inform_source_airport{"city": "Bangalore"}
    - slot{"city": "Bangalore"}
    - form: action_flight_search
    - slot{"source_airport": "Bangalore"}
    - slot{"requested_slot": "destination_airport"}
* form: inform_destination_airport{"city": "Melbourne"}
    - slot{"city": "Melbourne"}
    - form: action_flight_search
    - slot{"destination_airport": "Melbourne"}
    - slot{"requested_slot": "flight_date"}
* form: inform_flight_date{"flight_date": "20190320"}
    - slot{"flight_date": "20190320"}
    - form: action_flight_search
    - slot{"flight_date": "20190320"}
    - slot{"requested_slot": "seating_class"}
* form: inform_seating_class{"seating_class": "E"}
    - slot{"seating_class": "E"}
    - form: action_flight_search
    - slot{"seating_class": "E"}
    - slot{"requested_slot": "no_of_adults"}
* form: inform_no_of_adults{"no_of_people": "4"}
    - form: action_flight_search
    - slot{"no_of_adults": "4"}
    - slot{"requested_slot": "no_of_children"}
* form: inform_no_of_children{"no_of_people": "0"}
    - form: action_flight_search
    - slot{"no_of_children": "0"}
    - slot{"requested_slot": "no_of_infants"}
* form: inform_no_of_infants{"no_of_people": "2"}
    - form: action_flight_search
    - slot{"no_of_infants": "2"}
    - slot{"source_airport": "Bangalore"}
    - slot{"destination_airport": "Melbourne"}
    - slot{"flight_date": "20190320"}
    - slot{"seating_class": "E"}
    - slot{"no_of_adults": "4"}
    - slot{"no_of_children": "0"}
    - slot{"no_of_infants": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Flight2
* greet
    - utter_greet
* enquire_flight_details
    - action_flight_search
    - form{"name": "action_flight_search"}
    - slot{"requested_slot": "source_airport"}
* form: inform_city{"city": "Chennai"}
    - slot{"city": "Chennai"}
    - form: action_flight_search
    - slot{"source_airport": "Chennai"}
    - slot{"requested_slot": "destination_airport"}
* form: inform_destination_airport{"city": "Lucknow"}
    - slot{"city": "Lucknow"}
    - form: action_flight_search
    - slot{"destination_airport": "Lucknow"}
    - slot{"requested_slot": "flight_date"}
* form: inform_flight_date{"flight_date": "20190325"}
    - slot{"flight_date": "20190325"}
    - form: action_flight_search
    - slot{"flight_date": "20190325"}
    - slot{"requested_slot": "seating_class"}
* form: inform_seating_class{"seating_class": "B"}
    - slot{"seating_class": "B"}
    - form: action_flight_search
    - slot{"seating_class": "E"}
    - slot{"requested_slot": "no_of_adults"}
* form: inform_no_of_adults{"no_of_people": "2"}
    - form: action_flight_search
    - slot{"no_of_adults": "2"}
    - slot{"requested_slot": "no_of_children"}
* form: inform_no_of_children{"no_of_people": "0"}
    - form: action_flight_search
    - slot{"no_of_children": "0"}
    - slot{"requested_slot": "no_of_infants"}
* form: inform_no_of_infants{"no_of_people": "Zero"}
    - form: action_flight_search
    - slot{"no_of_infants": null}
    - slot{"requested_slot": "no_of_infants"}
* form: inform_no_of_infants{"no_of_people": "0"}
    - form: action_flight_search
    - slot{"no_of_infants": "0"}
    - slot{"source_airport": "Chennai"}
    - slot{"destination_airport": "Lucknow"}
    - slot{"flight_date": "20190325"}
    - slot{"seating_class": "E"}
    - slot{"no_of_adults": "2"}
    - slot{"no_of_children": "0"}
    - slot{"no_of_infants": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Flight3
* enquire_flight_details
    - action_flight_search
    - form{"name": "action_flight_search"}
    - slot{"requested_slot": "source_airport"}
* form: inform_source_airport{"city": "Berlin"}
    - slot{"city": "Berlin"}
    - form: action_flight_search
    - slot{"source_airport": "Berlin"}
    - slot{"requested_slot": "destination_airport"}
* form: inform_destination_airport{"city": "London"}
    - slot{"city": "London"}
    - form: action_flight_search
    - slot{"destination_airport": "London"}
    - slot{"requested_slot": "flight_date"}
* form: inform_flight_date{"flight_date": "20190327"}
    - slot{"flight_date": "20190327"}
    - form: action_flight_search
    - slot{"flight_date": "20190327"}
    - slot{"requested_slot": "seating_class"}
* form: inform_seating_class{"seating_class": "B"}
    - slot{"seating_class": "B"}
    - form: action_flight_search
    - slot{"seating_class": "E"}
    - slot{"requested_slot": "no_of_adults"}
* form: inform_no_of_adults{"no_of_people": "1"}
    - form: action_flight_search
    - slot{"no_of_adults": "1"}
    - slot{"requested_slot": "no_of_children"}
* form: inform_no_of_children{"no_of_people": "0"}
    - form: action_flight_search
    - slot{"no_of_children": "0"}
    - slot{"requested_slot": "no_of_infants"}
* form: inform_no_of_infants{"no_of_people": "0"}
    - form: action_flight_search
    - slot{"no_of_infants": "0"}
    - slot{"source_airport": "Berlin"}
    - slot{"destination_airport": "London"}
    - slot{"flight_date": "20190327"}
    - slot{"seating_class": "E"}
    - slot{"no_of_adults": "1"}
    - slot{"no_of_children": "0"}
    - slot{"no_of_infants": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Flight4
* greet
    - utter_greet
* enquire_flight_details
    - action_flight_search
    - form{"name": "action_flight_search"}
    - slot{"requested_slot": "source_airport"}
* form: inform_source_airport{"city": "Amsterdam"}
    - slot{"city": "Amsterdam"}
    - form: action_flight_search
    - slot{"source_airport": "Amsterdam"}
    - slot{"requested_slot": "destination_airport"}
* form: inform_destination_airport{"city": "Barcelona"}
    - slot{"city": "Barcelona"}
    - form: action_flight_search
    - slot{"destination_airport": "Barcelona"}
    - slot{"requested_slot": "flight_date"}
* form: inform_train_date{"flight_date": "20190401"}
    - slot{"flight_date": "20190401"}
    - form: action_flight_search
    - slot{"flight_date": "20190401"}
    - slot{"requested_slot": "seating_class"}
* form: inform_seating_class{"seating_class": "Business"}
    - slot{"seating_class": "Business"}
    - form: action_flight_search
    - slot{"seating_class": "B"}
    - slot{"requested_slot": "no_of_adults"}
* form: inform_no_of_adults{"no_of_people": "6"}
    - form: action_flight_search
    - slot{"no_of_adults": "6"}
    - slot{"requested_slot": "no_of_children"}
* form: inform_no_of_children{"no_of_people": "3"}
    - form: action_flight_search
    - slot{"no_of_children": "3"}
    - slot{"requested_slot": "no_of_infants"}
* form: inform_no_of_infants{"no_of_people": "0"}
    - form: action_flight_search
    - slot{"no_of_infants": "0"}
    - slot{"source_airport": "Amsterdam"}
    - slot{"destination_airport": "Barcelona"}
    - slot{"flight_date": "20190401"}
    - slot{"seating_class": "B"}
    - slot{"no_of_adults": "6"}
    - slot{"no_of_children": "3"}
    - slot{"no_of_infants": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Flight5
* enquire_flight_details
    - action_flight_search
    - form{"name": "action_flight_search"}
    - slot{"requested_slot": "source_airport"}
* form: inform_city{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - form: action_flight_search
    - slot{"source_airport": "Nagpur"}
    - slot{"requested_slot": "destination_airport"}
* form: inform_city{"city": "Gurgaon"}
    - slot{"city": "Gurgaon"}
    - form: action_flight_search
    - slot{"destination_airport": null}
    - slot{"requested_slot": "destination_airport"}
* form: inform_destination_airport{"city": "Patna"}
    - slot{"city": "Patna"}
    - form: action_flight_search
    - slot{"destination_airport": "Patna"}
    - slot{"requested_slot": "flight_date"}
* form: inform_flight_date{"flight_date": "20190405"}
    - slot{"flight_date": "20190405"}
    - form: action_flight_search
    - slot{"flight_date": "20190405"}
    - slot{"requested_slot": "seating_class"}
* form: inform_seating_class{"seating_class": "E"}
    - slot{"seating_class": "E"}
    - form: action_flight_search
    - slot{"seating_class": "E"}
    - slot{"requested_slot": "no_of_adults"}
* form: inform_no_of_adults{"no_of_people": "3"}
    - form: action_flight_search
    - slot{"no_of_adults": "3"}
    - slot{"requested_slot": "no_of_children"}
* form: inform_no_of_children{"no_of_people": "3"}
    - form: action_flight_search
    - slot{"no_of_children": "3"}
    - slot{"requested_slot": "no_of_infants"}
* form: inform_no_of_infants{"no_of_people": "0"}
    - form: action_flight_search
    - slot{"no_of_infants": "0"}
    - slot{"source_airport": "Nagpur"}
    - slot{"destination_airport": "Patna"}
    - slot{"flight_date": "20190405"}
    - slot{"seating_class": "E"}
    - slot{"no_of_adults": "3"}
    - slot{"no_of_children": "3"}
    - slot{"no_of_infants": "0"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Between1
* greet
    - utter_greet
* enquire_train_station
    - action_trains_station
    - form{"name": "action_trains_station"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "Bangalore city jn"}
    - form: action_trains_station
    - slot{"source_station_name": "Bangalore city jn"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "Hosur"}
    - form: action_trains_station
    - slot{"destination_station_name": "Hosur"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "21-03-2019"}
    - slot{"train_date": "21-03-2019"}
    - form: action_trains_station
    - slot{"train_date": "21-03-2019"}
    - slot{"source_station_name": "KSR BENGALURU"}
    - slot{"destination_station_name": "CARMELARAM"}
    - slot{"train_date": "21-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Between2
* enquire_train_station
    - action_trains_station
    - form{"name": "action_trains_station"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "Jolarpettai"}
    - form: action_trains_station
    - slot{"source_station_name": "Jolarpettai"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "Chennai Central"}
    - form: action_trains_station
    - slot{"destination_station_name": "Chennai Central"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "22-03-2019"}
    - slot{"train_date": "22-03-2019"}
    - form: action_trains_station
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Between3
* greet
    - utter_greet
* enquire_train_station
    - action_trains_station
    - form{"name": "action_trains_station"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "Miraj Jn"}
    - form: action_trains_station
    - slot{"source_station_name": "Miraj Jn"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "Belgaum"}
    - form: action_trains_station
    - slot{"destination_station_name": "Belgaum"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "29-03-2019"}
    - slot{"train_date": "29-03-2019"}
    - form: action_trains_station
    - slot{"train_date": "29-03-2019"}
    - slot{"source_station_name": "MIRAJ JN"}
    - slot{"destination_station_name": "BELGAUM"}
    - slot{"train_date": "29-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Between4
* enquire_train_station
    - action_trains_station
    - form{"name": "action_trains_station"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "Lonavala"}
    - form: action_trains_station
    - slot{"source_station_name": "Lonavala"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "Nanded"}
    - form: action_trains_station
    - slot{"destination_station_name": null}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "Andheri"}
    - form: action_trains_station
    - slot{"destination_station_name": "Andheri"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "01-04-2019"}
    - slot{"train_date": "01-04-2019"}
    - form: action_trains_station
    - slot{"train_date": "01-04-2019"}
    - slot{"source_station_name": "VISAPUR"}
    - slot{"destination_station_name": "BELAPUR"}
    - slot{"train_date": "01-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Live1
* greet
    - utter_greet
* enquire_live_status
    - action_trains_live
    - form{"name": "action_trains_live"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "16590"}
    - slot{"train_number": "16590"}
    - form: action_trains_live
    - slot{"train_number": "16590"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "21-03-2019"}
    - slot{"train_date": "21-03-2019"}
    - form: action_trains_live
    - slot{"train_date": "21-03-2019"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "BANGALORE CITY JN"}
    - form: action_trains_live
    - slot{"source_station_name": "BANGALORE CITY JN"}
    - slot{"train_number": "16590"}
    - slot{"train_date": "21-03-2019"}
    - slot{"source_station_name": "BANGALORE CITY JN"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Live2
* enquire_live_status
    - action_trains_live
    - form{"name": "action_trains_live"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "22626"}
    - slot{"train_number": "22626"}
    - form: action_trains_live
    - slot{"train_number": "22626"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "30-03-2019"}
    - slot{"train_date": "30-03-2019"}
    - form: action_trains_live
    - slot{"train_date": "30-03-2019"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "CHENNAI CENTRAL"}
    - form: action_trains_live
    - slot{"source_station_name": "CHENNAI CENTRAL"}
    - slot{"train_number": "22626"}
    - slot{"train_date": "30-03-2019"}
    - slot{"source_station_name": "CHENNAI CENTRAL"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Live3
* greet
    - utter_greet
* enquire_live_status
    - action_trains_live
    - form{"name": "action_trains_live"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "22221"}
    - slot{"train_number": "22221"}
    - form: action_trains_live
    - slot{"train_number": "22221"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "01-04-2019"}
    - slot{"train_date": "01-04-2019"}
    - form: action_trains_live
    - slot{"train_date": "01-04-2019"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "MUMBAI CST"}
    - form: action_trains_live
    - slot{"source_station_name": "MUMBAI CST"}
    - slot{"train_number": "22221"}
    - slot{"train_date": "01-04-2019"}
    - slot{"source_station_name": "MUMBAI CST"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Live4
* enquire_live_status
    - action_trains_live
    - form{"name": "action_trains_live"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "22691"}
    - slot{"train_number": "22691"}
    - form: action_trains_live
    - slot{"train_number": "22691"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "04-04-2019"}
    - slot{"train_date": "04-04-2019"}
    - form: action_trains_live
    - slot{"train_date": "04-04-2019"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "DELHI H NIZAMUDDIN"}
    - form: action_trains_live
    - slot{"source_station_name": "DELHI H NIZAMUDDIN"}
    - slot{"train_number": "22691"}
    - slot{"train_date": "04-04-2019"}
    - slot{"source_station_name": "DELHI H NIZAMUDDIN"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart


## Generated Story Cancel1
* greet
    - utter_greet
* enquire_train_cancel
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "22-03-2019"}
    - slot{"train_date": "22-03-2019"}
    - form: action_trains_cancel
    - slot{"train_date": "22-03-2019"}
    - slot{"train_date": "22-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}   
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Cancel2
* enquire_train_cancel
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "24-03-2019"}
    - slot{"train_date": "24-03-2019"}
    - form: action_trains_cancel
    - slot{"train_date": "24-03-2019"}
    - slot{"train_date": "24-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}   
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Cancel3
* greet
    - utter_greet
* enquire_train_cancel
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "25-03-2019"}
    - slot{"train_date": "25-03-2019"}
    - form: action_trains_cancel
    - slot{"train_date": "25-03-2019"}
    - slot{"train_date": "25-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}  
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Cancel4
* enquire_train_cancel
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "23-03-2019"}
    - slot{"train_date": "23-03-2019"}
    - form: action_trains_cancel
    - slot{"train_date": "23-03-2019"}
    - slot{"train_date": "23-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}  
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Cancel5
* greet
    - utter_greet
* enquire_train_cancel{"train_date": "04-04-2019"}
    - slot{"train_date": "04-04-2019"}
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"train_date": "04-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Cancel6
* enquire_train_cancel{"train_date": "04-04-2019"}
    - slot{"train_date": "04-04-2019"}
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"train_date": "04-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Cancel7
* greet
    - utter_greet
* enquire_train_cancel{"train_date": "04-04-2019"}
    - slot{"train_date": "04-04-2019"}
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"train_date": "04-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Cancel8
* enquire_train_cancel{"train_date": "03-04-2019"}
    - slot{"train_date": "03-04-2019"}
    - action_trains_cancel
    - form{"name": "action_trains_cancel"}
    - slot{"train_date": "03-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Reschedule1
* greet
    - utter_greet
* enquire_train_reschedule
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "26-03-2019"}
    - slot{"train_date": "26-03-2019"}
    - form: action_trains_reschedule
    - slot{"train_date": "26-03-2019"}
    - slot{"train_date": "26-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null} 
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Reschedule2
* enquire_train_reschedule
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "27-03-2019"}
    - slot{"train_date": "27-03-2019"}
    - form: action_trains_reschedule
    - slot{"train_date": "27-03-2019"}
    - slot{"train_date": "27-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}  
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Reschedule3
* greet
    - utter_greet
* enquire_train_reschedule
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "28-03-2019"}
    - slot{"train_date": "28-03-2019"}
    - form: action_trains_reschedule
    - slot{"train_date": "28-03-2019"}
    - slot{"train_date": "28-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}   
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Reschedule4
* enquire_train_reschedule
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "29-03-2019"}
    - slot{"train_date": "29-03-2019"}
    - form: action_trains_reschedule
    - slot{"train_date": "29-03-2019"}
    - slot{"train_date": "29-03-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Reschedule5
* greet
    - utter_greet
* enquire_train_reschedule{"train_date": "02-04-2019"}
    - slot{"train_date": "02-04-2019"}
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"train_date": "02-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Reschedule6
* enquire_train_reschedule{"train_date": "02-04-2019"}
    - slot{"train_date": "02-04-2019"}
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"train_date": "02-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Reschedule7
* greet
    - utter_greet
* enquire_train_reschedule{"train_date": "02-04-2019"}
    - slot{"train_date": "02-04-2019"}
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"train_date": "02-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Reschedule8
* enquire_train_reschedule{"train_date": "01-04-2019"}
    - slot{"train_date": "01-04-2019"}
    - action_trains_reschedule
    - form{"name": "action_trains_reschedule"}
    - slot{"train_date": "01-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots 
    - action_chat_restart 

## Generated Story StationCode1
* greet
    - utter_greet
* enquire_train_station_code
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form: action_trains_station_code
    - slot{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset    
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story StationCode2
* enquire_train_station_code
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form: action_trains_station_code
    - slot{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset    
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story StationCode3
* greet
    - utter_greet
* enquire_train_station_code
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form: action_trains_station_code
    - slot{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset    
    - reset_slots  
    - action_chat_restart

## Generated Story StationCode4
* enquire_train_station_code
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form: action_trains_station_code
    - slot{"city": "Belgaum"}
    - slot{"city": "Belgaum"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset    
    - reset_slots  
    - action_chat_restart

## Generated Story StationCode5
* greet
    - utter_greet
* enquire_train_station_code{"city": "Delhi"}
    - slot{"city": "Delhi"}
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"city": "Delhi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story StationCode6
* enquire_train_station_code{"city": "Kolkata"}
    - slot{"city": "Kolkata"}
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"city": "Kolkata"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story StationCode7
* greet
    - utter_greet
* enquire_train_station_code{"city": "Delhi"}
    - slot{"city": "Delhi"}
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"city": "Delhi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story StationCode8
* enquire_train_station_code{"city": "Hyderabad"}
    - slot{"city": "Hyderabad"}
    - action_trains_station_code
    - form{"name": "action_trains_station_code"}
    - slot{"city": "Hyderabad"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story StationName1
* greet
    - utter_greet
* enquire_train_station_name
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"requested_slot": "station_code"}
* form: inform_station_code{"station_code": "HWH"}
    - slot{"station_code": "HWH"}
    - form: action_trains_station_name
    - slot{"station_code": "HWH"}
    - slot{"station_code": "HWH"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story StationName2
* enquire_train_station_name
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"requested_slot": "station_code"}
* form: inform_station_code{"station_code": "TKD"}
    - slot{"station_code": "TKD"}
    - form: action_trains_station_name
    - slot{"station_code": "TKD"}
    - slot{"station_code": "TKD"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story StationName3
* greet
    - utter_greet
* enquire_train_station_name
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"requested_slot": "station_code"}
* form: inform_station_code{"station_code": "TKD"}
    - slot{"station_code": "TKD"}
    - form: action_trains_station_name
    - slot{"station_code": "TKD"}
    - slot{"station_code": "TKD"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story StationName4
* enquire_train_station_name
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"requested_slot": "station_code"}
* form: inform_station_code{"station_code": "MWM"}
    - slot{"station_code": "MWM"}
    - form: action_trains_station_name
    - slot{"station_code": "MWM"}
    - slot{"station_code": "MWM"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story StationName5
* greet
    - utter_greet
* enquire_train_station_name{"station_code": "YPR"}
    - slot{"station_code": "YPR"}
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"station_code": "YPR"}
    - slot{"station_code": "YPR"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story StationName6
* greet
    - utter_greet
* enquire_train_station_name{"station_code": "YPR"}
    - slot{"station_code": "YPR"}
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"station_code": "YPR"}
    - slot{"station_code": "YPR"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story StationName7
* enquire_train_station_name{"station_code": "YPR"}
    - slot{"station_code": "YPR"}
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"station_code": "YPR"}
    - slot{"station_code": "YPR"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart


## Generated Story StationName8
* enquire_train_station_name{"station_code": "BYPL"}
    - slot{"station_code": "BYPL"}
    - action_trains_station_name
    - form{"name": "action_trains_station_name"}
    - slot{"station_code": "BYPL"}
    - slot{"station_code": "BYPL"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart


## Generated Story Fare1
* greet
    - utter_greet
* enquire_train_fare
    - action_trains_fare
    - form{"name": "action_trains_fare"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "16589"}
    - slot{"train_number": "16589"}
    - form: action_trains_fare
    - slot{"train_number": "16589"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "BELGAUM"}
    - form: action_trains_fare
    - slot{"source_station_name": "BELGAUM"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "MIRAJ JN"}
    - form: action_trains_fare
    - slot{"destination_station_name": "MIRAJ JN"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "04-04-2019"}
    - slot{"train_date": "04-04-2019"}
    - form: action_trains_fare
    - slot{"train_date": "04-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "SL"}
    - slot{"class_code": "SL"}
    - form: action_trains_fare
    - slot{"class_code": "SL"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "GN"}
    - slot{"quota_code": "GN"}
    - form: action_trains_fare
    - slot{"quota_code": "GN"}
    - slot{"requested_slot": "age"}
* form: inform_age{"age": "22"}
    - slot{"age": "22"}
    - form: action_trains_fare
    - slot{"age": "22"}
    - slot{"train_number": "16589"}
    - slot{"source_station_name": "BELGAUM"}
    - slot{"destination_station_name": "MIRAJ JN"}
    - slot{"class_code": "SL"}
    - slot{"quota_code": "GN"}
    - slot{"train_date": "04-04-2019"}
    - slot{"age": "22"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Fare2
* enquire_train_fare
    - action_trains_fare
    - form{"name": "action_trains_fare"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "22691"}
    - slot{"train_number": "22691"}
    - form: action_trains_fare
    - slot{"train_number": "22691"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "BALHARSHAH"}
    - form: action_trains_fare
    - slot{"source_station_name": "BALHARSHAH"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "NAGPUR"}
    - form: action_trains_fare
    - slot{"destination_station_name": "NAGPUR"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "07-04-2019"}
    - slot{"train_date": "07-04-2019"}
    - form: action_trains_fare
    - slot{"train_date": "07-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "3A"}
    - slot{"class_code": "3A"}
    - form: action_trains_fare
    - slot{"class_code": "3A"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "TQ"}
    - slot{"quota_code": "TQ"}
    - form: action_trains_fare
    - slot{"quota_code": "TQ"}
    - slot{"requested_slot": "age"}
* form: inform_age{"age": "22"}
    - slot{"age": "22"}
    - form: action_trains_fare
    - slot{"age": "22"}
    - slot{"train_number": "22691"}
    - slot{"source_station_name": "BALHARSHAH"}
    - slot{"destination_station_name": "NAGPUR"}
    - slot{"class_code": "3A"}
    - slot{"quota_code": "TQ"}
    - slot{"train_date": "07-04-2019"}
    - slot{"age": "22"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Fare3
* greet
    - utter_greet
* enquire_train_fare
    - action_trains_fare
    - form{"name": "action_trains_fare"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "22691"}
    - slot{"train_number": "22691"}
    - form: action_trains_fare
    - slot{"train_number": "22691"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "BALHARSHAH"}
    - form: action_trains_fare
    - slot{"source_station_name": "BALHARSHAH"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "NAGPUR"}
    - form: action_trains_fare
    - slot{"destination_station_name": "NAGPUR"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "07-04-2019"}
    - slot{"train_date": "07-04-2019"}
    - form: action_trains_fare
    - slot{"train_date": "07-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "3A"}
    - slot{"class_code": "3A"}
    - form: action_trains_fare
    - slot{"class_code": "3A"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "TQ"}
    - slot{"quota_code": "TQ"}
    - form: action_trains_fare
    - slot{"quota_code": "TQ"}
    - slot{"requested_slot": "age"}
* form: inform_age{"age": "22"}
    - slot{"age": "22"}
    - form: action_trains_fare
    - slot{"age": "22"}
    - slot{"train_number": "22691"}
    - slot{"source_station_name": "BALHARSHAH"}
    - slot{"destination_station_name": "NAGPUR"}
    - slot{"class_code": "3A"}
    - slot{"quota_code": "TQ"}
    - slot{"train_date": "07-04-2019"}
    - slot{"age": "22"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Fare4
* enquire_train_fare
    - action_trains_fare
    - form{"name": "action_trains_fare"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "22691"}
    - slot{"train_number": "22691"}
    - form: action_trains_fare
    - slot{"train_number": "22691"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "BALHARSHAH"}
    - form: action_trains_fare
    - slot{"source_station_name": "BALHARSHAH"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "NAGPUR"}
    - form: action_trains_fare
    - slot{"destination_station_name": "NAGPUR"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "07-04-2019"}
    - slot{"train_date": "07-04-2019"}
    - form: action_trains_fare
    - slot{"train_date": "07-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "3A"}
    - slot{"class_code": "3A"}
    - form: action_trains_fare
    - slot{"class_code": "3A"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "TQ"}
    - slot{"quota_code": "TQ"}
    - form: action_trains_fare
    - slot{"quota_code": "TQ"}
    - slot{"requested_slot": "age"}
* form: inform_age{"age": "22"}
    - slot{"age": "22"}
    - form: action_trains_fare
    - slot{"age": "22"}
    - slot{"train_number": "22691"}
    - slot{"source_station_name": "BALHARSHAH"}
    - slot{"destination_station_name": "NAGPUR"}
    - slot{"class_code": "3A"}
    - slot{"quota_code": "TQ"}
    - slot{"train_date": "07-04-2019"}
    - slot{"age": "22"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart


## Generated Story Seat1
* greet
    - utter_greet
* enquire_train_seat
    - action_trains_seat
    - form{"name": "action_trains_seat"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "22626"}
    - slot{"train_number": "22626"}
    - form: action_trains_seat
    - slot{"train_number": "22626"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "KRISHNARAJAPURAM"}
    - form: action_trains_seat
    - slot{"source_station_name": "KRISHNARAJAPURAM"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "KATPADI JN"}
    - form: action_trains_seat
    - slot{"destination_station_name": "KATPADI JN"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "02-04-2019"}
    - slot{"train_date": "02-04-2019"}
    - form: action_trains_seat
    - slot{"train_date": "02-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "CC"}
    - slot{"class_code": "CC"}
    - form: action_trains_seat
    - slot{"class_code": "CC"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "GN"}
    - slot{"quota_code": "GN"}
    - form: action_trains_seat
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart


## Generated Story Seat2
* greet
    - utter_greet
* enquire_train_seat
    - action_trains_seat
    - form{"name": "action_trains_seat"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "12138"}
    - slot{"train_number": "12138"}
    - form: action_trains_seat
    - slot{"train_number": "12138"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "NEW DELHI"}
    - form: action_trains_seat
    - slot{"source_station_name": "NEW DELHI"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "MUMBAI CST"}
    - form: action_trains_seat
    - slot{"destination_station_name": "MUMBAI CST"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "10-04-2019"}
    - slot{"train_date": "10-04-2019"}
    - form: action_trains_seat
    - slot{"train_date": "10-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "2A"}
    - slot{"class_code": "2A"}
    - form: action_trains_seat
    - slot{"class_code": "2A"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "GN"}
    - slot{"quota_code": "GN"}
    - form: action_trains_seat
    - slot{"quota_code": "GN"}
    - slot{"train_number": "12138"}
    - slot{"source_station_name": "NEW DELHI"}
    - slot{"destination_station_name": "C SHIVAJI MAHARAJ T"}
    - slot{"class_code": "2A"}
    - slot{"quota_code": "GN"}
    - slot{"train_date": "10-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Seat3
* enquire_train_seat
    - action_trains_seat
    - form{"name": "action_trains_seat"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "16573"}
    - slot{"train_number": "16573"}
    - form: action_trains_seat
    - slot{"train_number": "16573"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "YESVANTPUR JN"}
    - form: action_trains_seat
    - slot{"source_station_name": "YESVANTPUR JN"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "PUDUCHERRY"}
    - form: action_trains_seat
    - slot{"destination_station_name": "PUDUCHERRY"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "26-04-2019"}
    - slot{"train_date": "26-04-2019"}
    - form: action_trains_seat
    - slot{"train_date": "26-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "SL"}
    - slot{"class_code": "SL"}
    - form: action_trains_seat
    - slot{"class_code": "SL"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "GN"}
    - slot{"quota_code": "GN"}
    - form: action_trains_seat
    - slot{"quota_code": "GN"}
    - slot{"train_number": "16573"}
    - slot{"source_station_name": "YASVANTPUR JN"}
    - slot{"destination_station_name": "PONDICHERRY"}
    - slot{"class_code": "SL"}
    - slot{"quota_code": "GN"}
    - slot{"train_date": "26-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Seat4
* enquire_train_seat
    - action_trains_seat
    - form{"name": "action_trains_seat"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "16573"}
    - slot{"train_number": "16573"}
    - form: action_trains_seat
    - slot{"train_number": "16573"}
    - slot{"requested_slot": "source_station_name"}
* form: inform_source_station_name{"station_name": "YESVANTPUR JN"}
    - form: action_trains_seat
    - slot{"source_station_name": "YESVANTPUR JN"}
    - slot{"requested_slot": "destination_station_name"}
* form: inform_destination_station_name{"station_name": "PUDUCHERRY"}
    - form: action_trains_seat
    - slot{"destination_station_name": "PUDUCHERRY"}
    - slot{"requested_slot": "train_date"}
* form: inform_train_date{"train_date": "26-04-2019"}
    - slot{"train_date": "26-04-2019"}
    - form: action_trains_seat
    - slot{"train_date": "26-04-2019"}
    - slot{"requested_slot": "class_code"}
* form: inform_class_code{"class_code": "SL"}
    - slot{"class_code": "SL"}
    - form: action_trains_seat
    - slot{"class_code": "SL"}
    - slot{"requested_slot": "quota_code"}
* form: inform_quota_code{"quota_code": "GN"}
    - slot{"quota_code": "GN"}
    - form: action_trains_seat
    - slot{"quota_code": "GN"}
    - slot{"train_number": "16573"}
    - slot{"source_station_name": "YASVANTPUR JN"}
    - slot{"destination_station_name": "PONDICHERRY"}
    - slot{"class_code": "SL"}
    - slot{"quota_code": "GN"}
    - slot{"train_date": "26-04-2019"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story PNR1
* greet
    - utter_greet
* enquire_pnr
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"requested_slot": "pnr_number"}
* form: inform_pnr{"pnr_number": "6527340784"}
    - slot{"pnr_number": "6527340784"}
    - form: action_trains_pnr
    - slot{"pnr_number": "6527340784"}
    - slot{"pnr_number": "6527340784"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story PNR2
* enquire_pnr
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"requested_slot": "pnr_number"}
* inform_pnr{"pnr_number": "2233445566"}
    - slot{"pnr_number": "2233445566"}
    - action_trains_pnr
    - slot{"pnr_number": "2233445566"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story PNR3
* greet
    - utter_greet
* enquire_pnr
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"requested_slot": "pnr_number"}
* inform_pnr{"pnr_number": "1122334455"}
    - slot{"pnr_number": "1122334455"}
    - action_trains_pnr
    - slot{"pnr_number": "1122334455"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story PNR4
* enquire_pnr
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"requested_slot": "pnr_number"}
* inform_pnr{"pnr_number": "0987654321"}
    - slot{"pnr_number": "0987654321"}
    - action_trains_pnr
    - slot{"pnr_number": "0987654321"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story PNR5
* greet
    - utter_greet
* enquire_pnr{"pnr_number": "3344556677"}
    - slot{"pnr_number": "3344556677"}
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"pnr_number": "3344556677"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story PNR6
* enquire_pnr{"pnr_number": "3344556677"}
    - slot{"pnr_number": "3344556677"}
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"pnr_number": "3344556677"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story PNR7
* greet
    - utter_greet
* enquire_pnr{"pnr_number": "3344556677"}
    - slot{"pnr_number": "3344556677"}
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"pnr_number": "3344556677"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
    - action_chat_restart

## Generated Story PNR8
* enquire_pnr{"pnr_number": "3344556677"}
    - slot{"pnr_number": "3344556677"}
    - action_trains_pnr
    - form{"name": "action_trains_pnr"}
    - slot{"pnr_number": "3344556677"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
    - action_chat_restart

## Generated Story TrainClassInfo1
* greet
    - utter_greet
* enquire_trains_class_info
    - action_trains_class_info
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story TrainClassInfo2
* enquire_trains_class_info
    - action_trains_class_info
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story TrainClassInfo3
* greet
    - utter_greet
* enquire_trains_class_info
    - action_trains_class_info
    - action_chat_restart

## Generated Story TrainClassInfo4
* enquire_trains_class_info
    - action_trains_class_info 
    - action_chat_restart


## Generated Story TrainQuotaInfo1
* greet
    - utter_greet
* enquire_train_quota_info
    - action_trains_quota_info
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story TrainQuotaInfo2
* greet
    - utter_greet
* enquire_train_quota_info
    - action_trains_quota_info
    - action_chat_restart

## Generated Story TrainQuotaInfo3
* enquire_train_quota_info
    - action_trains_quota_info
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story TrainQuotaInfo4
* enquire_train_quota_info
    - action_trains_quota_info
    - action_chat_restart


## Generated Story FlightClassInfo1
* greet
    - utter_greet
* enquire_flight_class_info
    - action_flight_class_info
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story FlightClassInfo2
* enquire_flight_class_info
    - action_flight_class_info
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story FlightClassInfo3
* greet
    - utter_greet
* enquire_flight_class_info
    - action_flight_class_info
    - action_chat_restart

## Generated Story FlightClassInfo4
* enquire_flight_class_info
    - action_flight_class_info
    - action_chat_restart


## Generated Story Hotel1
* greet
    - utter_greet
* enquire_hotel_details
    - action_hotels_search
    - form{"name": "action_hotels_search"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Canacona"}
    - slot{"city": "Canacona"}
    - form: action_hotels_search
    - slot{"city": "Canacona"}
    - slot{"city": "Canacona"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Hotel2
* greet
    - utter_greet
* enquire_hotel_details
    - action_hotels_search
    - form{"name": "action_hotels_search"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Pondicherry"}
    - slot{"city": "Pondicherry"}
    - form: action_hotels_search
    - slot{"city": "Pondicherry"}
    - slot{"city": "Pondicherry"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Hotel3
* enquire_hotel_details
    - action_hotels_search
    - form{"name": "action_hotels_search"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Bangalore"}
    - slot{"city": "Bangalore"}
    - form: action_hotels_search
    - slot{"city": "Bangalore"}
    - slot{"city": "Bangalore"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Hotel4
* greet
    - utter_greet
* enquire_hotel_details
    - action_hotels_search
    - form{"name": "action_hotels_search"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Mumbai"}
    - slot{"city": "Mumbai"}
    - form: action_hotels_search
    - slot{"city": "Mumbai"}
    - slot{"city": "Mumbai"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset     
    - reset_slots  
    - action_chat_restart

## Generated Story Hotel5
* enquire_hotel_details
    - action_hotels_search
    - form{"name": "action_hotels_search"}
    - slot{"requested_slot": "city"}
* form: inform_city{"city": "Chennai"}
    - slot{"city": "Chennai"}
    - form: action_hotels_search
    - action_slot_reset    
    - reset_slots  
    - action_chat_restart

## Generated Story Hotel6
* greet
    - utter_greet
* enquire_hotel_details{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - action_hotels_search
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Hotel7
* greet
    - utter_greet
* enquire_hotel_details{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - action_hotels_search
    - action_slot_reset
    - reset_slots
    - action_chat_restart

## Generated Story Hotel8
* enquire_hotel_details{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - action_hotels_search
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Hotel9
* enquire_hotel_details{"city": "Nagpur"}
    - slot{"city": "Nagpur"}
    - action_hotels_search
    - action_slot_reset
    - reset_slots
    - action_chat_restart

## Generated Story Route1
* greet
    - utter_greet
* enquire_train_route
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "18370"}
    - slot{"train_number": "18370"}
    - form: action_trains_route
    - slot{"train_number": "18370"}
    - slot{"train_number": "18370"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Route2
* enquire_train_route
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "12952"}
    - slot{"train_number": "12952"}
    - form: action_trains_route
    - slot{"train_number": "12952"}
    - slot{"train_number": "12952"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
    - action_chat_restart

## Generated Story Route3
* enquire_train_route
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "12951"}
    - slot{"train_number": "12951"}
    - form: action_trains_route
    - slot{"train_number": "12951"}
    - slot{"train_number": "12951"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Route4
* greet
    - utter_greet
* enquire_train_route
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"requested_slot": "train_number"}
* form: inform_train_number{"train_number": "12454"}
    - slot{"train_number": "12454"}
    - form: action_trains_route
    - slot{"train_number": "12454"}
    - slot{"train_number": "12454"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
    - action_chat_restart

## Generated Story Route5
* greet
    - utter_greet
* enquire_train_route{"train_number": "12027"}
    - slot{"train_number": "12027"}
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"train_number": "12027"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Route6
* enquire_train_route{"train_number": "12027"}
    - slot{"train_number": "12027"}
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"train_number": "12027"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
* goodbye
    - utter_goodbye
    - action_chat_restart

## Generated Story Route7
* greet
    - utter_greet
* enquire_train_route{"train_number": "12027"}
    - slot{"train_number": "12027"}
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"train_number": "12027"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
    - action_chat_restart

## Generated Story Route8
* enquire_train_route{"train_number": "12027"}
    - slot{"train_number": "12027"}
    - action_trains_route
    - form{"name": "action_trains_route"}
    - slot{"train_number": "12027"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - reset_slots
    - action_chat_restart


