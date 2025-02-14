import os
import urllib
import time
import urllib.request
data ='''Translingual,http://upload.wikimedia.org/wikipedia/commons/f/f3/Earth_flag_PD.jpg/45px-Earth_flag_PD.jpg
English,http://upload.wikimedia.org/wikipedia/commons/0/0b/English_language.svg
Abenaki,http://upload.wikimedia.org/wikipedia/commons/f/fb/Flag_of_Western_Abenaki.svg
Abkhaz,http://upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Abkhazia.svg
Adyghe,http://upload.wikimedia.org/wikipedia/commons/1/16/Flag_of_Adygea.svg
Afar,http://upload.wikimedia.org/wikipedia/commons/3/34/Flag_of_Djibouti.svg
Afrikaans,http://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_South_Africa_(1928–1994).svg
Akan,http://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Ghana.svg
Akkala_Sami,Inari_Sami,Kemi_Sami,Kildin_Sami,Lule_Sami,Northern_Sami,Pite_Sami,Skolt_Sami,Southern_Sami,Ter_Sami,Ume_Sami,http://upload.wikimedia.org/wikipedia/commons/1/1b/Sami_flag.svg
Albanian,http://upload.wikimedia.org/wikipedia/commons/3/36/Flag_of_Albania.svg
Alemannic_German,http://upload.wikimedia.org/wikipedia/commons/0/08/Flag_of_Switzerland_(Pantone).svg
Aleut,http://upload.wikimedia.org/wikipedia/commons/e/e6/Flag_of_Alaska.svg
American_Sign_Language,http://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg
Amharic,http://upload.wikimedia.org/wikipedia/commons/7/71/Flag_of_Ethiopia.svg
Ancient_Greek,http://upload.wikimedia.org/wikipedia/commons/5/58/Byzantine_imperial_flag,_14th_century,_square.svg
Angevin,http://upload.wikimedia.org/wikipedia/commons/a/ad/Flag_of_Anjou.svg
Annobonese,http://upload.wikimedia.org/wikipedia/commons/8/86/Annobon.svg
Arabic,http://upload.wikimedia.org/wikipedia/commons/2/2b/Flag_of_the_Arab_League.svg
Aragonese,http://upload.wikimedia.org/wikipedia/commons/1/18/Flag_of_Aragon.svg
Armenian,http://upload.wikimedia.org/wikipedia/commons/2/2f/Flag_of_Armenia.svg
Asturian,http://upload.wikimedia.org/wikipedia/commons/3/3e/Flag_of_Asturias.svg
Avar,http://upload.wikimedia.org/wikipedia/commons/7/77/Khunz_Wolf_3b.svg
Aymara,Bolivian_Sign_Language,http://upload.wikimedia.org/wikipedia/commons/d/de/Flag_of_Bolivia_,state).svg
Azerbaijani,http://upload.wikimedia.org/wikipedia/commons/d/dd/Flag_of_Azerbaijan.svg
Baharna_Arabic,http://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Bahrain.svg
Balinese,http://upload.wikimedia.org/wikipedia/commons/a/a3/Flag_of_Bali.svg
Bambara,http://upload.wikimedia.org/wikipedia/commons/9/92/Flag_of_Mali.svg
Bashkir,http://upload.wikimedia.org/wikipedia/commons/3/3d/Flag_of_Bashkortostan.svg
Basque,http://upload.wikimedia.org/wikipedia/commons/2/2d/Flag_of_the_Basque_Country.svg
Bavarian,http://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_Bavaria_(lozengy).svg
Belarusian,http://upload.wikimedia.org/wikipedia/commons/8/85/Flag_of_Belarus.svg
Belizean_Creole,http://upload.wikimedia.org/wikipedia/commons/e/e7/Flag_of_Belize.svg
Bengali,http://upload.wikimedia.org/wikipedia/commons/f/f9/Flag_of_Bangladesh.svg
Bislama,http://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Vanuatu.svg
Bourguignon,http://upload.wikimedia.org/wikipedia/commons/3/3c/Flag_of_Bourgogne.svg
Breton,http://upload.wikimedia.org/wikipedia/commons/7/7d/Flag_of_Brittany.svg
Brunei_Malay,http://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Brunei.svg
Bulgarian,http://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Bulgaria.svg
Burmese,http://upload.wikimedia.org/wikipedia/commons/8/8c/Flag_of_Myanmar.svg
Buryat,http://upload.wikimedia.org/wikipedia/commons/6/68/Flag_of_Buryatia.svg
Cantonese,http://upload.wikimedia.org/wikipedia/commons/5/5b/Flag_of_Hong_Kong.svg
Catalan,http://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Catalonia.svg
Cavineña,http://upload.wikimedia.org/wikipedia/commons/3/3f/Flag_of_beni.svg
Central_Kurdish,Northern_Kurdish,Southern_Kurdish,http://upload.wikimedia.org/wikipedia/commons/3/35/Flag_of_Kurdistan.svg
Chamorro,http://upload.wikimedia.org/wikipedia/commons/0/07/Flag_of_Guam.svg
Champenois,http://upload.wikimedia.org/wikipedia/commons/f/f1/Flag_of_Champagne-Ardenne.svg
Chechen,http://upload.wikimedia.org/wikipedia/commons/1/13/Flag_of_the_Chechen_Republic.svg
Cherokee,http://upload.wikimedia.org/wikipedia/commons/4/4d/Flag_of_the_Cherokee_Nation.svg
Chinese,Mandarin,http://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_the_People's_Republic_of_China.svg
Choctaw,http://upload.wikimedia.org/wikipedia/commons/2/2b/ChoctawFlag.png/45px-ChoctawFlag.png
Chuvash,http://upload.wikimedia.org/wikipedia/commons/d/d7/Flag_of_Chuvashia.svg
Cornish,http://upload.wikimedia.org/wikipedia/commons/b/b8/Flag_of_Cornwall.svg
Corsican,http://upload.wikimedia.org/wikipedia/commons/7/7c/Flag_of_Corsica.svg
Crimean_Tatar,http://upload.wikimedia.org/wikipedia/commons/0/08/Flag_of_the_Crimean_Tatar_people.svg
Cuban_Sign_Language,http://upload.wikimedia.org/wikipedia/commons/b/bd/Flag_of_Cuba.svg
Czech,http://upload.wikimedia.org/wikipedia/commons/c/cb/Flag_of_the_Czech_Republic.svg
Dalmatian,http://upload.wikimedia.org/wikipedia/commons/2/2f/Flag_of_Kingdom_of_Dalmatia_,1852-1860).svg
Danish,http://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Denmark.svg
Dhivehi,http://upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Maldives.svg
Dutch,http://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg
Dzongkha,http://upload.wikimedia.org/wikipedia/commons/9/91/Flag_of_Bhutan.svg
Eastern_Mari,http://upload.wikimedia.org/wikipedia/commons/a/a7/Flag_of_Mari_El.svg
Egyptian_Arabic,http://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Egypt.svg
Emilian,http://upload.wikimedia.org/wikipedia/commons/1/1f/Flag_of_Bologna_2.png/45px-Flag_of_Bologna_2.png
Erzya,http://upload.wikimedia.org/wikipedia/commons/2/28/Erzya_Flag.svg
Esperanto,http://upload.wikimedia.org/wikipedia/commons/f/f5/Flag_of_Esperanto.svg
Estonian,http://upload.wikimedia.org/wikipedia/commons/8/8f/Flag_of_Estonia.svg
Evenki,http://upload.wikimedia.org/wikipedia/commons/7/72/Flag_of_Evenks.svg
Ewe,http://upload.wikimedia.org/wikipedia/commons/b/b8/Flag_of_the_Ewe_people.svg
Extremaduran,http://upload.wikimedia.org/wikipedia/commons/4/4d/Flag_of_Extremadura_(with_coat_of_arms).svg
Fala,http://upload.wikimedia.org/wikipedia/commons/b/b7/Bandera_de_Valverde_del_Fresno_(Cáceres).svg
Faroese,http://upload.wikimedia.org/wikipedia/commons/3/3c/Flag_of_the_Faroe_Islands.svg
Fijian,http://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Fiji.svg
Finnish,http://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Finland.svg
Forest_Nenets,Tundra_Nenets,http://upload.wikimedia.org/wikipedia/commons/1/15/Flag_of_Nenets_Autonomous_District.svg
Franc-Comtois,http://upload.wikimedia.org/wikipedia/commons/9/96/Flag_of_Franche-Comté.svg
Franco-Provençal,http://upload.wikimedia.org/wikipedia/commons/9/90/Flag_of_Valle_dAosta.svg
French,http://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg
Friulian,http://upload.wikimedia.org/wikipedia/commons/8/87/Bandiere_dal_Friûl.svg
Gagauz,http://upload.wikimedia.org/wikipedia/commons/6/69/Flag_of_Gagauzia.svg
Galician,http://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Galicia.svg
Garhwali,http://upload.wikimedia.org/wikipedia/commons/7/7d/Flag_of_the_Princely_State_of_Tehri_Garhwal.svg
Garifuna,http://upload.wikimedia.org/wikipedia/commons/b/b1/Flag_of_Garifuna.svg
Georgian,http://upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Georgia.svg
German,http://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg
Gilbertese,http://upload.wikimedia.org/wikipedia/commons/d/d3/Flag_of_Kiribati.svg
Greek,http://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Greece.svg
Greenlandic,http://upload.wikimedia.org/wikipedia/commons/0/09/Flag_of_Greenland.svg
Guaraní,http://upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Paraguay.svg
Guianese_Creole,http://upload.wikimedia.org/wikipedia/commons/2/29/Flag_of_French_Guiana.svg
Guinea-Bissau_Creole,http://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Guinea-Bissau.svg
Gujarati,Hindi,Marathi,Telugu,http://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_India.svg
Guyanese_Creole_English,http://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_Guyana.svg
Haitian_Creole,http://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Haiti.svg
Hawaiian,http://upload.wikimedia.org/wikipedia/commons/e/ef/Flag_of_Hawaii.svg
Hijazi_Arabic,http://upload.wikimedia.org/wikipedia/commons/6/61/Flag_of_Hejaz_1926.svg
Hungarian,Hungarian_Sign_Language,http://upload.wikimedia.org/wikipedia/commons/c/c1/Flag_of_Hungary.svg
Hunsrik,http://upload.wikimedia.org/wikipedia/commons/6/63/Bandeira_do_Rio_Grande_do_Sul.svg
Icelandic,http://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Iceland.svg
Ido,http://upload.wikimedia.org/wikipedia/commons/f/f1/Flag_of_Ido.svg
Indo-Portuguese,http://upload.wikimedia.org/wikipedia/commons/7/72/Flag_of_Portugal_,1640).svg
Indonesian,http://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg
Ingrian,http://upload.wikimedia.org/wikipedia/commons/2/27/Flag_igora.svg
Ingush,http://upload.wikimedia.org/wikipedia/commons/0/00/Flag_of_Ingushetia.svg
Interlingua,http://upload.wikimedia.org/wikipedia/commons/7/7e/Flag_of_Interlingua.svg
Interlingue,http://upload.wikimedia.org/wikipedia/commons/5/5b/Flag_of_Interlingue.svg
Inuktitut,http://upload.wikimedia.org/wikipedia/commons/9/90/Flag_of_Nunavut.svg
Irish,http://upload.wikimedia.org/wikipedia/commons/4/45/Flag_of_Ireland.svg
Istriot,http://upload.wikimedia.org/wikipedia/commons/6/68/Zastava_Rovinja.svg
Italian,http://upload.wikimedia.org/wikipedia/commons/0/03/Flag_of_Italy.svg
Jamaican_Creole,http://upload.wikimedia.org/wikipedia/commons/0/0a/Flag_of_Jamaica.svg
Japanese,Okinawan,http://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg
Juba_Arabic,http://upload.wikimedia.org/wikipedia/commons/7/7a/Flag_of_South_Sudan.svg
Kabuverdianu,http://upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Cape_Verde.svg
Kalmyk,http://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Kalmykia.svg
Kannada,http://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Karnataka.svg
Kanuri,http://upload.wikimedia.org/wikipedia/commons/9/95/Flag_of_the_Kanuri_people.svg
Karakalpak,http://upload.wikimedia.org/wikipedia/commons/1/16/Flag_of_Karakalpakstan.svg
Karelian,http://upload.wikimedia.org/wikipedia/commons/6/69/Flag_of_Karelia.svg
Kashubian,http://upload.wikimedia.org/wikipedia/commons/6/61/Provinz_Pommern_flag.svg
Kazakh,http://upload.wikimedia.org/wikipedia/commons/d/d3/Flag_of_Kazakhstan.svg
Khakas,http://upload.wikimedia.org/wikipedia/commons/e/ec/Flag_of_Khakassia.svg
Khanty,Mansi,http://upload.wikimedia.org/wikipedia/commons/7/70/Flag_of_Yugra.svg
Khmer,http://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_Cambodia.svg
Komi-Permyak,http://upload.wikimedia.org/wikipedia/commons/0/02/Flag_of_Permyakia.svg
Komi-Zyrian,http://upload.wikimedia.org/wikipedia/commons/5/54/Flag_of_Komi.svg
Korean,http://upload.wikimedia.org/wikipedia/commons/0/09/Flag_of_South_Korea.svg
Koryak,http://upload.wikimedia.org/wikipedia/commons/0/0d/Flag_of_Koryakia.svg
Krio,http://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_Sierra_Leone.svg
Kumyk,http://upload.wikimedia.org/wikipedia/commons/1/1c/Flag_of_Kumyks.svg
Kuna,http://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Kuna_Yala.svg
Kyrgyz,http://upload.wikimedia.org/wikipedia/commons/c/c7/Flag_of_Kyrgyzstan.svg
Ladin,http://upload.wikimedia.org/wikipedia/commons/6/62/Flag_of_Ladinia.svg
Lahu,http://upload.wikimedia.org/wikipedia/commons/1/17/Lahu_flag.svg
Lao,http://upload.wikimedia.org/wikipedia/commons/5/56/Flag_of_Laos.svg
Latin,http://upload.wikimedia.org/wikipedia/commons/a/a6/Flag_of_Rome.svg
Latvian,http://upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Latvia.svg
Leonese,http://upload.wikimedia.org/wikipedia/commons/8/8b/Bandera_de_León.svg
Libyan_Arabic,http://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Libya.svg
Ligurian,http://upload.wikimedia.org/wikipedia/commons/8/88/Flag_of_Liguria.svg
Limbu,http://upload.wikimedia.org/wikipedia/commons/a/a2/Flag_of_Limbuwan.svg
Limburgish,http://upload.wikimedia.org/wikipedia/commons/d/d1/Flag_of_Limburg_,Netherlands).svg
Lingala,http://upload.wikimedia.org/wikipedia/commons/6/6f/Flag_of_the_Democratic_Republic_of_the_Congo.svg
Lithuanian,http://upload.wikimedia.org/wikipedia/commons/1/11/Flag_of_Lithuania.svg
Livonian,http://upload.wikimedia.org/wikipedia/commons/4/42/Flag_of_the_Livonians.svg
Lojban,http://upload.wikimedia.org/wikipedia/commons/d/d5/Lojban_flag_public_domain.svg
Lombard,http://upload.wikimedia.org/wikipedia/commons/e/ea/Flag_of_Lombardy.svg
Louisiana_Creole_French,http://upload.wikimedia.org/wikipedia/commons/e/e0/Flag_of_Louisiana.svg
Lower_Sorbian,Upper_Sorbian,http://upload.wikimedia.org/wikipedia/commons/c/c0/Flag_of_Sorbs.svg
Ludian,http://upload.wikimedia.org/wikipedia/commons/6/6c/Ludic_flag.svg
Luxembourgish,http://upload.wikimedia.org/wikipedia/commons/d/da/Flag_of_Luxembourg.svg
Macedonian,http://upload.wikimedia.org/wikipedia/commons/f/f8/Flag_of_Macedonia.svg
Maguindanao,http://upload.wikimedia.org/wikipedia/commons/8/87/Flag_of_Maguindanao.svg
Malagasy,http://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Madagascar.svg
Malay,http://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg
Malayalam,http://upload.wikimedia.org/wikipedia/commons/7/74/Malayali_flag.svg
Maltese,http://upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Malta.svg
Manchu,http://upload.wikimedia.org/wikipedia/commons/8/86/Flag_of_China_,1862–1889).svg
Manx,http://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_the_Isle_of_Man.svg
Maori,http://upload.wikimedia.org/wikipedia/commons/3/3e/Flag_of_New_Zealand.svg
Mapudungun,http://upload.wikimedia.org/wikipedia/commons/f/f1/Flag_of_the_Mapuches.svg
Marshallese,http://upload.wikimedia.org/wikipedia/commons/2/2e/Flag_of_the_Marshall_Islands.svg
Mauritian_Creole,http://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Mauritius.svg
Megleno-Romanian,http://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Greek_Macedonia.svg
Mi\kmaq,http://upload.wikimedia.org/wikipedia/commons/3/3f/Mikmaq_State_Flag.svg
Michif,http://upload.wikimedia.org/wikipedia/commons/f/f4/Metis_Blue.svg
Middle_Dutch,http://upload.wikimedia.org/wikipedia/commons/3/3c/Flag_of_the_prince-bishopric_of_Utrecht.svg
Middle_English,http://upload.wikimedia.org/wikipedia/commons/b/be/Flag_of_England.svg
Middle_French,Old_French,http://upload.wikimedia.org/wikipedia/commons/9/92/Pavillon_royal_de_la_France.svg
Middle_Irish,http://upload.wikimedia.org/wikipedia/commons/8/8d/Flag_of_Leinster.svg
Min_Nan,http://upload.wikimedia.org/wikipedia/commons/7/72/Flag_of_the_Republic_of_China.svg
Mirandese,http://upload.wikimedia.org/wikipedia/commons/4/41/Bandeira-de-Miranda-do-Douro.png/45px-Bandeira-de-Miranda-do-Douro.png
Miskito,http://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Nicaragua.svg
Moksha,http://upload.wikimedia.org/wikipedia/commons/e/e1/Flag_of_the_Moksha_people.svg
Mongolian,http://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Mongolia.svg
Moroccan_Arabic,http://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Morocco.svg
Najdi_Arabic,http://upload.wikimedia.org/wikipedia/commons/1/17/Flag_of_the_Emirate_of_Hail.svg
Nauruan,http://upload.wikimedia.org/wikipedia/commons/3/30/Flag_of_Nauru.svg
Navajo,http://upload.wikimedia.org/wikipedia/commons/0/0c/Navajo_flag.svg
Neapolitan,http://upload.wikimedia.org/wikipedia/commons/7/7c/Flag_of_Campania.png/45px-Flag_of_Campania.png
Nepali,http://upload.wikimedia.org/wikipedia/commons/9/9b/Flag_of_Nepal.svg
Niuean,http://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Niue.svg
Norman,http://upload.wikimedia.org/wikipedia/commons/6/60/Basse-Normandie_flag.svg
Norwegian_Bokmål,Norwegian_Nynorsk,http://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Norway.svg
Novial,http://upload.wikimedia.org/wikipedia/commons/e/ed/Flag_of_Novial.svg
Occitan,http://upload.wikimedia.org/wikipedia/commons/6/6d/Flag_of_Occitania_(with_star).svg
Old_Armenian,http://upload.wikimedia.org/wikipedia/commons/7/77/Artaxiad.svg
Old_English,http://upload.wikimedia.org/wikipedia/commons/e/e0/Flag_of_Wessex.svg
Old_Georgian,http://upload.wikimedia.org/wikipedia/commons/c/cf/Kartli_-_drosha_jvari.svg
Old_Irish,http://upload.wikimedia.org/wikipedia/commons/4/42/Triskele-Symbol1.svg
Old_Occitan,http://upload.wikimedia.org/wikipedia/commons/6/6f/Flag_of_Provence.svg
Old_Portuguese,http://upload.wikimedia.org/wikipedia/commons/2/25/PortugueseFlag1143.svg
Omani_Arabic,http://upload.wikimedia.org/wikipedia/commons/d/dd/Flag_of_Oman.svg
Ossetian,http://upload.wikimedia.org/wikipedia/commons/1/1c/Flag_of_North_Ossetia.svg
Ottoman_Turkish,http://upload.wikimedia.org/wikipedia/commons/b/b0/Ottoman_flag.svg
Papiamentu,http://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_the_Netherlands_Antilles.png/45px-Flag_of_the_Netherlands_Antilles.png
Pashto,http://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Afghanistan.svg
Pennsylvania_German,http://upload.wikimedia.org/wikipedia/commons/f/f7/Flag_of_Pennsylvania.svg
Persian,http://upload.wikimedia.org/wikipedia/commons/c/ca/Flag_of_Iran.svg
Picard,http://upload.wikimedia.org/wikipedia/commons/5/50/Picardy_flag.png/45px-Picardy_flag.png
Pichinglis,http://upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Equatorial_Guinea.svg
Piedmontese,http://upload.wikimedia.org/wikipedia/commons/b/b9/Flag_of_Piedmont.svg
Pijin,http://upload.wikimedia.org/wikipedia/commons/7/74/Flag_of_the_Solomon_Islands.svg
Polish,http://upload.wikimedia.org/wikipedia/commons/1/12/Flag_of_Poland.svg
Portuguese,http://upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Portuguese_language_(PT-BR).svg
Quechua,http://upload.wikimedia.org/wikipedia/commons/8/8f/Quechuas_flag.svg
Rapa_Nui,http://upload.wikimedia.org/wikipedia/commons/d/d8/Flag_of_Rapa_Nui,_Chile.svg
Rohingya,http://upload.wikimedia.org/wikipedia/commons/f/f1/Rohingya_flag.png/45px-Rohingya_flag.png
Romagnol,http://upload.wikimedia.org/wikipedia/commons/b/b1/Flag_of_San_Marino.svg
Romani,http://upload.wikimedia.org/wikipedia/commons/1/10/Flag_of_the_Romani_people.svg
Romanian,Transylvanian_Saxon,http://upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Romania.svg
Romansch,http://upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Canton_of_Graubünden.svg
Russian,http://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Russia.svg
Rusyn,http://upload.wikimedia.org/wikipedia/commons/1/1f/Flag_of_Carpathian_Ruthenia.svg
Samoan,http://upload.wikimedia.org/wikipedia/commons/3/31/Flag_of_Samoa.svg
Sardinian,http://upload.wikimedia.org/wikipedia/commons/f/fd/Flag_of_the_Italian_region_Sardinia.svg
Saterland_Frisian,http://upload.wikimedia.org/wikipedia/commons/e/e0/Saterland_flag.svg
Scots,http://upload.wikimedia.org/wikipedia/commons/1/10/Flag_of_Scotland.svg
Scottish_Gaelic,http://upload.wikimedia.org/wikipedia/commons/4/48/Lionrampant.svg
Serbo-Croatian,http://upload.wikimedia.org/wikipedia/commons/7/77/Serbo-Croatian_language_flag.gif/45px-Serbo-Croatian_language_flag.gif
Seychellois_Creole,http://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Seychelles.svg
Shan,http://upload.wikimedia.org/wikipedia/commons/b/b3/Flag_of_the_Shan_State.svg
Sicilian,http://upload.wikimedia.org/wikipedia/commons/7/7a/Flag_of_Sicily.svg
Sikkimese,http://upload.wikimedia.org/wikipedia/commons/6/6b/Flag_of_Sikkim_(1967-1975).svg
Sindhi,http://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_Sindh.svg
Sinhalese,http://upload.wikimedia.org/wikipedia/commons/1/11/Flag_of_Sri_Lanka.svg
Slovak,http://upload.wikimedia.org/wikipedia/commons/e/e6/Flag_of_Slovakia.svg
Slovene,http://upload.wikimedia.org/wikipedia/commons/f/f0/Flag_of_Slovenia.svg
Somali,http://upload.wikimedia.org/wikipedia/commons/a/a0/Flag_of_Somalia.svg
Sotho,http://upload.wikimedia.org/wikipedia/commons/4/4a/Flag_of_Lesotho.svg
Southern_Altai,http://upload.wikimedia.org/wikipedia/commons/f/ff/Flag_of_Altai_Republic.svg
Spanish,http://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Spanish_language_(ES-MX).svg
Sranan_Tongo,http://upload.wikimedia.org/wikipedia/commons/6/60/Flag_of_Suriname.svg
Sudanese_Arabic,http://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_Sudan.svg
Swabian,http://upload.wikimedia.org/wikipedia/commons/1/14/Flagge_Königreich_Württemberg.svg
Swahili,http://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg
Swedish,http://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Sweden.svg
Tagalog,http://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_the_Philippines.svg
Tahitian,http://upload.wikimedia.org/wikipedia/commons/d/db/Flag_of_French_Polynesia.svg
Tajik,http://upload.wikimedia.org/wikipedia/commons/d/d0/Flag_of_Tajikistan.svg
Tarantino,http://upload.wikimedia.org/wikipedia/commons/4/4f/Flag_of_Apulia.png/45px-Flag_of_Apulia.png
Tatar,http://upload.wikimedia.org/wikipedia/commons/2/28/Flag_of_Tatarstan.svg
Tausug,http://upload.wikimedia.org/wikipedia/commons/d/da/Late_19th_Century_Flag_of_Sulu.svg
Tetum,http://upload.wikimedia.org/wikipedia/commons/2/26/Flag_of_East_Timor.svg
Thai,http://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg
Tibetan,http://upload.wikimedia.org/wikipedia/commons/3/3c/Flag_of_Tibet.svg
Tigrinya,http://upload.wikimedia.org/wikipedia/commons/2/29/Flag_of_Eritrea.svg
Tok_Pisin,http://upload.wikimedia.org/wikipedia/commons/e/e3/Flag_of_Papua_New_Guinea.svg
Tokelauan,http://upload.wikimedia.org/wikipedia/commons/8/8e/Flag_of_Tokelau.svg
Tongan,http://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Tonga.svg
Tourangeau,http://upload.wikimedia.org/wikipedia/commons/0/0b/Flag_of_Touraine.svg
Tswana,ǃXóõ,http://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_Botswana.svg
Tunisian_Arabic,http://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg
Turkish,http://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg
Turkmen,http://upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Turkmenistan.svg
Tuvaluan,http://upload.wikimedia.org/wikipedia/commons/3/38/Flag_of_Tuvalu.svg
Tuvan,http://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Tuva.svg
Udmurt,http://upload.wikimedia.org/wikipedia/commons/c/c7/Flag_of_Udmurtia.svg
Ukrainian,http://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Ukraine.svg
Urdu,http://upload.wikimedia.org/wikipedia/commons/3/32/Flag_of_Pakistan.svg
Uyghur,http://upload.wikimedia.org/wikipedia/commons/2/2c/Kokbayraq_flag.svg
Uzbek,http://upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Uzbekistan.svg
Venetian,http://upload.wikimedia.org/wikipedia/commons/d/d5/Flag_of_Veneto.svg
Veps,http://upload.wikimedia.org/wikipedia/commons/4/45/Flag_of_Vepsia.svg
Vietnamese,http://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg
Volga_German,http://upload.wikimedia.org/wikipedia/commons/5/55/Flag_of_Volga_Germans_,version).svg
Votic,http://upload.wikimedia.org/wikipedia/commons/d/d1/Votic_Flag.svg
Võro,http://upload.wikimedia.org/wikipedia/commons/c/c1/Võrumaa_lipp.svg
Walloon,http://upload.wikimedia.org/wikipedia/commons/4/42/Flag_of_Wallonia.svg
Welsh,http://upload.wikimedia.org/wikipedia/commons/d/dc/Flag_of_Wales.svg
West_Frisian,http://upload.wikimedia.org/wikipedia/commons/c/ca/Frisian_flag.svg
Western_Mari,http://upload.wikimedia.org/wikipedia/commons/2/24/Flag_of_Gornomariysky_rayon.svg
Wolof,http://upload.wikimedia.org/wikipedia/commons/f/fd/Flag_of_Senegal.svg
Yakut,http://upload.wikimedia.org/wikipedia/commons/e/eb/Flag_of_Sakha.svg
Yonaguni,http://upload.wikimedia.org/wikipedia/commons/4/45/Flag_of_Yonaguni,_Okinawa.svg'''

for line in data.splitlines():
    l = line.split(",")
    try:
        time.sleep(1)
        urllib.request.urlretrieve(l[-1],l[0]+".svg")
    except Exception as e: 
        print(e)
        print(l[-1],l[-1].split("/")[-1])

