LTS_list = [
    "dpage@bhncdsb.ca",
    "vandenboschl@hwcdsb.ca",
    "LENORA.SAWYER@granderie.ca",
    "h.grenville@hotmail.com",
    "boutrosc@hdsb.ca",
    "morrisli@hdsb.ca",
    "anthonyj@hdsb.ca",
    "tudhopen@hdsb.ca",
    "cgraves@hwdsb.on.ca",
    "allison.okopny@peelsb.com",
    "jeffery.wells@peelsb.com",
    "usha.kelleymaharaj@tdsb.on.ca",
    "murphyp@hdsb.ca",
    "erin.lepischak@gmail.com",
    "MGUPTA@hwdsb.on.ca",
    "newberryr@hwcdsb.ca",
    "grubisicn@hwcdsb.ca",
    "MerrickS@hcdsb.org",
    "sattridg@hwdsb.on.ca",
    "donica@hwdsb.on.ca",
    "saltysh@hdsb.ca",
    "rroddie@hwdsb.on.ca",
    "slindner@hwdsb.on.ca",
    "tarucka@my.yorku.ca",
    "rroddie@hwdsb.on.ca",
    "caroline.fussek@peelsb.com",
    "clmccomb@hwdsb.on.ca",
    "JSmajda@niagaracc.com",
    "elepisch@hwdsb.on.ca",
    "lcope@hwdsb.on.ca",
    "sborges@bhncdsb.ca",
    "zpavlovi@hwdsb.on.ca",
    "tran.bochen@tdsb.on.ca"
]

emails = [
    "dpage@bhncdsb.ca",
    "vandenboschl@hwcdsb.ca",
    "LENORA.SAWYER@granderie.ca",
    "boutrosc@hdsb.ca",
    "anthonyj@hdsb.ca",
    "tudhopen@hdsb.ca",
    "cgraves@hwdsb.on.ca",
    "jeffery.wells@peelsb.com",
    "usha.kelleymaharaj@tdsb.on.ca",
    "murphyp@hdsb.ca",
    "MGUPTA@hwdsb.on.ca",
    "newberryr@hwcdsb.ca",
    "grubisicn@hwcdsb.ca",
    "MerrickS@hcdsb.org",
    "sattridg@hwdsb.on.ca",
    "donica@hwdsb.on.ca",
    "saltysh@hdsb.ca",
    "rroddie@hwdsb.on.ca",
    "caroline.fussek@peelsb.com",
    "clmccomb@hwdsb.on.ca",
    "JSmajda@niagaracc.com",
    "elepisch@hwdsb.on.ca",
    "lcope@hwdsb.on.ca",
    "sborges@bhncdsb.ca",
    "zpavlovi@hwdsb.on.ca",
    "tran.bochen@tdsb.on.ca",
    "caroline.hamilton@peelsb.com"
]

new_educators = []

for name in LTS_list:
    if name in emails:
        continue
    new_educators.append(name)
    print(name)

print(new_educators)
