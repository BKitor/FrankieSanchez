class ServerMetadata():

    emojis = {
        "ANDREW_CONCENTRATE": "<:Andrewsconcentrationface:793306010697334784>",
        "ANDREW_SAD": "<:andrewsad:789514794443997254>",
        "ANDREW_FRANCH": "<:franchandrew:793317464460886048>",
        "ANDREW_HAHA": "<:hahaandrew:793317995245076500>",
        "ANDREW_LONGO": "<:longo:788496351481561088>",

        "JESSICA_23": "<:jessica23:788919518369284107>",

        "DOM_COVERT": "<:covertdom:793334958604550144>",
        "DOM_3D": "<:3Dom:793322401374142494>",
        "DOM_CUTE": "<:cutedomo:793334567012401162>",
        "DOM_S3XY": "<:3_s3xy_5_me:792604221949345802>",
        "DOM_AND_BRODY": "<:domandbrody:788913684067254344>",
        "DOM_DINO": "<:dinodom:788916378739671084>",

        "LINA_STUDY": "<:Study_lina:789512821322022972>",
        "LINA_HAPPY": "<:HappyLina:789513446173179964>",
        "LINA_MUSTACHE": "<:lina_mustache:788500643164717096>",
        "LINA_GRAMMY": "<:grammylina:789160798747492362>",

        "ADRIAN_POWER_TOP": "<:power_top:788505495328784384>",
        "ADRIAN_BLOOD": "<:bloods:788505739777802260>",

        "LYDIA_DORK": "<:dork:788495169493532752>",

        "KITO_CPF": "<:CPF:792604221891149854>",

        "MEL_MEL": "<:mel:789290148642816000>",

        "SALLY_BOTTY_PLANT": "<:booty:788506892011044927>",
    }

    andew_longo_id = "788493761373667430"
    pro_brody_lover_id = "788493329666539550"
    little_smarty_pants_id = "788492323386163261"
    board_game_master_id = "788493669950029887"
    deadlift_daddy_id = "788552797460365312"
    power_dork_id = "788493026485600286"
    kito_hacker_man_id = "788486828986204190"
    sally_damn_id = "788494299612053515"
    hamster_mom_id = "789295205320360006"

    andrew_emojis = {}
    dom_emojis = {}
    jessica_emojis = {}
    lina_emojis = {}
    adrian_emojis = {}
    lydia_emojis = {}
    kito_emojis = {}
    mel_emojis = {}
    sally_emojis = {}

    def get_emojis(self):
        return self.emojis

    def get_andrew_emojis(self):
        if not self.andrew_emojis:
            for k in self.emojis:
                if k.startswith("ANDREW"):
                    self.andrew_emojis[k] = self.emojis[k]

        return self.andrew_emojis

    def get_dom_emojis(self):
        if not self.dom_emojis:
            for k in self.emojis:
                if k.startswith("DOM"):
                    self.dom_emojis[k] = self.emojis[k]

        return self.dom_emojis

    def get_jessica_emojis(self):
        if not self.jessica_emojis:
            for k in self.emojis:
                if k.startswith("JESSICA"):
                    self.jessica_emojis[k] = self.emojis[k]
        return self.jessica_emojis

    def get_lina_emojis(self):
        if not self.lina_emojis:
            for k in self.emojis:
                if k.startswith("LINA"):
                    self.lina_emojis[k] = self.emojis[k]
        return self.lina_emojis

    def get_adrian_emojis(self):
        if not self.adrian_emojis:
            for k in self.emojis:
                if k.startswith("ADRIAN"):
                    self.adrian_emojis[k] = self.emojis[k]

        return self.adrian_emojis

    def get_lydia_emojis(self):
        if not self.lydia_emojis:
            for k in self.emojis:
                if k.startswith("LYDIA"):
                    self.lydia_emojis[k] = self.emojis[k]

        return self.lydia_emojis

    def get_kito_emojis(self):
        if not self.kito_emojis:
            for k in self.emojis:
                if k.startswith("KITO"):
                    self.kito_emojis[k] = self.emojis[k]

        return self.kito_emojis

    def get_mel_emojis(self):
        if not self.mel_emojis:
            for k in self.emojis:
                if k.startswith("MEL"):
                    self.mel_emojis[k] = self.emojis[k]

        return self.mel_emojis

    def get_sally_emojis(self):
        if not self.sally_emojis:
            for k in self.emojis:
                if k.startswith("SALLY"):
                    self.sally_emojis[k] = self.emojis[k]

        return self.sally_emojis
