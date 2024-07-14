from random import choice

from .coureurs_texts import SprintEndText
from .time_handler import *

class Course:
    def __init__(self, participants, is_on=False):
        self.participants = participants
        self.is_on = is_on

    ################# STARTING AND JOINING
    def launch_course(self, arg):
        error_format = "Merci de formater votre message de la façon suivante :\n" \
        "```course à 15 pour 30``` (unités en minutes)"
        error_already_course = "Un marathon d'écriture est déjà en cours !"
        sprint_data = return_delays(arg)
        start_time = sprint_data[2]
        duration = int(sprint_data[1]/60)

        if self.is_on:
            return [0, error_already_course]
        elif sprint_data == False:
            return [0, error_format]
        else:
            self.is_on = True

            if start_time.minute < 10:
                return [1, f"Le marathon commencera à {start_time.hour}h0{start_time.minute} pour {duration} minutes.", duration]
            else:
                return [1, f"Le marathon commencera à {start_time.hour}h{start_time.minute} pour {duration} minutes.", duration]

    def start_course(self, duration):
        if len(self.participants) == 0:
            self.in_on = False
            return [0, choice(SprintEndText.sprint_cancelled)]
        else:
            all_mentions = ", ".join([d.get('name').mention for d in self.participants])

            return [1, f"{all_mentions}\n" + choice(SprintEndText.sprint_start) + f"\n Vous avez {duration} minutes !"]

    def ask_for_wordcount(self):
        all_names = [d.get('name') for d in self.participants]
        mentions = ", ".join([dude.mention for dude in all_names])
        return f"{mentions}\nABOULEZ LES MOTS ! Vous avez deux (2) minutes."

    def finish_course(self):
        finished_list = self.handle_participants()
        self.is_on = False
        self.participants = []

        return "\n:sparkles::sparkles::sparkles: **C'EEEEEEST *FINI***:sparkles::sparkles::sparkles:" + \
            f"\n\n{finished_list}\n\n{choice(SprintEndText.inspiring_quotes)}"

    def participant_is_joining(self, user_data):
        # Expected user_data : {'name': "x", "wordcount": x}
        if not self.is_on:
            return [0, "Aucune course en cours. Tanpis."]
        elif user_data["wordcount"] == ():
            user_data['wordcount'] = 0
            self.give_starting_wordcount(
                user_data['name'], user_data['wordcount']
            )

            return [1, f"{user_data['name'].name} joint avec {user_data['wordcount']} mots."]
        
        elif not user_data['wordcount'][0].isdigit():
                return [0, "Format: ```!cj VOTRE_NOMBRE_DE_MOT```"]
        else:
            user_data['wordcount'] = user_data['wordcount'][0]
            self.give_starting_wordcount(
                user_data['name'], user_data['wordcount']
            )

            return [1, f"{user_data['name'].name} joint avec {user_data['wordcount']} mots."]

    def participant_give_final_wordcount(self, user_data):
        # Expected user_data : {'name': "x", "wordcount": x}
        if not self.is_on:
            return "Aucune course en cours. Tanpis."
        elif not user_data['wordcount'].isdigit():
                return "Format: ```!cm VOTRE_NOMBRE_DE_MOT```"
        else:
            self.give_ending_wordcount(
                user_data['name'], user_data['wordcount']
            )
            return [1, f"{user_data['name'].name}, votre dernier mot : {user_data['wordcount']} mots."]

    ############### Handling wordcounts
    def give_starting_wordcount(self, user_name, wordcount):
        all_names = [d.get('name') for d in self.participants]

        if user_name not in all_names:
            self.participants.append({'name': user_name, "starting_wordcount": wordcount, "ending_wordcount": 0})
        else:
            for p in self.participants:
                if p['name'] == user_name:
                    p["starting_wordcount"] = wordcount

    def give_ending_wordcount(self, user_name, wordcount):
        all_names = [d.get('name') for d in self.participants]

        if user_name not in all_names:
            self.participants.append({'name': user_name, "starting_wordcount": wordcount, "ending_wordcount": wordcount})
        else:
            for p in self.participants:
                if p['name'] == user_name:
                    p["ending_wordcount"] = wordcount
        
    def handle_participants(self):
        sorted_participants = self.sort_participants()
        cleaned_users = []

        for user in sorted_participants:
            # LUCILE : le bug est ici
            if user['has_written'] > 0:
                user = f"\n:star2: {user['name'].mention}: {user['final_wordcount']} mots, dont {user['has_written']} nouveaux !"
            elif user['has_written'] == 0:
                user = f"\n:star2: {user['name'].mention} {choice(SprintEndText.zero_words)}"
            else:
                user = f"\n:star2: {user['name'].mention} a effacé {abs(user['has_written'])} mots."
            cleaned_users.append(user)

        if len(sorted_participants) > 1:
            sorted_users_list = "".join(cleaned_users)
        else:
            sorted_users_list = f"{cleaned_users[0]}\n\n{choice(SprintEndText.sprint_alone)}"

        return sorted_users_list

    def sort_participants(self):
        winners_list = []
        
        for p in self.participants:
            result = {
                'name': p['name'],
                'final_wordcount': int(p["ending_wordcount"]),
                'has_written': int(p["ending_wordcount"]) - int(p['starting_wordcount'])
            }
            winners_list.append(result)
        results = sorted(winners_list, key=lambda x: x['has_written'])
        results.reverse()
        
        return results
    
# truc = Course([
#         {'name': "Lucile", "starting_wordcount": 0, "ending_wordcount": 0},
#         {'name': "Jean", "starting_wordcount": 10, "ending_wordcount": -5},
#         {'name': "Bob", "starting_wordcount": 10, "ending_wordcount": 35},
#     ])

# print(truc.launch_course(['à', '24']))
# print(truc.participant_is_joining({'name': 'Lucile', "wordcount":"399"}))
