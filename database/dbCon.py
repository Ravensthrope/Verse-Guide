import pymongo

def main():
                                    #add your mongodb server
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["VerseDB"]
    collection1 = db["anger"]
    dictionary1 = [
        {
            "_id": 1, 
            "surah": 3, 
            "ayah": 134, 
            "arabic": "الَّذِیۡنَ یُنۡفِقُوۡنَ فِی السَّرَّآءِ وَ الضَّرَّآءِ وَ الۡکٰظِمِیۡنَ الۡغَیۡظَ وَ الۡعَافِیۡنَ عَنِ النَّاسِ ؕ وَ اللّٰہُ یُحِبُّ الۡمُحۡسِنِیۡنَ ",
            "english": " Who spend [in the cause of Allah ] during ease and hardship and who restrain anger and who pardon the people - and Allah loves the doers of good"
        },
        {
            "_id": 2, 
            "surah": 2, 
            "ayah": 153, 
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ اٰمَنُوا اسۡتَعِیۡنُوۡا بِالصَّبۡرِ وَ الصَّلٰوۃِ  ؕ اِنَّ اللّٰہَ مَعَ الصّٰبِرِیۡنَ ",
            "english": "O you who have believed, seek help through patience and prayer. Indeed, Allah is with the patient."
        },
        {
            "_id": 3, 
            "surah": 2, 
            "ayah": 286, 
            "arabic": "لَا یُکَلِّفُ اللّٰہُ نَفۡسًا اِلَّا وُسۡعَہَا ؕ",
            "english":" Allah does not charge a soul except [with that within] its capacity."
        },
        {
            "_id": 4, 
            "surah": 2, 
            "ayah": 155, 
            "arabic": "وَ لَنَبۡلُوَنَّکُمۡ بِشَیۡءٍ مِّنَ الۡخَوۡفِ وَ الۡجُوۡعِ وَ نَقۡصٍ مِّنَ الۡاَمۡوَالِ وَ الۡاَنۡفُسِ وَ الثَّمَرٰتِ ؕ وَ بَشِّرِ الصّٰبِرِیۡنَ ",
            "english": "And We will surely test you with something of fear and hunger and a loss of wealth and lives and fruits, but give good tidings to the patient."
        },
        {
            "_id": 5, 
            "surah": 16, 
            "ayah": 96, 
            "arabic": "مَا عِنۡدَکُمۡ یَنۡفَدُ وَ مَا عِنۡدَ اللّٰہِ بَاقٍ ؕ وَ لَنَجۡزِیَنَّ الَّذِیۡنَ صَبَرُوۡۤا اَجۡرَہُمۡ بِاَحۡسَنِ مَا  کَانُوۡا یَعۡمَلُوۡنَ ",
            "english": " Whatever you have will end, but what Allah has is lasting. And We will surely give those who were patient their reward according to the best of what they used to do."
        },
        {
            "_id": 6,
            "surah": 9,
            "ayah": 51,
            "arabic": "قُلۡ لَّنۡ یُّصِیۡبَنَاۤ اِلَّا مَا کَتَبَ اللّٰہُ  لَنَا ۚ ہُوَ مَوۡلٰىنَا ۚ وَ عَلَی اللّٰہِ  فَلۡیَتَوَکَّلِ  الۡمُؤۡمِنُوۡنَ ",
            "english": "Say, 'Never will we be struck except by what Allah has decreed for us; He is our protector.' And upon Allah let the believers rely."
        },
        {
            "_id": 7,
            "surah": 42,
            "ayah": 37,
            "arabic": "وَ الَّذِیۡنَ یَجۡتَنِبُوۡنَ کَبٰٓئِرَ الۡاِثۡمِ وَ الۡفَوَاحِشَ وَ اِذَا مَا غَضِبُوۡا ہُمۡ یَغۡفِرُوۡنَ",
            "english": " And those who avoid the major sins and immoralities, and when they are angry, they forgive"
        },
        {
            "_id": 8,
            "surah": 39,
            "ayah": 10,
            "arabic": "قُلۡ یٰعِبَادِ الَّذِیۡنَ اٰمَنُوا اتَّقُوۡا رَبَّکُمۡ ؕ لِلَّذِیۡنَ اَحۡسَنُوۡا فِیۡ ہٰذِہِ  الدُّنۡیَا حَسَنَۃٌ ؕ وَ اَرۡضُ اللّٰہِ  وَاسِعَۃٌ ؕ اِنَّمَا یُوَفَّی الصّٰبِرُوۡنَ  اَجۡرَہُمۡ بِغَیۡرِ حِسَابٍ ",
            "english": "Say, 'O My servants who have believed, fear your Lord. For those who do good in this world is good, and the earth of Allah is spacious. Indeed, the patient will be given their reward without account.'"
        }, 
        {
            "_id": 9,
            "surah": 9,
            "ayah": 15,
            "arabic": "وَ یُذۡہِبۡ غَیۡظَ قُلُوۡبِہِمۡ ؕ وَ یَتُوۡبُ اللّٰہُ عَلٰی مَنۡ  یَّشَآءُ ؕ وَ اللّٰہُ عَلِیۡمٌ  حَکِیۡمٌ",
            "english": "And remove the fury in the believer's hearts. And Allah turns in forgiveness to whom He wills; and Allah is Knowing and Wise."
        },
        {
            "_id": 10,
            "surah": 7,
            "ayah": 199,
            "arabic": "خُذِ الۡعَفۡوَ وَ اۡمُرۡ بِالۡعُرۡفِ وَ اَعۡرِضۡ عَنِ  الۡجٰہِلِیۡنَ",
            "english": "Take what is given freely, enjoin what is good, and turn away from the ignorant."
        },
        {
            "_id": 11,
            "surah": 25,
            "ayah": 63,
            "arabic": "وَ عِبَادُ  الرَّحۡمٰنِ الَّذِیۡنَ  یَمۡشُوۡنَ عَلَی الۡاَرۡضِ ہَوۡنًا وَّ اِذَا خَاطَبَہُمُ الۡجٰہِلُوۡنَ  قَالُوۡا سَلٰمًا",
            "english": "And the servants of the Most Merciful are those who walk upon the earth easily, and when the ignorant address them [harshly], they say [words of] peace"
        },
        {
            "_id": 12,
            "surah": 2,
            "ayah": 263,
            "arabic": "قَوۡلٌ مَّعۡرُوۡفٌ وَّ مَغۡفِرَۃٌ خَیۡرٌ مِّنۡ صَدَقَۃٍ یَّتۡبَعُہَاۤ  اَذًی ؕ وَ اللّٰہُ غَنِیٌّ حَلِیۡمٌ",
            "english": "Kind speech and forgiveness are better than charity followed by injury. And Allah is Free of need and Forbearing."
        },
        {
            "_id": 13,
            "surah": 28,
            "ayah": 54,
            "arabic": "اُولٰٓئِکَ یُؤۡتَوۡنَ اَجۡرَہُمۡ مَّرَّتَیۡنِ بِمَا صَبَرُوۡا وَ یَدۡرَءُوۡنَ بِالۡحَسَنَۃِ  السَّیِّئَۃَ  وَ  مِمَّا  رَزَقۡنٰہُمۡ  یُنۡفِقُوۡنَ",
            "english": "Those will be given their reward twice for what they patiently endured and [because] they avert evil through good, and from what We have provided them they spend."
        },
        {
            "_id": 14,
            "surah": 42,
            "ayah": 40,
            "arabic": "وَ جَزٰٓؤُا سَیِّئَۃٍ  سَیِّئَۃٌ  مِّثۡلُہَا ۚ فَمَنۡ عَفَا وَ اَصۡلَحَ  فَاَجۡرُہٗ  عَلَی اللّٰہِ ؕ اِنَّہٗ  لَا یُحِبُّ الظّٰلِمِیۡنَ",
            "english": "And the retribution for an evil act is an evil one like it, but whoever pardons and makes reconciliation – his reward is [due] from Allah . Indeed, He does not like wrongdoers."
        },
        {
            "_id": 15,
            "surah": 8,
            "ayah": 46,
            "arabic": "اِنَّ  اللّٰہَ  مَعَ  الصّٰبِرِیۡنَ",
            "english": "Indeed, Allah is with the patient."
        },
    ]
    collection1.insert_many(dictionary1)
    # Adding "Disgust" collection in the database
    collection2 = db["disgust"]
    dictionary2 = [
        {
            "_id": 1, 
            "surah": 18, 
            "ayah": 54, 
            "arabic": "وَ لَقَدۡ صَرَّفۡنَا فِیۡ ہٰذَا الۡقُرۡاٰنِ لِلنَّاسِ مِنۡ کُلِّ مَثَلٍ ؕ وَ کَانَ الۡاِنۡسَانُ اَکۡثَرَ  شَیۡءٍ  جَدَلًا ",
            "english": "And We have certainly diversified in this Qur'an for the people from every [kind of] example; but man has ever been, most of anything, [prone to] dispute."
        },
        {
            "_id": 2, 
            "surah": 25, 
            "ayah": 63, 
            "arabic": "وَ عِبَادُ  الرَّحۡمٰنِ الَّذِیۡنَ  یَمۡشُوۡنَ عَلَی الۡاَرۡضِ ہَوۡنًا وَّ اِذَا خَاطَبَہُمُ الۡجٰہِلُوۡنَ  قَالُوۡا سَلٰمًا ",
            "english": "And the servants of the Most Merciful are those who walk upon the earth easily, and when the ignorant address them [harshly], they say [words of] peace"
        },
        {
            "_id": 3, 
            "surah": 2, 
            "ayah": 286, 
            "arabic": "لَا یُکَلِّفُ اللّٰہُ نَفۡسًا اِلَّا وُسۡعَہَا ؕ",
            "english":" Allah does not charge a soul except [with that within] its capacity."
        },
        {
            "_id": 4, 
            "surah": 5, 
            "ayah": 100, 
            "arabic": "قُلۡ لَّا یَسۡتَوِی الۡخَبِیۡثُ وَ الطَّیِّبُ وَ لَوۡ اَعۡجَبَکَ کَثۡرَۃُ الۡخَبِیۡثِ ۚ فَاتَّقُوا اللّٰہَ یٰۤاُولِی الۡاَلۡبَابِ لَعَلَّکُمۡ تُفۡلِحُوۡنَ",
            "english": "Say, 'Not equal are the evil and the good, although the abundance of evil might impress you.' So fear Allah , O you of understanding, that you may be successful."
        },
        {
            "_id": 5, 
            "surah": 39, 
            "ayah": 45, 
            "arabic": "وَ  اِذَا ذُکِرَ اللّٰہُ  وَحۡدَہُ  اشۡمَاَزَّتۡ قُلُوۡبُ الَّذِیۡنَ لَا یُؤۡمِنُوۡنَ بِالۡاٰخِرَۃِ ۚ وَ اِذَا ذُکِرَ الَّذِیۡنَ مِنۡ دُوۡنِہٖۤ  اِذَا ہُمۡ یَسۡتَبۡشِرُوۡنَ",
            "english": "And when Allah is mentioned alone, the hearts of those who do not believe in the Hereafter shrink with aversion, but when those [worshipped] other than Him are mentioned, immediately they rejoice."
        },
        {
            "_id": 6,
            "surah": 49,
            "ayah": 12,
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ  اٰمَنُوا اجۡتَنِبُوۡا کَثِیۡرًا مِّنَ الظَّنِّ ۫ اِنَّ  بَعۡضَ الظَّنِّ   اِثۡمٌ وَّ لَا تَجَسَّسُوۡا وَ لَا یَغۡتَبۡ بَّعۡضُکُمۡ بَعۡضًا ؕ اَیُحِبُّ  اَحَدُکُمۡ  اَنۡ یَّاۡکُلَ  لَحۡمَ اَخِیۡہِ  مَیۡتًا فَـکَرِہۡتُمُوۡہُ ؕ  وَ اتَّقُوا اللّٰہَ ؕ اِنَّ  اللّٰہَ  تَوَّابٌ  رَّحِیۡمٌ",
            "english": "O you who have believed, avoid much [negative] assumption. Indeed, some assumption is sin. And do not spy or backbite each other. Would one of you like to eat the flesh of his brother when dead? You would detest it. And fear Allah ; indeed, Allah is Accepting of repentance and Merciful."
        },
        {
            "_id": 7,
            "surah": 2,
            "ayah": 165,
            "arabic": "وَ مِنَ النَّاسِ مَنۡ یَّتَّخِذُ مِنۡ دُوۡنِ اللّٰہِ اَنۡدَادًا یُّحِبُّوۡنَہُمۡ کَحُبِّ اللّٰہِ ؕ وَ الَّذِیۡنَ اٰمَنُوۡۤا اَشَدُّ حُبًّا  لِّلّٰہِ ؕوَ لَوۡ  یَرَی الَّذِیۡنَ ظَلَمُوۡۤا اِذۡ یَرَوۡنَ الۡعَذَابَ  ۙ اَنَّ الۡقُوَّۃَ لِلّٰہِ جَمِیۡعًا  ۙ وَّ اَنَّ اللّٰہَ شَدِیۡدُ الۡعَذَابِ",
            "english": "And [yet], among the people are those who take other than Allah as equals [to Him]. They love them as they [should] love Allah . But those who believe are stronger in love for Allah . And if only they who have wronged would consider [that] when they see the punishment, [they will be certain] that all power belongs to Allah and that Allah is severe in punishment."
        },
        {
            "_id": 8,
            "surah": 7,
            "ayah": 199,
            "arabic": "خُذِ الۡعَفۡوَ وَ اۡمُرۡ بِالۡعُرۡفِ وَ اَعۡرِضۡ عَنِ  الۡجٰہِلِیۡنَ",
            "english": " Take what is given freely, enjoin what is good, and turn away from the ignorant."
        },
        {
            "_id": 9,
            "surah": 5,
            "ayah": 8,
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ اٰمَنُوۡا کُوۡنُوۡا قَوّٰمِیۡنَ لِلّٰہِ شُہَدَآءَ  بِالۡقِسۡطِ ۫ وَ لَا  یَجۡرِمَنَّکُمۡ شَنَاٰنُ قَوۡمٍ عَلٰۤی اَلَّا تَعۡدِلُوۡا ؕ اِعۡدِلُوۡا ۟ ہُوَ  اَقۡرَبُ لِلتَّقۡوٰی ۫ وَ اتَّقُوا اللّٰہَ ؕ اِنَّ  اللّٰہَ  خَبِیۡرٌۢ  بِمَا تَعۡمَلُوۡنَ",
            "english": "O you who have believed, be persistently standing firm for Allah , witnesses in justice, and do not let the hatred of a people prevent you from being just. Be just; that is nearer to righteousness. And fear Allah ; indeed, Allah is Acquainted with what you do."
        },
        {
            "_id": 10,
            "surah": 41,
            "ayah": 34,
            "arabic": "وَ لَا تَسۡتَوِی الۡحَسَنَۃُ  وَ لَا السَّیِّئَۃُ ؕ اِدۡفَعۡ  بِالَّتِیۡ  ہِیَ  اَحۡسَنُ فَاِذَا الَّذِیۡ بَیۡنَکَ وَ بَیۡنَہٗ  عَدَاوَۃٌ کَاَنَّہٗ  وَلِیٌّ حَمِیۡمٌ",
            "english": "And not equal are the good deed and the bad. Repel [evil] by that [deed] which is better; and thereupon the one whom between you and him is enmity [will become] as though he was a devoted friend."
        },
        {
            "_id": 11,
            "surah": 65,
            "ayah": 4,
            "arabic": " وَ مَنۡ یَّتَّقِ اللّٰہَ  یَجۡعَلۡ لَّہٗ  مِنۡ  اَمۡرِہٖ یُسۡرًا",
            "english": "And whoever fears Allah – He will make for him of his matter ease."
        },
        {
            "_id": 12,
            "surah": 8,
            "ayah": 28,
            "arabic": "وَ اعۡلَمُوۡۤا  اَنَّمَاۤ   اَمۡوَالُکُمۡ  وَ اَوۡلَادُکُمۡ  فِتۡنَۃٌ  ۙ وَّ اَنَّ اللّٰہَ عِنۡدَہٗۤ  اَجۡرٌ  عَظِیۡمٌ",
            "english": "And know that your properties and your children are but a trial and that Allah has with Him a great reward."
        }
    ]
    collection2.insert_many(dictionary2)
    # Adding "Fear" collection
    collection3 = db["fear"]
    dictionary3 = [
        {
            "_id": 1,
            "surah": 2,
            "ayah": 197,
            "arabic": " وَ مَا تَفۡعَلُوۡا مِنۡ خَیۡرٍ  یَّعۡلَمۡہُ اللّٰہُ      ؕ    ؔ وَ تَزَوَّدُوۡا فَاِنَّ خَیۡرَ الزَّادِ التَّقۡوٰی  ۫  وَ اتَّقُوۡنِ یٰۤاُولِی الۡاَلۡبَابِ",
            "english": "And whatever good you do - Allah knows it. And take provisions, but indeed, the best provision is fear of Allah . And fear Me, O you of understanding."
        },
        {
            "_id": 2,
            "surah": 3,
            "ayah": 175,
            "arabic": "اِنَّمَا ذٰلِکُمُ الشَّیۡطٰنُ یُخَوِّفُ اَوۡلِیَآءَہٗ ۪ فَلَا تَخَافُوۡہُمۡ وَ خَافُوۡنِ  اِنۡ کُنۡتُمۡ  مُّؤۡمِنِیۡنَ ",
            "english": "That is only Satan who frightens [you] of his supporters. So fear them not, but fear Me, if you are [indeed] believers."
        },
        {
            "_id": 3,
            "surah": 33,
            "ayah": 39,
            "arabic": "الَّذِیۡنَ یُبَلِّغُوۡنَ  رِسٰلٰتِ اللّٰہِ وَ یَخۡشَوۡنَہٗ  وَ لَا یَخۡشَوۡنَ  اَحَدًا  اِلَّا اللّٰہَ ؕ وَ کَفٰی  بِاللّٰہِ  حَسِیۡبًا",
            "english": "[ Allah praises] those who convey the messages of Allah and fear Him and do not fear anyone but Allah . And sufficient is Allah as Accountant."
        },
        {
            "_id": 4,
            "surah": 8,
            "ayah": 29,
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ اٰمَنُوۡۤا اِنۡ تَتَّقُوا اللّٰہَ یَجۡعَلۡ لَّکُمۡ فُرۡقَانًا وَّ یُکَفِّرۡ عَنۡکُمۡ سَیِّاٰتِکُمۡ وَ یَغۡفِرۡ لَکُمۡ ؕ وَ اللّٰہُ  ذُو الۡفَضۡلِ  الۡعَظِیۡمِ",
            "english": "O you who have believed, if you fear Allah , He will grant you a criterion and will remove from you your misdeeds and forgive you. And Allah is the possessor of great bounty."
        },
        {
            "_id": 5,
            "surah": 10,
            "ayah": 62,
            "arabic": "اَلَاۤ اِنَّ اَوۡلِیَآءَ اللّٰہِ لَا خَوۡفٌ عَلَیۡہِمۡ وَ لَا  ہُمۡ  یَحۡزَنُوۡنَ",
            "english": " Unquestionably, [for] the allies of Allah there will be no fear concerning them, nor will they grieve"
        },
        {
            "_id": 6,
            "surah": 8,
            "ayah": 2,
            "arabic": "اِنَّمَا الۡمُؤۡمِنُوۡنَ الَّذِیۡنَ اِذَا ذُکِرَ اللّٰہُ وَجِلَتۡ قُلُوۡبُہُمۡ وَ اِذَا تُلِیَتۡ عَلَیۡہِمۡ اٰیٰتُہٗ زَادَتۡہُمۡ  اِیۡمَانًا وَّ عَلٰی رَبِّہِمۡ یَتَوَکَّلُوۡنَ ۚ",
            "english": "The believers are only those who, when Allah is mentioned, their hearts become fearful, and when His verses are recited to them, it increases them in faith; and upon their Lord they rely -"
        },
        {
            "_id": 7,
            "surah": 3,
            "ayah": 102,
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ اٰمَنُوا اتَّقُوا اللّٰہَ حَقَّ تُقٰتِہٖ وَ لَا تَمُوۡتُنَّ  اِلَّا وَ اَنۡتُمۡ  مُّسۡلِمُوۡنَ",
            "english": "O you who have believed, fear Allah as He should be feared and do not die except as Muslims [in submission to Him]."
        },
        {
            "_id": 8,
            "surah": 16,
            "ayah": 128,
            "arabic": "اِنَّ اللّٰہَ مَعَ الَّذِیۡنَ اتَّقَوۡا وَّ الَّذِیۡنَ ہُمۡ مُّحۡسِنُوۡنَ",
            "english": " Indeed, Allah is with those who fear Him and those who are doers of good."
        },
        {
            "_id": 9,
            "surah": 74,
            "ayah": 56,
            "arabic": " ہُوَ اَہۡلُ التَّقۡوٰی وَ اَہۡلُ الۡمَغۡفِرَۃِ",
            "english": "He is worthy of fear and adequate for [granting] forgiveness."
        },
        {
            "_id": 10,
            "surah": 65,
            "ayah": 5,
            "arabic": " وَ مَنۡ یَّتَّقِ اللّٰہَ یُکَفِّرۡ عَنۡہُ سَیِّاٰتِہٖ وَ یُعۡظِمۡ لَہٗۤ  اَجۡرًا",
            "english": "And and whoever fears Allah - He will remove for him his misdeeds and make great for him his reward"
        },
        {
            "_id": 11,
            "surah": 7,
            "ayah": 35,
            "arabic": "یٰبَنِیۡۤ  اٰدَمَ  اِمَّا یَاۡتِیَنَّکُمۡ رُسُلٌ مِّنۡکُمۡ یَقُصُّوۡنَ عَلَیۡکُمۡ اٰیٰتِیۡ ۙ فَمَنِ اتَّقٰی وَ اَصۡلَحَ فَلَا خَوۡفٌ عَلَیۡہِمۡ وَ لَا ہُمۡ یَحۡزَنُوۡنَ",
            "english": "O children of Adam, if there come to you messengers from among you relating to you My verses, then whoever fears Allah and reforms – there will be no fear concerning them, nor will they grieve."
        },
        {
            "_id": 12,
            "surah": 59,
            "ayah": 13,
            "arabic": "لَاَنۡتُمۡ  اَشَدُّ رَہۡبَۃً  فِیۡ  صُدُوۡرِہِمۡ  مِّنَ اللّٰہِ ؕ ذٰلِکَ بِاَنَّہُمۡ  قَوۡمٌ لَّا یَفۡقَہُوۡنَ",
            "english": "You [believers] are more fearful within their breasts than Allah . That is because they are a people who do not understand."
        },
        {
            "_id": 13,
            "surah": 2,
            "ayah": 194,
            "arabic": "  ۪ وَ اتَّقُوا اللّٰہَ وَ اعۡلَمُوۡۤا  اَنَّ اللّٰہَ مَعَ  الۡمُتَّقِیۡنَ",
            "english": "And fear Allah and know that Allah is with those who fear Him."
        },
        {
            "_id": 14,
            "surah": 57,
            "ayah": 28,
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ اٰمَنُوا اتَّقُوا اللّٰہَ  وَ اٰمِنُوۡا بِرَسُوۡلِہٖ یُؤۡتِکُمۡ کِفۡلَیۡنِ مِنۡ رَّحۡمَتِہٖ وَ یَجۡعَلۡ  لَّکُمۡ  نُوۡرًا تَمۡشُوۡنَ بِہٖ وَ یَغۡفِرۡ لَکُمۡ ؕ وَ اللّٰہُ  غَفُوۡرٌ رَّحِیۡمٌ",
            "english": "O you who have believed, fear Allah and believe in His Messenger; He will [then] give you a double portion of His mercy and make for you a light by which you will walk and forgive you; and Allah is Forgiving and Merciful."
        },
        {
            "_id": 15,
            "surah": 20,
            "ayah": 46,
            "arabic": "قَالَ لَا تَخَافَاۤ اِنَّنِیۡ مَعَکُمَاۤ  اَسۡمَعُ وَ اَرٰی",
            "english": "[ Allah ] said, “Fear not. Indeed, I am with you both; I hear and I see."
        }
    ]
    collection3.insert_many(dictionary3)
    # Adding "Joy" collection
    collection4 = db["joy"]
    dictionary4 = [
        {
            "_id": 1,
            "surah": 2,
            "ayah": 152,
            "arabic": "فَاذۡکُرُوۡنِیۡۤ اَذۡکُرۡکُمۡ  وَ اشۡکُرُوۡا لِیۡ وَ لَا تَکۡفُرُوۡنِ لۡمَغۡفِرَۃِ",
            "english": "So remember Me; I will remember you. And be grateful to Me and do not deny Me."
        },
        {
            "_id": 2,
            "surah": 93,
            "ayah": 11,
            "arabic": "وَ اَمَّا بِنِعۡمَۃِ  رَبِّکَ فَحَدِّثۡ",
            "english": "But as for the favor of your Lord, report [it]."
        },
        {
            "_id": 3,
            "surah": 9,
            "ayah": 109,
            "arabic": "وَ اللّٰہُ  لَا یَہۡدِی الۡقَوۡمَ  الظّٰلِمِیۡنَ",
            "english": "And Allah does not guide the wrongdoing people."
        },
        {
            "_id": 4,
            "surah": 28,
            "ayah": 77,
            "arabic": "وَ ابۡتَغِ  فِیۡمَاۤ  اٰتٰىکَ اللّٰہُ  الدَّارَ الۡاٰخِرَۃَ  وَ لَا تَنۡسَ نَصِیۡبَکَ مِنَ الدُّنۡیَا وَ اَحۡسِنۡ کَمَاۤ  اَحۡسَنَ اللّٰہُ  اِلَیۡکَ وَ لَا تَبۡغِ الۡفَسَادَ فِی الۡاَرۡضِ ؕ اِنَّ اللّٰہَ  لَا یُحِبُّ الۡمُفۡسِدِیۡنَ",
            "english": "But seek, through that which Allah has given you, the home of the Hereafter; and [yet], do not forget your share of the world. And do good as Allah has done good to you. And desire not corruption in the land. Indeed, Allah does not like corrupters."
        },
        {
            "_id": 5,
            "surah": 57,
            "ayah": 20,
            "arabic": "اِعۡلَمُوۡۤا اَنَّمَا الۡحَیٰوۃُ  الدُّنۡیَا لَعِبٌ وَّ لَہۡوٌ وَّ زِیۡنَۃٌ  وَّ تَفَاخُرٌۢ  بَیۡنَکُمۡ وَ تَکَاثُرٌ فِی الۡاَمۡوَالِ وَ الۡاَوۡلَادِ ؕ کَمَثَلِ غَیۡثٍ اَعۡجَبَ الۡکُفَّارَ نَبَاتُہٗ  ثُمَّ یَہِیۡجُ فَتَرٰىہُ مُصۡفَرًّا ثُمَّ  یَکُوۡنُ حُطَامًا ؕ وَ فِی الۡاٰخِرَۃِ  عَذَابٌ شَدِیۡدٌ ۙ وَّ مَغۡفِرَۃٌ مِّنَ اللّٰہِ وَ رِضۡوَانٌ ؕ وَ مَا الۡحَیٰوۃُ  الدُّنۡیَاۤ   اِلَّا مَتَاعُ  الۡغُرُوۡرِ",
            "english": "Know that the life of this world is but amusement and diversion and adornment and boasting to one another and competition in increase of wealth and children - like the example of a rain whose [resulting] plant growth pleases the tillers; then it dries and you see it turned yellow; then it becomes [scattered] debris. And in the Hereafter is severe punishment and forgiveness from Allah and approval. And what is the worldly life except the enjoyment of delusion."
        },
        {
            "_id": 6,
            "surah": 16,
            "ayah": 18,
            "arabic": "وَ اِنۡ تَعُدُّوۡا نِعۡمَۃَ اللّٰہِ لَا تُحۡصُوۡہَا ؕ اِنَّ  اللّٰہَ  لَغَفُوۡرٌ  رَّحِیۡمٌ",
            "english": "And if you should count the favors of Allah , you could not enumerate them. Indeed, Allah is Forgiving and Merciful."
        },
        {
            "_id": 7,
            "surah": 13,
            "ayah": 28,
            "arabic": "اَلَّذِیۡنَ اٰمَنُوۡا وَ تَطۡمَئِنُّ قُلُوۡبُہُمۡ بِذِکۡرِ اللّٰہِ ؕ اَلَا بِذِکۡرِ اللّٰہِ تَطۡمَئِنُّ الۡقُلُوۡبُ",
            "english": "Those who have believed and whose hearts are assured by the remembrance of Allah . Unquestionably, by the remembrance of Allah hearts are assured."
        },
        {
            "_id": 8,
            "surah": 31,
            "ayah": 12,
            "arabic": "وَ لَقَدۡ اٰتَیۡنَا لُقۡمٰنَ الۡحِکۡمَۃَ اَنِ اشۡکُرۡ لِلّٰہِ ؕ وَ مَنۡ یَّشۡکُرۡ فَاِنَّمَا یَشۡکُرُ لِنَفۡسِہٖ ۚ وَ مَنۡ کَفَرَ فَاِنَّ اللّٰہَ غَنِیٌّ حَمِیۡدٌ",
            "english": "And We had certainly given Luqman wisdom [and said], 'Be grateful to Allah .' And whoever is grateful is grateful for [the benefit of] himself. And whoever denies [His favor] - then indeed, Allah is Free of need and Praiseworthy."
        },
        {
            "_id": 9,
            "surah": 14,
            "ayah": 7,
            "arabic": "وَ اِذۡ  تَاَذَّنَ  رَبُّکُمۡ  لَئِنۡ شَکَرۡتُمۡ لَاَزِیۡدَنَّکُمۡ  وَ لَئِنۡ کَفَرۡتُمۡ  اِنَّ عَذَابِیۡ لَشَدِیۡدٌ",
            "english": "And [remember] when your Lord proclaimed, 'If you are grateful, I will surely increase you [in favor]; but if you deny, indeed, My punishment is severe.'"
        },
        {
            "_id": 10,
            "surah": 27,
            "ayah": 40,
            "arabic": "وَ مَنۡ شَکَرَ فَاِنَّمَا یَشۡکُرُ  لِنَفۡسِہٖ ۚ وَ مَنۡ  کَفَرَ  فَاِنَّ رَبِّیۡ غَنِیٌّ  کَرِیۡمٌ",
            "english": "His gratitude is only for [the benefit of] himself. And whoever is ungrateful - then indeed, my Lord is Free of need and Generous."
        },
        {
            "_id": 11,
            "surah": 2,
            "ayah": 21,
            "arabic": "یٰۤاَیُّہَا النَّاسُ اعۡبُدُوۡا رَبَّکُمُ الَّذِیۡ خَلَقَکُمۡ وَ الَّذِیۡنَ مِنۡ قَبۡلِکُمۡ لَعَلَّکُمۡ تَتَّقُوۡنَ",
            "english": " O mankind, worship your Lord, who created you and those before you, that you may become righteous",
        },
        {
            "_id": 12,
            "surah": 6,
            "ayah": 32,
            "arabic": "وَ مَا الۡحَیٰوۃُ  الدُّنۡیَاۤ  اِلَّا  لَعِبٌ وَّ لَہۡوٌ ؕ وَ  لَلدَّارُ الۡاٰخِرَۃُ  خَیۡرٌ  لِّلَّذِیۡنَ  یَتَّقُوۡنَ ؕ اَفَلَا  تَعۡقِلُوۡنَ",
            "english": "And the worldly life is not but amusement and diversion; but the home of the Hereafter is best for those who fear Allah , so will you not reason?",
        },
        {
            "_id": 13,
            "surah": 4,
            "ayah": 124,
            "arabic": "وَ مَنۡ یَّعۡمَلۡ مِنَ الصّٰلِحٰتِ مِنۡ ذَکَرٍ اَوۡ اُنۡثٰی وَ ہُوَ مُؤۡمِنٌ فَاُولٰٓئِکَ یَدۡخُلُوۡنَ الۡجَنَّۃَ  وَ لَا  یُظۡلَمُوۡنَ  نَقِیۡرًا",
            "english": "And whoever does righteous deeds, whether male or female, while being a believer – those will enter Paradise and will not be wronged, [even as much as] the speck on a date seed.",
        },
        {
            "_id": 14,
            "surah": 2,
            "ayah": 172,
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ اٰمَنُوۡا کُلُوۡا مِنۡ طَیِّبٰتِ مَا رَزَقۡنٰکُمۡ وَ اشۡکُرُوۡا لِلّٰہِ  اِنۡ  کُنۡتُمۡ اِیَّاہُ  تَعۡبُدُوۡنَ",
            "english": "O you who have believed, eat from the good things which We have provided for you and be grateful to Allah if it is [indeed] Him that you worship.",
        },
        {
            "_id": 15,
            "surah": 18,
            "ayah": 107,
            "arabic": "اِنَّ الَّذِیۡنَ اٰمَنُوۡا وَ عَمِلُوا الصّٰلِحٰتِ کَانَتۡ لَہُمۡ  جَنّٰتُ الۡفِرۡدَوۡسِ نُزُلًا",
            "english": "Indeed, those who have believed and done righteous deeds – they will have the Gardens of Paradise as a lodging",
        },
        {
            "_id": 16,
            "surah": 16,
            "ayah": 53,
            "arabic": "وَ مَا بِکُمۡ مِّنۡ نِّعۡمَۃٍ فَمِنَ اللّٰہِ ثُمَّ  اِذَا مَسَّکُمُ  الضُّرُّ  فَاِلَیۡہِ  تَجۡئَرُوۡنَ",
            "english": "And whatever you have of favor – it is from Allah . Then when adversity touches you, to Him you cry for help."
        }
    ]
    collection4.insert_many(dictionary4)
    # Adding "Sad" collection

    collection5 = db["sad"]
    dictionary5 = [
        {
            "_id": 1,
            "surah": 40,
            "ayah": 55,
            "arabic": "فَاصۡبِرۡ  اِنَّ وَعۡدَ اللّٰہِ حَقٌّ وَّ اسۡتَغۡفِرۡ لِذَنۡۢبِکَ وَ سَبِّحۡ بِحَمۡدِ رَبِّکَ بِالۡعَشِیِّ وَ الۡاِبۡکَارِ",
            "english": "So be patient, [O Muhammad]. Indeed, the promise of Allah is truth. And ask forgiveness for your sin and exalt [ Allah ] with praise of your Lord in the evening and the morning." 
        },
        {
            "_id": 2,
            "surah": 39,
            "ayah": 53,
            "arabic": "قُلۡ یٰعِبَادِیَ  الَّذِیۡنَ  اَسۡرَفُوۡا عَلٰۤی اَنۡفُسِہِمۡ  لَا تَقۡنَطُوۡا مِنۡ رَّحۡمَۃِ اللّٰہِ ؕ اِنَّ اللّٰہَ یَغۡفِرُ الذُّنُوۡبَ جَمِیۡعًا ؕ اِنَّہٗ  ہُوَ  الۡغَفُوۡرُ  الرَّحِیۡمُ",
            "english": "Say, 'O My servants who have transgressed against themselves [by sinning], do not despair of the mercy of Allah . Indeed, Allah forgives all sins. Indeed, it is He who is the Forgiving, the Merciful.'" 
        },
        {
            "_id": 3,
            "surah": 93,
            "ayah": 3,
            "arabic": "مَا وَدَّعَکَ رَبُّکَ وَ مَا قَلٰی ؕ",
            "english": "Your Lord has not taken leave of you, [O Muhammad], nor has He detested [you]." 
        },
        {
            "_id": 4,
            "surah": 93,
            "ayah": 5,
            "arabic": "وَ  لَسَوۡفَ یُعۡطِیۡکَ رَبُّکَ فَتَرۡضٰی ؕ",
            "english": "And your Lord is going to give you, and you will be satisfied." 
        },
        {
            "_id": 5,
            "surah": 30,
            "ayah": 36,
            "arabic": "وَ اِذَاۤ  اَذَقۡنَا النَّاسَ رَحۡمَۃً  فَرِحُوۡا بِہَا ؕ  وَ  اِنۡ  تُصِبۡہُمۡ سَیِّئَۃٌۢ  بِمَا قَدَّمَتۡ  اَیۡدِیۡہِمۡ   اِذَا  ہُمۡ  یَقۡنَطُوۡنَ",
            "english": "And when We let the people taste mercy, they rejoice therein, but if evil afflicts them for what their hands have put forth, immediately they despair." 
        },
        {
            "_id": 6,
            "surah": 94,
            "ayah": 5,
            "arabic": "فَاِنَّ مَعَ الۡعُسۡرِ  یُسۡرًا ۙ"
            ,
            "english": "For indeed, with hardship [will be] ease." 
        },
        {
            "_id": 7,
            "surah": 94,
            "ayah": 6,
            "arabic": "اِنَّ مَعَ الۡعُسۡرِ  یُسۡرًا ؕ",
            "english": "Indeed, with hardship [will be] ease." 
        },
        {
            "_id": 8,
            "surah": 2,
            "ayah": 153,
            "arabic": "یٰۤاَیُّہَا الَّذِیۡنَ اٰمَنُوا اسۡتَعِیۡنُوۡا بِالصَّبۡرِ وَ الصَّلٰوۃِ  ؕ اِنَّ اللّٰہَ مَعَ الصّٰبِرِیۡنَ",
            "english": "O you who have believed, seek help through patience and prayer. Indeed, Allah is with the patient." 
        },
        {
            "_id": 9,
            "surah": 93,
            "ayah": 7,
            "arabic": "وَ  وَجَدَکَ ضَآلًّا فَہَدٰی",
            "english": "And He found you lost and guided you" 
        },
        {
            "_id": 10,
            "surah": 3,
            "ayah": 139,
            "arabic": "وَ لَا تَہِنُوۡا وَ لَا تَحۡزَنُوۡا وَ اَنۡتُمُ الۡاَعۡلَوۡنَ  اِنۡ  کُنۡتُمۡ مُّؤۡمِنِیۡنَ",
            "english": "So do not weaken and do not grieve, and you will be superior if you are [true] believers."
        },
        {
            "_id": 11,
            "surah": 47,
            "ayah": 31,
            "arabic": "وَ لَنَبۡلُوَنَّکُمۡ  حَتّٰی نَعۡلَمَ الۡمُجٰہِدِیۡنَ مِنۡکُمۡ وَ الصّٰبِرِیۡنَ ۙ وَ نَبۡلُوَا۠ اَخۡبَارَکُمۡ",
            "english": "And We will surely test you until We make evident those who strive among you [for the cause of Allah ] and the patient, and We will test your affairs."
        },
        {
            "_id": 12,
            "surah": 29,
            "ayah": 69,
            "arabic": "وَ الَّذِیۡنَ جَاہَدُوۡا فِیۡنَا لَنَہۡدِیَنَّہُمۡ سُبُلَنَا ؕ وَ اِنَّ اللّٰہَ  لَمَعَ الۡمُحۡسِنِیۡنَ",
            "english": "And those who strive for Us – We will surely guide them to Our ways. And indeed, Allah is with the doers of good."
        },
        {
            "_id": 13,
            "surah": 17,
            "ayah": 9,
            "arabic": "اِنَّ ہٰذَا  الۡقُرۡاٰنَ  یَہۡدِیۡ  لِلَّتِیۡ ہِیَ اَقۡوَمُ وَ یُبَشِّرُ الۡمُؤۡمِنِیۡنَ الَّذِیۡنَ یَعۡمَلُوۡنَ الصّٰلِحٰتِ اَنَّ لَہُمۡ اَجۡرًا کَبِیۡرًا",
            "english": "Indeed, this Qur'an guides to that which is most suitable and gives good tidings to the believers who do righteous deeds that they will have a great reward."
        },
        {
            "_id": 14,
            "surah": 65,
            "ayah": 3,
            "arabic": "وَّ یَرۡزُقۡہُ  مِنۡ حَیۡثُ لَا یَحۡتَسِبُ ؕ وَ مَنۡ  یَّتَوَکَّلۡ عَلَی اللّٰہِ  فَہُوَ حَسۡبُہٗ",
            "english": "And will provide for him from where he does not expect. And whoever relies upon Allah – then He is sufficient for him."
        },
        {
            "_id": 15,
            "surah": 20,
            "ayah": 132,
            "arabic": "وَ اۡمُرۡ اَہۡلَکَ بِالصَّلٰوۃِ وَ اصۡطَبِرۡ عَلَیۡہَا ؕ لَا نَسۡئَلُکَ رِزۡقًا ؕ نَحۡنُ نَرۡزُقُکَ ؕ وَ الۡعَاقِبَۃُ  لِلتَّقۡوٰی",
            "english": "And enjoin prayer upon your family [and people] and be steadfast therein. We ask you not for provision; We provide for you, and the [best] outcome is for [those of] righteousness."
        },
        {
            "_id": 16,
            "surah": 9,
            "ayah": 51,
            "arabic": "وَ عَلَی اللّٰہِ  فَلۡیَتَوَکَّلِ  الۡمُؤۡمِنُوۡنَ",
            "english": "And upon Allah let the believers rely."
        }
    ]

    collection5.insert_many(dictionary5)

if __name__ == "__main__":
    main()