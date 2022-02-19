verbo =input()

personas ={
    'yo':{
        'ar':'o',
        'er':'o',
        'ir':'o'
    },
    'el':{
        'ar':'a',
        'er':'e',
        'ir':'e'
    },
    'tu':{
        'ar':'as',
        'er':'es',
        'ir':'es'
    },
    'nosotros':{
        'ar':'amos',
        'er':'emos',
        'ir':'imos'
    },
    'ellos':{
        'ar':'an',
        'er':'en',
        'ir':'en'
    }
}
letraFinal = verbo[len(verbo)-1]
letraAntesFinal = verbo[len(verbo)-2]

terminacion = letraAntesFinal+letraFinal
verboSinTerminacion = verbo.replace(terminacion,"")


for persona in personas:
    print(persona+' '+)