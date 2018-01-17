answers_dz_c = {"jako dz": 1, "jako c": 2}
answers_ch_c = {"Tak samo": 1, "inaczej": 2}
answers_ll = {"nie słychać": 1, "słychać literę ł": 2,
             "nie jestem pewien/na": 3, "nie jestem pewien": 3}
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# accesing the google sheets API
scope = [ 'https://spreadsheets.google.com/feeds' ]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# sheet's name
sheet_name = "wymowa_reg_worksheet"
sheet = client.open(sheet_name).sheet1
pp = pprint.PrettyPrinter()

# i wanted tuples with the voivodenship (5th col) and answer for the first question (second column)
dz_c = list(zip([item for item in sheet.col_values(2) if item][1:],
                [thing for thing in sheet.col_values(5) if thing][1:]))

dolnośląskie_dz_c = []
kujpom_dz_c = []
lubelskie_dz_c = []
lubuskie_dz_c = []
łódzkie_dz_c = []
małopolskie_dz_c = []
mazowieckie_dz_c = []
opolskie_dz_c = []
podkarpackie_dz_c = []
podlaskie_dz_c = []
pomorskie_dz_c = []
śląskie_dz_c = []
świętokrzyskie_dz_c = []
warmaz_dz_c = []
wielkopolskie_dz_c = []
zachpom_dz_c = []

# w sumie mogłem walnąć dicta xd
# chociaż to jednak lepsze imo
for res in dz_c:
    if res[1][:4].lower() == "doln":
        dolnośląskie_dz_c.append(res)
    elif res[1][:3].lower() == "kuj":
        kujpom_dz_c.append(res)
    elif res[1][:4].lower() == "lube":
        lubelskie_dz_c.append(res)
    elif res[1][:4].lower() == "lubu":
        lubuskie_dz_c.append(res)
    elif res[1][:3].lower() == "łód":
        łódzkie_dz_c.append(res)
    elif res[1][:3].lower() in ["mał", "mal"]:
        małopolskie_dz_c.append(res)
    elif res[1][:3].lower() == "maz":
        mazowieckie_dz_c.append(res)
    elif res[1][:3].lower() == "opo":
        opolskie_dz_c.append(res)
    elif res[1][:4].lower() == "podk":
        podkarpackie_dz_c.append(res)
    elif res[1][:4].lower() == "podl":
        podlaskie_dz_c.append(res)
    elif res[1][:3].lower() == "pom":
        pomorskie_dz_c.append(res)
    elif res[1][:2].lower() in ['śl', 'sl']:
        śląskie_dz_c.append(res)
    elif res[1][:3].lower() in ['świ', 'swi']:
        świętokrzyskie_dz_c.append(res)
    elif res[1][:3].lower() == "war":
        warmaz_dz_c.append(res)
    elif res[1][:3].lower() in ["wie", "wlk"]:
        wielkopolskie_dz_c.append(res)
    else:
        zachpom_dz_c.append(res)

voiv_perc = lambda x, y: [answers_dz_c[item[0].strip()] for item in x].count(y) \
            /len([item[0] for item in x])
# pewnie jest jakiś lepszy sposób niż ten powalony dict
varnames = {tuple(łódzkie_dz_c): "Lódzkie",
            tuple(świętokrzyskie_dz_c): "Swietokrzyskie",
            tuple(wielkopolskie_dz_c): "Wielkopolskie",
            tuple(kujpom_dz_c): "Kujawsko-Pomorskie",
            tuple(małopolskie_dz_c): "Malopolskie",
            tuple(dolnośląskie_dz_c): "Dolnoslaskie",
            tuple(lubelskie_dz_c): "Lubelskie",
            tuple(lubuskie_dz_c): "Lubuskie",
            tuple(mazowieckie_dz_c): "Mazowieckie",
            tuple(opolskie_dz_c): "Opolskie",
            tuple(podlaskie_dz_c): "Podlaskie",
            tuple(pomorskie_dz_c): "Pomorskie",
            tuple(śląskie_dz_c): "Slaskie",
            tuple(podkarpackie_dz_c): "Podkarpackie",
            tuple(warmaz_dz_c): "Warminsko-Mazurskie",
            tuple(zachpom_dz_c): "Zachodniopomorskie"}

voivodenships = [dolnośląskie_dz_c, kujpom_dz_c,
                 lubelskie_dz_c, lubuskie_dz_c,
                 łódzkie_dz_c, małopolskie_dz_c,
                 mazowieckie_dz_c, opolskie_dz_c,
                 podkarpackie_dz_c, podlaskie_dz_c,
                 pomorskie_dz_c, śląskie_dz_c,
                 świętokrzyskie_dz_c, warmaz_dz_c,
                 wielkopolskie_dz_c, zachpom_dz_c]

dict_dz_c = {varnames[tuple(voivodenship)]: voiv_perc(voivodenship, 2)
             for voivodenship in voivodenships}
if __name__ == "__main__":
    pp.pprint(dict_dz_c) 
