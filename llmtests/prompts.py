def multiple_choice_picture_simple()->str:
    s = "Hva er det riktige svaret på flervalgsoppgaven? Gi svaret som bokstaven som er rett uten forklaring og uten parentes. Altså er maksimal lengde på svaret 1 bokstav og svaret er blant bokstavene A, B, C og D."
    return s

def multiple_choice_picture_reasoning()->str:
    s = "Lag en json dict med to nøkkelord. 'explanation' som gir en maks 1 setning lang forklaring på hva det riktige svaret på oppgave på bildet er. 'answer' bokstaven som betegner det riktige alternativet, altså MÅ svaret være en av bokstavene A, B C eller D. Svaret skal altså KUN bestå av en json-formatert dict. Dersom noe må formateres i forklaringsstrengen, bruk markdown-formatering og ikke ta med escape-characters som backslash."
    return s

def multiple_choice_picture_reasoning_expert()->str:
    s = "Du skal være en ekspert på kjemi fra videregående skole og kjemi på nivå opp til de første årene av en universitetsutdannelse i kjemi. Hva er det riktige svaret på flervalgsoppgaven? Svaret skal være enten A, B, C eller D. Svaret, sammen med en forklaring på 1 setning, returneres som en json dict med følgende nøkkelord: 'explanation' for forklaringen og nøkkelord 'answer' for svaret. Svaret skal altså KUN bestå av en json-formatert dict"
    return s

def multiple_choice_get_question_description():
    s = ""
    return s

def multiple_choice_text_simple()->str:
    s = ""
    return s