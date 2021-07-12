import math
import time

base = int(input("base: ")or 0)
hypo= int(input("hypo: ") or 0)
perp = int(input("prep: ") or 0)

if hypo== 0:
    hypo= math.sqrt((base**2) + (perp**2))
    print("")
    time.sleep(0.1)
    print("Hypo: " + str(hypo))


if perp == 0:
    perp = math.sqrt((hypo**2) - (base**2))
    print("")
    time.sleep(0.1)
    print("Perp: " + str(perp))


if base == 0:
    base = math.sqrt((hypo**2) - (perp**2))
    print("")
    time.sleep(0.1)
    print("Base: " + str(base))


print(" ")
print("Getting results.......")
time.sleep(0.1)
print(f"Sine A: {base}/{hypo}")
time.sleep(0.1)
print(f"Cos A : {perp}/{hypo}")
time.sleep(0.1)
print(f"Tan A: {perp}/{base}")
time.sleep(0.1)
print(f"Consecant A {hypo}/{perp}")
time.sleep(0.1)
print(f"Secant A {hypo}/ {base}")
time.sleep(0.1)
print(f"Cotangent A {base}/{perp}")
