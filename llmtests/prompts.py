from pathlib import Path


def multiple_choice_picture_simple()->str:
    s = "Hva er det riktige svaret på flervalgsoppgaven? Gi svaret som bokstaven som er rett uten forklaring og uten parentes. Altså er maksimal lengde på svaret 1 bokstav og svaret er blant bokstavene A, B, C og D."
    return s

def multiple_choice_picture_reasoning()->str:
    s = "Lag en json dict med to nøkkelord. 'explanation' som gir en maks 1 setning lang forklaring på hva det riktige svaret på oppgave på bildet er. 'answer' bokstaven som betegner det riktige alternativet, altså MÅ svaret være en av bokstavene A, B C eller D. Svaret skal altså KUN bestå av en json-formatert dict. Dersom noe må formateres i forklaringsstrengen, bruk markdown-formatering og ikke ta med escape-characters som backslash."
    return s

def multiple_choice_picture_reasoning_expert()->str:
    s = "Du skal være en ekspert på kjemi fra videregående skole og kjemi på nivå opp til de første årene av en universitetsutdannelse i kjemi. Hva er det riktige svaret på flervalgsoppgaven? Svaret skal være enten A, B, C eller D. Svaret, sammen med en forklaring på 1 setning, returneres som en json dict med følgende nøkkelord: 'explanation' for forklaringen og nøkkelord 'answer' for svaret. Svaret skal altså KUN bestå av en json-formatert dict"
    return s

def multiple_choice_get_question_keywords():
    txt = Path('stikkord.txt').read_text()
    s = "Lag en json-liste. Bruk listen med stikkord i slutten av denne teksten til å velge ut riktige stikkord som hører sammen med bildet. Returner svaret som en json-liste med stikkordene som verdi. Stikkordene skal være skrevet med små bokstaver og uten mellomrom. Dersom det er flere stikkord, skal de være adskilt med komma. Dersom det er flere ord i et stikkord, skal ordene være adskilt med understrek."
    s += txt
    return s

def multiple_choice_transcription()->str:
    s = "Retun a json dict. Given the photo return the transcription of the multiple choice question in the picture. The transcription should be given as a json dict with the keys 'transcription', 'altA', 'altB', 'altC', 'altD', 'picture_required'. The value of 'transcription' should be the transcription of the text in the photo excluding the alternatives. The values of 'altA', 'altB', 'altC', 'altD' should be the transcription of the alternatives. The value of 'picture_required' should be True if the task is impossible with just the text from the alternatives and False if the task is possible to solve with just the transcription. The language of text in the picture is Norwegian." 
    return s