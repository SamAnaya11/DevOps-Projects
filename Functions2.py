def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficacy")
    if (efficacy < 50):
        print("Discard this Vaccine")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, Needs more trials.")
    elif (efficacy > 75) and (efficacy <= 90):
        print("Can consider this vaccine.")
    elif(efficacy >= 90):
        print("Vaccine is safe to be supplied.")
    else:
        print("Needs a lot more trials.")

vac_feedback("Pfizer", 95)
vac_feedback("Moderna", 80)
vac_feedback("Sinovac", 75)
vac_feedback("AstraZeneca", 50)
vac_feedback(efficacy=35, vac="unknown")