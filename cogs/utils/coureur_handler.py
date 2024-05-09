class Course:
    def __init__(self):
        participants = []

    def give_starting_wordcount(self, user_name, wordcount):
        all_names = [d.get('name') for d in self.participants]

        if user_name not in all_names:
            self.participants.append({"name": user_name, "starting_wordcount": wordcount, "ending_wordcount": 0})
        else:
            for p in self.participants:
                if p["name"] == user_name:
                    p["starting_wordcount"] = wordcount

    def give_ending_wordcount(self, user_name, wordcount):
        all_names = [d.get('name') for d in self.participants]

        if user_name not in all_names:
            self.participants.append({"name": user_name, "starting_wordcount": wordcount, "ending_wordcount": wordcount})
        else:
            for p in self.participants:
                if p["name"] == user_name:
                    p["ending_wordcount"] = wordcount
        
    # def give_words(user, words):
    #     error_words = "Format: ```!j 1000``̀`̀"
    #     words = 0
    #     # user = ctx.message.author

    #     # LUCILE : if sprint == False, on le laisse même pas accéder au rendu
    #     # if self.sprint == False:
    #         # error_no_sprint = "Aucune course en cours."
    #     #     await ctx.channel.send(error_no_sprint)
    #     if words:
    #         if not words.isdigit():
    #             return [0, error_words]
    #         else:
    #             words = int(words)
    #             self.enders.update({user: words})
    #             await ctx.channel.send(f"{user.name}, votre dernier mot : {words} mots.")