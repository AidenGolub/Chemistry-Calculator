import math
import decimal
import sys
import time
import re
z=True
print("Made by Aiden Golub")
#Version: 2.2 (4/1/2021)
#Version: 2.3 (4/21/2021) [Latest]
onexone = (
	"""
	R1[C1]
	"""
)
onextwo = (
	"""
	R1[C1][C2]
	"""
)
onexthree = (
	"""
	R1[C1][C2][C3]
	"""
)
twoxthree = (
	"""
	R1[C1][C2][C3]
	R2[C1][C2][C3]
	"""
)
twoxtwo = (
	"""
	R1[C1][C2]
	R2[C1][C2]
	"""
)
twoxone = (
	"""
	R1[C1]
	R2[C1]
	"""
)
threextwo = (
	"""
	R1[C1][C2]
	R2[C1][C2]
	R3[C1][C2]
	"""
)
threexone = (
	"""
	R1[C1]
	R2[C1]
	R3[C1]
	"""
)
threexthree = (
	"""
	R1[C1][C2][C3]
	R2[C1][C2][C3]
	R3[C1][C2][C3]
	"""
)
onexfour = (
	"""
	R1[C1][C2][C3][C4]
	"""
)
twoxfour = (
	"""
	R1[C1][C2][C3][C4]
	R2[C1][C2][C3][C4]
	"""
)
threexfour = (
	"""
	R1[C1][C2][C3][C4]
	R2[C1][C2][C3][C4]
	R3[C1][C2][C3][C4]
	"""
)
fourxfour = (
	"""
	R1[C1][C2][C3][C4]
	R2[C1][C2][C3][C4]
	R3[C1][C2][C3][C4]
	R4[C1][C2][C3][C4]
	"""
)
fourxone = (
	"""
	R1[C1]
	R2[C1]
	R3[C1]
	R4[C1]
	"""
)
fourxtwo = (
	"""
	R1[C1][C2]
	R2[C1][C2]
	R3[C1][C2]
	R4[C1][C2]
	"""
)
fourxthree = (
	"""
	R1[C1][C2][C3]
	R2[C1][C2][C3]
	R3[C1][C2][C3]
	R4[C1][C2][C3]
	"""
)
while z is True:
	def again_Time():
		again = input("Do you want to calculate again? Y or N: ").lower()
		if again =="y":
			print("")
			print("")
			print("")
			print("")
			print("")
			print("")
			print("")
			z=True
		elif again =="n":
			z=False
			sys.exit()
		elif again =="":
			z=False
			sys.exit()
		else:
			z=False
			sys.exit()
	output = 0
	actionList=["a", "s", "m", "d", "ma", "g", "c", "gc", "exit"]
	Matrix1_sizeList=["1x1", "1x2", "1x3", "2x3", "2x2", "2x1", "3x1","3x2", "3x3", "1x4", "2x4", "3x4", "4x4", "4x1", "4x2", "4x3"]
	print("")
	print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
	print("")
	print("Add(A)   Subtract(S)   Multiply(M)   Divide(D)   Matrices(MA)   Geometry(G)   Chemistry(C)   (exit)")
	print("")
	print("Grade Calculations (GC)")
	print("")
	print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
	print("")
	calculator_machine = input("What action would you like to do?: ").lower()
	print("")
	if calculator_machine not in actionList:
		sys.exit()
	if calculator_machine =="exit":
		sys.exit()
	elif calculator_machine =="gc":
		print("________________________________________________________________________________________________________")
		# x (percentage: input) / 100 * z (points in assignment: input) = answer
		x=input("What percentage do you want?: ")
		z=input("How many points are in the assignment?: ")
		answer = (float(x)/100)*float(z)
		print("______________________________")
		print("Final Grade:")
		print(str(answer))
		print("______________________________")
		again_Time()
	elif calculator_machine =="c":
		Hydrogen =	{
		  "atomicNO": 1,
		  "atomicWeight": 1.008,
		  "electronConfig": "1s1",
		  "valElectrons": 1,
		  "Type": "Non-Metal",
		  "elementSymbol": "H",
		  "density": 0.0899, #g/l
		  "meltingPoint": "-259.14°C",
		  "boilingPoint": "-252.87°C"
		}
		Helium =	{
		  "atomicNO": 2,
		  "atomicWeight": 4.0026,
		  "electronConfig": "1s2",
		  "valElectrons": 2,
		  "Type": "Noble Gas",
		  "elementSymbol" : "He",
		  "density": 0.1785, #g/l
		  "meltingPoint": "-272.2°C",
		  "boilingPoint": "-268.93°C"
		}
		Lithium =	{
		  "atomicNO": 3,
		  "atomicWeight": 6.94,
		  "electronConfig": "[He]2s1",
		  "valElectrons": 1,
		  "Type": "Alkali Metal",
		  "elementSymbol": "Li",
		  "density": 0.535, #g/cm3
		  "meltingPoint": "180.54°C",
		  "boilingPoint": "1342°C"
		}
		Beryllium =	{
		  "atomicNO": 4,
		  "atomicWeight": 9.0122,
		  "electronConfig": "[He]2s2",
		  "valElectrons": 2,
		  "Type": "Alkaline Earth Metal",
		  "elementSymbol": "Be",
		  "density": 1.848, #g/cm3
		  "meltingPoint": "1287°C",
		  "boilingPoint": "2470°C"
		}
		Boron =	{
		  "atomicNO": 5,
		  "atomicWeight": 10.81,
		  "electronConfig": "[He]2s22p1",
		  "valElectrons": 3,
		  "Type": "Metalloid",
		  "elementSymbol": "B",
		  "density": 2.46, #g/cm3
		  "meltingPoint": "2075°C",
		  "boilingPoint": "4000°C"
		}
		Carbon =	{
		  "atomicNO": 6,
		  "atomicWeight": 12.011,
		  "electronConfig": "[He]2s22p2",
		  "valElectrons": 4,
		  "Type": "Non-Metal",
		  "elementSymbol": "C",
		  "density": 2.26, #g/cm3
		  "meltingPoint": "3550°C",
		  "boilingPoint": "3825°C"
		}
		Nitrogen =	{
		  "atomicNO": 7,
		  "atomicWeight": 14.007,
		  "electronConfig": "[He]2s22p3",
		  "valElectrons": 5,
		  "Type": "Non-Metal",
		  "elementSymbol": "N",
		  "density": 1.251, #g/l
		  "meltingPoint": "-210.1°C",
		  "boilingPoint": "-195.79°C"
		}
		Oxygen =	{
		  "atomicNO": 8,
		  "atomicWeight": 15.999,
		  "electronConfig": "[He]2s22p4",
		  "valElectrons": 6,
		  "Type": "Non-Metal",
		  "elementSymbol": "O",
		  "density": 1.429, #g/l
		  "meltingPoint": "-218.3°C",
		  "boilingPoint": "-182.9°C"
		}
		Fluorine =	{
		  "atomicNO": 9,
		  "atomicWeight": 18.998,
		  "electronConfig": "[He]2s22p5",
		  "valElectrons": 7,
		  "Type": "Non-Metal",
		  "elementSymbol": "F",
		  "density": 1.696, #g/l
		  "meltingPoint": "-219.6°C",
		  "boilingPoint": "-188.12°C"
		}
		Neon =	{
		  "atomicNO": 10,
		  "atomicWeight": 20.180,
		  "electronConfig": "[He]2s22p6",
		  "valElectrons": 8,
		  "Type": "Noble Gas",
		  "elementSymbol": "Ne",
		  "density": 0.9, #g/l
		  "meltingPoint": "-248.59°C",
		  "boilingPoint": "-246.08°C"
		}
		Sodium =	{
		  "atomicNO": 11,
		  "atomicWeight": 22.990,
		  "electronConfig": "[Ne]3s1",
		  "valElectrons": 1,
		  "Type": "Alkali Metal",
		  "elementSymbol": "Na",
		  "density": 0.968, #g/cm3
		  "meltingPoint": "-259.14°C",
		  "boilingPoint": "-252.87°C"
		}
		Magnesium =	{
		  "atomicNO": 12,
		  "atomicWeight": 24.305,
		  "electronConfig": "[Ne]3s2",
		  "valElectrons": 2,
		  "Type": "Alkaline Earth Metal",
		  "elementSymbol": "Mg",
		  "density": 1.738, #g/cm3
		  "meltingPoint": "650°C",
		  "boilingPoint": "1090°C"
		}
		Aluminum =	{
		  "atomicNO": 13,
		  "atomicWeight": 26.982,
		  "electronConfig": "[Ne]3s23p1",
		  "valElectrons": 3,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Al",
		  "density": 2.7, #g/cm3(ml)
		  "meltingPoint": "660.32°C",
		  "boilingPoint": "-2519°C"
		}
		Silicon =	{
		  "atomicNO": 14,
		  "atomicWeight": 28.085,
		  "electronConfig": "[Ne]3s23p2",
		  "valElectrons": 4,
		  "Type": "Metalloid",
		  "elementSymbol": "Si",
		  "density": 2.33, #g/cm3(ml)
		  "meltingPoint": "1414°C",
		  "boilingPoint": "2900°C"
		}
		Phosphorus =	{
		  "atomicNO": 15,
		  "atomicWeight": 30.974,
		  "electronConfig": "[Ne]3s23p3",
		  "valElectrons": 5,
		  "Type": "Non-Metal",
		  "elementSymbol": "P",
		  "density": 1.823, #g/cm3(ml)
		  "meltingPoint": "44.2°C",
		  "boilingPoint": "280.5°C"
		}
		Sulfur =	{
		  "atomicNO": 16,
		  "atomicWeight": 32.06,
		  "electronConfig": "[Ne]3s23p4",
		  "valElectrons": 6,
		  "Type": "Non-Metal",
		  "elementSymbol": "S",
		  "density": 1.96, #g/cm3(ml)
		  "meltingPoint": "115.21",
		  "boilingPoint": "444.72°C"
		}
		Chlorine =	{
		  "atomicNO": 17,
		  "atomicWeight": 35.45,
		  "electronConfig": "[Ne]3s23p5",
		  "valElectrons": 7,
		  "Type": "Non-Metal",
		  "elementSymbol": "Cl",
		  "density": 3.214, #g/l
		  "meltingPoint": "-101.5°C",
		  "boilingPoint": "-34.04°C"
		}
		Argon =	{
		  "atomicNO": 18,
		  "atomicWeight": 39.948,
		  "electronConfig": "[Ne]3s23p6",
		  "valElectrons": 8,
		  "Type": "Noble Gas",
		  "elementSymbol": "Ar",
		  "density": 1.784, #g/l
		  "meltingPoint": "-189.3°C",
		  "boilingPoint": "-185.8°C"
		}
		Potassium =	{
		  "atomicNO": 19,
		  "atomicWeight": 39.098,
		  "electronConfig": "[Ar]4s1",
		  "valElectrons": 1,
		  "Type": "Alkali Metal",
		  "elementSymbol": "K",
		  "density": 0.856, #g/cm3(ml)
		  "meltingPoint": "63.38°C",
		  "boilingPoint": "759°C"
		}
		Calcium =	{
		  "atomicNO": 20,
		  "atomicWeight": 40.078,
		  "electronConfig": "[Ar]4s2",
		  "valElectrons": 2,
		  "Type": "Alkaline Earth Metal",
		  "elementSymbol": "Ca",
		  "density": 1.55, #g/cm3(ml)
		  "meltingPoint": "842°C",
		  "boilingPoint": "1484°C"
		}
		Scandium =	{
		  "atomicNO": 21,
		  "atomicWeight": 44.956,
		  "electronConfig": "[Ar]4s23d1",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Sc",
		  "density": 2.985, #g/cm3(ml)
		  "meltingPoint": "1541°C",
		  "boilingPoint": "2830°C"
		}
		Titanium =	{
		  "atomicNO": 22,
		  "atomicWeight": 47.867,
		  "electronConfig": "[Ar]4s23d2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Ti",
		  "density": 4.507, #g/cm3(ml)
		  "meltingPoint": "1668°C",
		  "boilingPoint": "3287°C"
		}
		Vanadium =	{
		  "atomicNO": 23,
		  "atomicWeight": 50.942,
		  "electronConfig": "[Ar]4s23d3",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "V",
		  "density": 6.11, #g/cm3(ml)
		  "meltingPoint": "1910°C",
		  "boilingPoint": "3407°C"
		}
		Chromium =	{
		  "atomicNO": 24,
		  "atomicWeight": 51.996,
		  "electronConfig": "[Ar]4s13d5",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Cr",
		  "density": 7.19, #g/cm3(ml)
		  "meltingPoint": "1907°C",
		  "boilingPoint": "2671°C"
		}
		Manganese =	{
		  "atomicNO": 25,
		  "atomicWeight": 54.938,
		  "electronConfig": "[Ar]4s23d5",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Mn",
		  "density": 7.47, #g/cm3(ml)
		  "meltingPoint": "1246°C",
		  "boilingPoint": "2061°C"
		}
		Iron =	{
		  "atomicNO": 26,
		  "atomicWeight": 55.845,
		  "electronConfig": "[Ar]4s23d6",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Fe",
		  "density": 7.874, #g/cm3(ml)
		  "meltingPoint": "1538°C",
		  "boilingPoint": "2861°C"
		}
		Cobalt =	{
		  "atomicNO": 27,
		  "atomicWeight": 58.933,
		  "electronConfig": "[Ar]4s23d7",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Co",
		  "density": 8.9, #g/cm3(ml)
		  "meltingPoint": "1495°C",
		  "boilingPoint": "2927°C"
		}
		Nickel =	{
		  "atomicNO": 28,
		  "atomicWeight": 58.693,
		  "electronConfig": "[Ar]4s23d8",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Ni",
		  "density": 8.908, #g/cm3(ml)
		  "meltingPoint": "1455°C",
		  "boilingPoint": "2913°C"
		}
		Copper =	{
		  "atomicNO": 29,
		  "atomicWeight": 63.546,
		  "electronConfig": "[Ar]4s13d10",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Cu",
		  "density": 8.96, #g/cm3(ml)
		  "meltingPoint": "1084.62°C",
		  "boilingPoint": "2562°C"
		}
		Zinc =	{
		  "atomicNO": 30,
		  "atomicWeight": 65.38,
		  "electronConfig": "[Ar]4s23d10",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Zn",
		  "density": 7.14, #g/cm3(ml)
		  "meltingPoint": "419.53°C",
		  "boilingPoint": "907°C"
		}
		Gallium =	{
		  "atomicNO": 31,
		  "atomicWeight": 69.723,
		  "electronConfig": "[Ar]4s23d104p1",
		  "valElectrons": 3,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Ga",
		  "density": 5.904, #g/cm3(ml)
		  "meltingPoint": "29.76°C",
		  "boilingPoint": "2204°C"
		}
		Germanium =	{
		  "atomicNO": 32,
		  "atomicWeight": 72.630,
		  "electronConfig": "[Ar]4s23d104p2",
		  "valElectrons": 4,
		  "Type": "Metalloid",
		  "elementSymbol": "Ge",
		  "density": 5.323, #g/cm3(ml)
		  "meltingPoint": "938.3°C",
		  "boilingPoint": "2820°C"
		}
		Arsenic =	{
		  "atomicNO": 33,
		  "atomicWeight": 74.922,
		  "electronConfig": "[Ar]4s23d104p3",
		  "valElectrons": 5,
		  "Type": "Metalloid",
		  "elementSymbol": "As",
		  "density": 5.727, #g/cm3(ml)
		  "meltingPoint": "817°C",
		  "boilingPoint": "614°C"
		}
		Selenium =	{
		  "atomicNO": 34,
		  "atomicWeight": 78.971,
		  "electronConfig": "[Ar]4s23d104p4",
		  "valElectrons": 6,
		  "Type": "Non-Metal",
		  "elementSymbol": "Se",
		  "density": 4.819, #g/cm3(ml)
		  "meltingPoint": "221°C",
		  "boilingPoint": "685°C"
		}
		Bromine =	{
		  "atomicNO": 35,
		  "atomicWeight": 79.904,
		  "electronConfig": "[Ar]4s23d104p5",
		  "valElectrons": 7,
		  "Type": "Non-Metal",
		  "elementSymbol": "Br",
		  "density": 3.12, #g/cm3(ml)
		  "meltingPoint": "-7.3°C",
		  "boilingPoint": "59°C"
		}
		Krypton =	{
		  "atomicNO": 36,
		  "atomicWeight": 83.798,
		  "electronConfig": "[Ar]4s23d104p6",
		  "valElectrons": 8,
		  "Type": "Noble Gas",
		  "elementSymbol": "Kr",
		  "density": 3.75, #g/l
		  "meltingPoint": "-157.36°C",
		  "boilingPoint": "-153.22°C"
		}
		Rubidium =	{
		  "atomicNO": 37,
		  "atomicWeight": 85.468,
		  "electronConfig": "[Kr]5s1",
		  "valElectrons": 1,
		  "Type": "Alkali Metal",
		  "elementSymbol": "Rb",
		  "density": 1.532, #g/cm3(ml)
		  "meltingPoint": "39.31°C",
		  "boilingPoint": "688°C"
		}
		Strontium =	{
		  "atomicNO": 38,
		  "atomicWeight": 87.62,
		  "electronConfig": "[Kr]5s2",
		  "valElectrons": 2,
		  "Type": "Alkaline Earth Metal",
		  "elementSymbol": "Sr",
		  "density": 2.63, #g/cm3(ml)
		  "meltingPoint": "777°C",
		  "boilingPoint": "1382°C"
		}
		Yttrium =	{
		  "atomicNO": 39,
		  "atomicWeight": 88.906,
		  "electronConfig": "[Kr]5s24d1",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Y",
		  "density": 4.472, #g/cm3(ml)
		  "meltingPoint": "1526°C",
		  "boilingPoint": "3345°C"
		}
		Zirconium =	{
		  "atomicNO": 40,
		  "atomicWeight": 91.224,
		  "electronConfig": "[Kr]5s24d2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Zr",
		  "density": 6.511, #g/cm3(ml)
		  "meltingPoint": "1855°C",
		  "boilingPoint": "4409°C"
		}
		Niobium =	{
		  "atomicNO": 41,
		  "atomicWeight": 92.906,
		  "electronConfig": "[Kr]5s14d4",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Nb",
		  "density": 8.57, #g/cm3(ml)
		  "meltingPoint": "2477°C",
		  "boilingPoint": "4744°C"
		}
		Molybdenur =	{
		  "atomicNO": 42,
		  "atomicWeight": 95.95,
		  "electronConfig": "[Kr]5s14d5",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Mo",
		  "density": 10.28, #g/cm3(ml)
		  "meltingPoint": "2623°C",
		  "boilingPoint": "4639°C"
		}
		Technetium =	{
		  "atomicNO": 43,
		  "atomicWeight": 98,
		  "electronConfig": "[Kr]5s24d5",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Tc",
		  "density": 11.5, #g/cm3(ml)
		  "meltingPoint": "2157°C",
		  "boilingPoint": "4265°C"
		}
		Ruthenium =	{
		  "atomicNO": 44,
		  "atomicWeight": 101.07,
		  "electronConfig": "[Kr]5s14d7",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Ru",
		  "density": 12.37, #g/cm3(ml)
		  "meltingPoint": "2334°C",
		  "boilingPoint": "4150°C"
		}
		Rhodium =	{
		  "atomicNO": 45,
		  "atomicWeight": 102.91,
		  "electronConfig": "[Kr]5s14d8",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Rh",
		  "density": 12.45, #g/cm3(ml)
		  "meltingPoint": "1964°C",
		  "boilingPoint": "3695°C"
		}
		Palladium =	{
		  "atomicNO": 46,
		  "atomicWeight": 106.42,
		  "electronConfig": "[Kr]4d10",
		  "valElectrons": 10,
		  "Type": "Transition Metal",
		  "elementSymbol": "Pd",
		  "density": 12.023, #g/cm3(ml)
		  "meltingPoint": "1554.9°C",
		  "boilingPoint": "2963°C"
		}
		Silver =	{
		  "atomicNO": 47,
		  "atomicWeight": 107.87,
		  "electronConfig": "[Kr]5s14d10",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Ag",
		  "density": 10.49, #g/cm3(ml)
		  "meltingPoint": "961.78°C",
		  "boilingPoint": "2162°C"
		}
		Cadmium =	{
		  "atomicNO": 48,
		  "atomicWeight": 112.41,
		  "electronConfig": "[Kr]5s24d10",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Cd",
		  "density": 8.56, #g/cm3(ml)
		  "meltingPoint": "321.07°C",
		  "boilingPoint": "767°C"
		}
		Indium =	{
		  "atomicNO": 49,
		  "atomicWeight": 114.82,
		  "electronConfig": "[Kr]5s24d105p1",
		  "valElectrons": 3,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "In",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "156.6°C",
		  "boilingPoint": "2072°C"
		}
		Tin =	{
		  "atomicNO": 50,
		  "atomicWeight": 118.71,
		  "electronConfig": "[Kr]5s24d105p2",
		  "valElectrons": 4,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Sn",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Antimony =	{
		  "atomicNO": 51,
		  "atomicWeight": 121.76,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 5,
		  "Type": "Metalloid",
		  "elementSymbol": "Sb",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Tellurium =	{
		  "atomicNO": 52,
		  "atomicWeight": 127.60,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 6,
		  "Type": "Metalloid",
		  "elementSymbol": "Te",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Iodine =	{
		  "atomicNO": 53,
		  "atomicWeight": 126.90,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 7,
		  "Type": "Non-Metal",
		  "elementSymbol": "I",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Xenon =	{
		  "atomicNO": 54,
		  "atomicWeight": 131.29,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 8,
		  "Type": "Noble Gas",
		  "elementSymbol": "Xe",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Caesium =	{
		  "atomicNO": 55,
		  "atomicWeight": 132.91,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 1,
		  "Type": "Alkali Metal",
		  "elementSymbol": "Cs",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Barium =	{
		  "atomicNO": 56,
		  "atomicWeight": 137.33,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Alkaline Earth Metal",
		  "elementSymbol": "Ba",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Lanthanum =	{
		  "atomicNO": 57,
		  "atomicWeight": 138.91,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "La",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Cerium =	{
		  "atomicNO": 58,
		  "atomicWeight": 140.12,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Ce",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Praseodymium =	{
		  "atomicNO": 59,
		  "atomicWeight": 140.91,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Pr",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Neodymium =	{
		  "atomicNO": 60,
		  "atomicWeight": 144.24,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Nd",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Promethium =	{
		  "atomicNO": 61,
		  "atomicWeight": 145,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Pm",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Samarium =	{
		  "atomicNO": 62,
		  "atomicWeight": 150.36,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Sm",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Europium =	{
		  "atomicNO": 63,
		  "atomicWeight": 151.96,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Eu",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Gadolinium =	{
		  "atomicNO": 64,
		  "atomicWeight": 157.25,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Gd",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Terbium =	{
		  "atomicNO": 65,
		  "atomicWeight": 158.93,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Tb",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Dysprosium =	{
		  "atomicNO": 66,
		  "atomicWeight": 162.50,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Dy",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Holmium =	{
		  "atomicNO": 67,
		  "atomicWeight": 164.93,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Ho",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Erbium =	{
		  "atomicNO": 68,
		  "atomicWeight": 167.26,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Er",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Thulium =	{
		  "atomicNO": 69,
		  "atomicWeight": 168.93,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Tm",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Ytterbium =	{
		  "atomicNO": 70,
		  "atomicWeight": 173.05,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Yb",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Lutetium =	{
		  "atomicNO": 71,
		  "atomicWeight": 174.97,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Lanthanoid",
		  "elementSymbol": "Lu",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Hafnium =	{
		  "atomicNO": 72,
		  "atomicWeight": 178.49,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Hf",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Tantalum =	{
		  "atomicNO": 73,
		  "atomicWeight": 180.95,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Ta",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Tungsten =	{
		  "atomicNO": 74,
		  "atomicWeight": 183.84,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "W",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Rhenium =	{
		  "atomicNO": 75,
		  "atomicWeight": 186.21,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Re",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Osmium =	{
		  "atomicNO": 76,
		  "atomicWeight": 190.23,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Os",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Iridium =	{
		  "atomicNO": 77,
		  "atomicWeight": 192.22,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Ir",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Platinum =	{
		  "atomicNO": 78,
		  "atomicWeight": 195.08,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Pt",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Gold =	{
		  "atomicNO": 79,
		  "atomicWeight": 196.97,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Au",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Mercury =	{
		  "atomicNO": 80,
		  "atomicWeight": 200.59,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Hg",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Thallium =	{
		  "atomicNO": 81,
		  "atomicWeight": 204.38,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 3,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Tl",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Lead =	{
		  "atomicNO": 82,
		  "atomicWeight": 207.2,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 4,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Pb",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Bismuth =	{
		  "atomicNO": 83,
		  "atomicWeight": 208.98,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 5,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Bi",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Polonium =	{
		  "atomicNO": 84,
		  "atomicWeight": 209,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 6,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Po",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Astatine =	{
		  "atomicNO": 85,
		  "atomicWeight": 210,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 7,
		  "Type": "Metalloid",
		  "elementSymbol": "At",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Radon =	{
		  "atomicNO": 86,
		  "atomicWeight": 222,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 8,
		  "Type": "Noble Gas",
		  "elementSymbol": "Rn",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Francium =	{
		  "atomicNO": 87,
		  "atomicWeight": 223,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 1,
		  "Type": "Alkali Metal",
		  "elementSymbol": "Fr",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Radium =	{
		  "atomicNO": 88,
		  "atomicWeight": 226,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Alkaline Earth Metal",
		  "elementSymbol": "Ra",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Actinium =	{
		  "atomicNO": 89,
		  "atomicWeight": 227,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Ac",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Thorium =	{
		  "atomicNO": 90,
		  "atomicWeight": 232.04,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Th",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Protactinium =	{
		  "atomicNO": 91,
		  "atomicWeight": 231.04,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Pa",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Uranium =	{
		  "atomicNO": 92,
		  "atomicWeight": 238.03,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "U",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Neptunium =	{
		  "atomicNO": 93,
		  "atomicWeight": 237,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Np",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Plutonium =	{
		  "atomicNO": 94,
		  "atomicWeight": 244,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Pu",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Americium =	{
		  "atomicNO": 95,
		  "atomicWeight": 243,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Am",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Curium =	{
		  "atomicNO": 96,
		  "atomicWeight": 247,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Cm",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Berkelium =	{
		  "atomicNO": 97,
		  "atomicWeight": 247,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Bk",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Californium =	{
		  "atomicNO": 98,
		  "atomicWeight": 251,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Cf",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Einsteinium =	{
		  "atomicNO": 99,
		  "atomicWeight": 252,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Es",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Fermium =	{
		  "atomicNO": 100,
		  "atomicWeight": 257,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Fm",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Mendelevium =	{
		  "atomicNO": 101,
		  "atomicWeight": 258,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "Md",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Nobelium =	{
		  "atomicNO": 102,
		  "atomicWeight": 259,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Actinoid",
		  "elementSymbol": "No",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Lawrencium =	{
		  "atomicNO": 103,
		  "atomicWeight": 266,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 3,
		  "Type": "Actinoid",
		  "elementSymbol": "Lr",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Rutherfordium =	{
		  "atomicNO": 104,
		  "atomicWeight": 267,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Rf",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Dubnium =	{
		  "atomicNO": 105,
		  "atomicWeight": 268,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Db",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Seaborgium =	{
		  "atomicNO": 106,
		  "atomicWeight": 269,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Sg",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Bohrium =	{
		  "atomicNO": 107,
		  "atomicWeight": 270,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Bh",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Hassium =	{
		  "atomicNO": 108,
		  "atomicWeight": 277,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Hs",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Meitnerium =	{
		  "atomicNO": 109,
		  "atomicWeight": 278,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Mt",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Darmstadtium =	{
		  "atomicNO": 110,
		  "atomicWeight": 281,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 1,
		  "Type": "Transition Metal",
		  "elementSymbol": "Ds",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Roentgenium =	{
		  "atomicNO": 111,
		  "atomicWeight": 282,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Rg",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Copernicium =	{
		  "atomicNO": 112,
		  "atomicWeight": 285,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 2,
		  "Type": "Transition Metal",
		  "elementSymbol": "Cn",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Nihonium =	{
		  "atomicNO": 113,
		  "atomicWeight": 286,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 3,
		  "Type": "N/A",
		  "elementSymbol": "Nh",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Flerovium =	{
		  "atomicNO": 114,
		  "atomicWeight": 289,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 4,
		  "Type": "Post-Transition Metal",
		  "elementSymbol": "Fl",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Moscovium =	{
		  "atomicNO": 115,
		  "atomicWeight": 290,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 5,
		  "Type": "N/A",
		  "elementSymbol": "Mc",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Livermorium =	{
		  "atomicNO": 116,
		  "atomicWeight": 293,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 6,
		  "Type": "N/A",
		  "elementSymbol": "Lv",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Tennessine =	{
		  "atomicNO": 117,
		  "atomicWeight": 294,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 7,
		  "Type": "N/A",
		  "elementSymbol": "Ts",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		Oganesson =	{
		  "atomicNO": 118,
		  "atomicWeight": 294,
		  "electronConfig": "5s24d105p2",
		  "valElectrons": 8,
		  "Type": "N/A",
		  "elementSymbol": "Og",
		  "density": 7.31, #g/cm3(ml)
		  "meltingPoint": "231.93°C",
		  "boilingPoint": "2602°C"
		}
		H=1.008
		He=4.0026
		Li=6.94
		Be=9.0122
		B=10.81
		C=12.011
		N=14.007
		O=15.999
		F=18.998
		Ne=20.180
		Na=22.990
		Mg=24.305
		Al=26.982
		Si=28.085
		P=30.974
		S=32.06
		Cl=35.45
		Ar=39.98
		K=39.098
		Ca=40.078
		Sc=44.956
		Ti=47.867
		V=50.942
		Cr=51.996
		Mn=54.938
		Fe=55.845
		Co=58.993
		Ni=58.693
		Cu=63.546
		Zn=65.38
		Ga=69.723
		Ge=72.630
		As=74.992
		Se=78.971
		Br=79.904
		Kr=83.798
		Rb=85.468
		Sr=87.62
		Y=88.906
		Zr=91.224
		Nb=92.906
		Mo=95.95
		Tc=98
		Ru=101.07
		Rh=102.91
		Pd=106.42
		Ag=107.87
		Cd=112.41
		In=114.82
		Sn=118.71
		Sb=121.76
		Te=127.60
		I=126.90
		Xe=131.29
		Cs=132.91
		Ba=137.33
		La=138.91
		Ce=140.12
		Pr=140.91
		Nd=144.24
		Pm=145
		Sm=150.36
		Eu=151.96
		Gd=157.25
		Tb=158.93
		Dy=162.50
		Ho=164.93
		Er=167.26
		Tm=168.93
		Yb=173.05
		Lu=174.97
		Hf=178.49
		Ta=180.95
		W=183.84
		Re=186.21
		Os=190.23
		Ir=192.22
		Pt=195.08
		Au=196.97
		Hg=200.59
		Tl=204.38
		Pb=207.2
		Bi=208.98
		Po=209
		At=210
		Rn=222
		Fr=223
		Ra=226
		Ac=227
		Th=232.04
		Pa=231.04
		U=238.03
		Np=237
		Pu=244
		Am=243
		Cm=247
		Bk=247
		Cf=251
		Es=252
		Fm=257
		Md=258
		No=259
		Lr=266
		Rf=267
		Db=268
		Sg=269
		Bh=270
		Hs=277
		Mt=278
		Ds=281
		Rg=282
		Cn=285
		Nh=286
		Fl=289
		Mc=290
		Lv=293
		Ts=294
		Og=294
		Save1 = []
		Save2 = []
		Save3 = []
		Save4 = []
		Save5 = []
		Save6 = []
		Save7 = []
		Save8 = []
		Save9 = []
		Save10 = []
		chem = True
		while chem is True:
			print("")	
			print("")
			print("")
			print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			print("")
			print("Lim/Ex/Mol(M)   EF/MF(FM)   Ideal Gas Law(I)   Element Index(EI)   Main Menu(MM)                 (Exit)")
			print("")
			print("pH/pOH(P)   Percent Composition(PC)   Mol/Mass(OS)   Pressure Conversions(PS)                  Saves(S)")
			print("")
			print("Specific Heat Formula(SH)   1/2-life First-Order(HL)   Temperature Conversions(TC)      ([Clear] Saves)")
			print("")
			print("KSP Solubility Products (KS)")
			print("")
			print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			print("")
			chemistry_machine = input("What action would you like to do?: ").lower()
			print("")
			if chemistry_machine == "mm":
				z=True
			if chemistry_machine == "exit":
				sys.exit()
			if chemistry_machine == "clear":
				Save1.clear()
				Save2.clear()
				Save3.clear()
				Save4.clear()
				Save5.clear()
				Save6.clear()
				Save7.clear()
				Save8.clear()
				Save9.clear()
				Save10.clear()
				print("")
				print("(Saves Cleared)")
				time.sleep(.25)
				chem = True
			if chemistry_machine == "s":
				print("")
				print("______________________________")
				print("")
				print("1: ", Save1)
				print("2: ", Save2)
				print("3: ", Save3)
				print("4: ", Save4)
				print("5: ", Save5)
				print("6: ", Save6)
				print("7: ", Save7)
				print("8: ", Save8)
				print("9: ", Save9)
				print("10:", Save10)
				print("______________________________")
			if chemistry_machine == "ks":
				print("________________________________________________________________________________________________________")
				#Solubility Products Dictionary
				questionpo = input("Enter a Primary Element (EX: Al, or Find): ").lower()
				if questionpo == "find":
					print("")
					print("Accepted Elements:")
					print("_________________________________________________________________________________________________")
					print("|	Aluminum(Al)		Chromium(Cr)		Magnesium(Mg)		Silver(Ag)	|")
					print("|	Barium(Ba)		Cobalt(Co)		Manganese(Mn)		Strontium(Sr)	|")
					print("|	Bismuth(Bi)		Copper(Cu)		Mercury(Hg)		Thallium(Tl)    |")
					print("|	Cadmium(Cd)		Iron(Fe)		Nickel(Ni)		Tin(Sn)         |")
					print("|	Calcium(Ca)		Lead(Pb)		Potassium(K)		Zinc(Zn)        |")
					print("_________________________________________________________________________________________________")
				print("")
				if questionpo == "find":
					questionpo = input("Enter a Primary Element: ").lower()
				if questionpo == "al":
					print("")
					print("1:  Al(OH)3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Al(OH)3 = 2e-32"
				elif questionpo == "cr":
					print("")
					print("1:  Cr(OH)3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Cr(OH)3 = 6.7e-31"
				elif questionpo == "mg":
					print("")
					print("1:  Mg(OH)2")
					print("2:  MgCO3~3H2O")
					print("3:  MgNH4PO4")
					print("4:  MgF2")
					print("5:  MgC2O4")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Mg(OH)2 = 8.9e-12"
					elif FSPinput == "2":
						answer = "MgCO3~3H2O = ca1e-5"
					elif FSPinput == "3":
						answer = "MgNH4PO4 = 3e-13"
					elif FSPinput == "4":
						answer = "MgF2 = 6.4e-9"
					elif FSPinput == "5":
						answer = "MgC2O4 = 7e-7"
				elif questionpo == "ag":
					print("")
					print("1:  1/2Ag2O ([Ag^+]+[OH^-])")
					print("2:  AgCl")
					print("3:  AgBr")
					print("4:  AgI")
					print("5:  AgCN")
					print("6:  AgSCN")
					print("7:  Ag2S")
					print("8:  Ag2CO3")
					print("9:  Ag2CrO4")
					print("10: Ag4Fe(CN)6")
					print("11: Ag2SO4")
					print("12: Ag3PO4")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "1/2Ag2O ([Ag^+]+[OH^-]) = 2e-8"
					elif FSPinput == "2":
						answer = "AgCl = 1.6e-10"
					elif FSPinput == "3":
						answer = "AgBr = 5e-13"
					elif FSPinput == "4":
						answer = "AgI = 1.5e-16"
					elif FSPinput == "5":
						answer = "AgCN = 1.2e-16"
					elif FSPinput == "6":
						answer = "AgSCN = 1.0e-12"
					elif FSPinput == "7":
						answer = "Ag2S = 1.6e-49"
					elif FSPinput == "8":
						answer = "Ag2CO3 = 8.1e-12"
					elif FSPinput == "9":
						answer = "Ag2CrO4 = 9.0e-12"
					elif FSPinput == "10":
						answer = "Ag4Fe(CN)6 = 1.55e-41"
					elif FSPinput == "11":
						answer = "Ag2SO4 = 1.2e-5"
					elif FSPinput == "12":
						answer = "Ag3PO4 = 1.8e-18"
				elif questionpo == "ba":
					print("")
					print("1:  BaCO3")
					print("2:  BaC2O4~2H2O")
					print("3:  BaSO4")
					print("4:  BaCrO4")
					print("5:  BaF2")
					print("6:  Ba(OH)2~8H2O")
					print("7:  Ba3(PO4)2")
					print("8:  Ba3(AsO4)2")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "BaCO3 = 1.6e-9"
					elif FSPinput == "2":
						answer = "CaC2O4~2H2O = 1.1e-7"
					elif FSPinput == "3":
						answer = "BaSO4 = 2.3e-8"
					elif FSPinput == "4":
						answer = "BaCrO4 = 8.5e-11"
					elif FSPinput == "5":
						answer = "BaF2 = 2.4e-5"
					elif FSPinput == "6":
						answer = "Ba(OH)2~8H2O = 5.0e-3"
					elif FSPinput == "7":
						answer = "Ba3(PO4)2 = 6e-39"
					elif FSPinput == "8":
						answer = "Ba3(AsO4)2 = 1.1e-13"
				elif questionpo == "co":
					print("")
					print("1:  Co(OH)2")
					print("2:  CoS(α)")
					print("3:  CoS(β)")
					print("4:  CoCO3")
					print("5:  Co(OH)3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Co(OH)2 = 2.5e-16"
					elif FSPinput == "2":
						answer = "CoS(α) = 5e-22"
					elif FSPinput == "3":
						answer = "CoS(β) = 3e-26"
					elif FSPinput == "4":
						answer = "CoCO3 = 1.4e-13"
					elif FSPinput == "5":
						answer = "Co(OH)3 = 2.5e-43"
				elif questionpo == "mn":
					print("")
					print("1:  Mn(OH)2")
					print("2:  MnCO3")
					print("3:  MnS")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Mn(OH)2 = 2e-13"
					elif FSPinput == "2":
						answer = "MnCO3 = 8.8e-11"
					elif FSPinput == "3":
						answer = "MnS = 2.3e-13"
				elif questionpo == "sr":
					print("")
					print("1:  Sr(OH)2~8H2O")
					print("2:  SrCO3")
					print("3:  SrCrO4")
					print("4:  SrSO4")
					print("5:  SrC2O4~H2O")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Sr(OH)2~8H2O = 3.2e-4"
					elif FSPinput == "2":
						answer = "SrCO3 = 7e-10"
					elif FSPinput == "3":
						answer = "SrCrO4 = 3.6e-5"
					elif FSPinput == "4":
						answer = "SrSO4 = 3.2e-7"
					elif FSPinput == "5":
						answer = "SrC2O4~H2O = 4e-7"
				elif questionpo == "bi":
					print("")
					print("1:  BiO(OH)")
					print("2:  BiOCl")
					print("3:  Bi2S3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "BiO(OH) = 4e-10"
					elif FSPinput == "2":
						answer = "BiOCl = 1.8e-31"
					elif FSPinput == "3":
						answer = "Bi2S3 = 1e-97"
				elif questionpo == "cu":
					print("")
					print("1:  CuCl")
					print("2:  CuBr")
					print("3:  CuI")
					print("4:  CuSCN")
					print("5:  Cu2S")
					print("6:  Cu(OH)2")
					print("7:  CuS")
					print("8:  CuCO3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "CuCl = 1.2e-6"
					elif FSPinput == "2":
						answer = "CuBr = 6.27e-9"
					elif FSPinput == "3":
						answer = "CuI = 1.27e-12"
					elif FSPinput == "4":
						answer = "CuSCN = 1.6e-11"
					elif FSPinput == "5":
						answer = "Cu2S = 2.5e-48"
					elif FSPinput == "6":
						answer = "Cu(OH)2 = 2.2e-20"
					elif FSPinput == "7":
						answer = "CuS = 8.5e-45"
					elif FSPinput == "8":
						answer = "CuCO3 = 2.5e-10"
				elif questionpo == "hg":
					print("")
					print("1:  Hg2O~H2O")
					print("2:  Hg2Cl2")
					print("3:  Hg2Br2")
					print("4:  Hg2I2")
					print("5:  Hg2CO3")
					print("6:  Hg2SO4")
					print("7:  Hg2S")
					print("8:  Hg2CrO4")
					print("9:  HgS")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Hg2O~H2O = 3.6e-26"
					elif FSPinput == "2":
						answer = "Hg2Cl2 = 1.1e-18"
					elif FSPinput == "3":
						answer = "Hg2Br2 = 1.3e-22"
					elif FSPinput == "4":
						answer = "Hg2I2 = 4.5e-29"
					elif FSPinput == "5":
						answer = "Hg2CO3 = 9e-15"
					elif FSPinput == "6":
						answer = "Hg2SO4 = 7.4e-7"
					elif FSPinput == "7":
						answer = "Hg2S = 1.0e-47"
					elif FSPinput == "8":
						answer = "Hg2CrO4 = 2e-9"
					elif FSPinput == "9":
						answer = "HgS = 1.6e-54"
				elif questionpo == "tl":
					print("")
					print("1:  TlCl")
					print("2:  TlSCN")
					print("3:  Tl2S")
					print("4:  Tl(OH)3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "TlCl = 1.7e-4"
					elif FSPinput == "2":
						answer = "TlSCN = 1.6e-4"
					elif FSPinput == "3":
						answer = "Tl2S = 6e-22"
					elif FSPinput == "4":
						answer = "Tl(OH)3 = 6.3e-46"
				elif questionpo == "cd":
					print("")
					print("1:  Cd(OH)2")
					print("2:  CdS")
					print("3:  CdCO3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Cd(OH)2 = 5.9e-15"
					elif FSPinput == "2":
						answer = "CdS = 1.0e-28"
					elif FSPinput == "3":
						answer = "CdCO3 = 5.2e-12"
				elif questionpo == "fe":
					print("")
					print("1:  Fe(OH)2")
					print("2:  FeCO3")
					print("3:  FeS")
					print("4:  Fe(OH)3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Fe(OH)2 = 1.8e-15"
					elif FSPinput == "2":
						answer = "FeCO3 = 2.1e-11"
					elif FSPinput == "3":
						answer = "FeS = 3.7e-19"
					elif FSPinput == "4":
						answer = "Fe(OH)3 = 4e-38"
				elif questionpo == "ni":
					print("")
					print("1:  Ni(OH)2")
					print("2:  NiCO3")
					print("3:  NiS(α)")
					print("4:  NiS(β)")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Ni(OH)2 = 1.6e-16"
					elif FSPinput == "2":
						answer = "NiCO3 = 1.4e-7"
					elif FSPinput == "3":
						answer = "NiS(α) = 4e-20"
					elif FSPinput == "4":
						answer = "NiS(β) = 1.3e-25"
				elif questionpo == "sn":
					print("")
					print("1:  Sn(OH)2")
					print("2:  SnS")
					print("3:  Sn(OH)4")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Sn(OH)2 = 3e-27"
					elif FSPinput == "2":
						answer = "SnS = 1e-26"
					elif FSPinput == "3":
						answer = "Sn(OH)4 = 1e-57"
				elif questionpo == "ca":
					print("")
					print("1:  Ca(OH)2")
					print("2:  CaCO3")
					print("3:  CaSO4~2H2O")
					print("4:  CaC2O4~H2O")
					print("5:  Ca3(PO4)2")
					print("6:  CaHPO4")
					print("7:  CaF2")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Ca(OH)2 = 1.3e-6"
					elif FSPinput == "2":
						answer = "CaCO3 = 8.7e-9"
					elif FSPinput == "3":
						answer = "CaSO4~2H2O = 6.1e-5"
					elif FSPinput == "4":
						answer = "CaC2O4~H2O = 1.96e-8"
					elif FSPinput == "5":
						answer = "Ca3(PO4)2 = 1.3e-32"
					elif FSPinput == "6":
						answer = "CaHPO4 = 7e-7"
					elif FSPinput == "7":
						answer = "CaF2 = 5.0e-11"
				elif questionpo == "pb":
					print("")
					print("1:  Pb(OH)2")
					print("2:  PbF2")
					print("3:  PbCl2")
					print("4:  PbBr2")
					print("5:  PbI2")
					print("6:  PbCO3")
					print("7:  PbS")
					print("8:  PbCrO4")
					print("9:  PbSO4")
					print("10: Pb3(PO4)2")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "Pb(OH)2 = 1.2e-15"
					elif FSPinput == "2":
						answer = "PbF2 = 4e-8"
					elif FSPinput == "3":
						answer = "PbCl2 = 1.6e-5"
					elif FSPinput == "4":
						answer = "PbBr2 = 4.6e-6"
					elif FSPinput == "5":
						answer = "PbI2 = 1.4e-8"
					elif FSPinput == "6":
						answer = "PbCO3 = 1.5e-15"
					elif FSPinput == "7":
						answer = "PbS = 7e-29"
					elif FSPinput == "8":
						answer = "PbCrO4= 2e-16"
					elif FSPinput == "9":
						answer = "PbSO4 = 1.3e-8"
					elif FSPinput == "10":
						answer = "Pb3(PO4)2 = 1e-54"
				elif questionpo == "k":
					print("")
					print("1:  KClO4")
					print("2:  K2PtCl6")
					print("3:  KHC4H4O6")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "KClO4 = 1.05e-2"
					elif FSPinput == "2":
						answer = "K2PtCl6 = 7.48e-6"
					elif FSPinput == "3":
						answer = "KHC4H4O6 = 3e-4"
				elif questionpo == "zn":
					print("")
					print("1:  ZnCO3")
					print("")
					FSPinput = input("which number: ")
					if FSPinput == "1":
						answer = "ZnCO3 = 2e-10"
				else:
					print("Wrong Element")
					#End Loop Here
				Unit = "KSP"
				print("")
				print("______________________________")
				print("Final KSP:")
				print(str(answer)+" KSP")
				print("______________________________")
				print("")
				SaveQ = input("Do you want to save the answer? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1
			if chemistry_machine == "tc":
				print("________________________________________________________________________________________________________")
				#Temperature Conversions
				questionpo = input("What Temperature are you Trying to Find (C, K, or F): ").lower()
				if questionpo == "c":
					print("")
					CConverto = input("What is your original Temperature (32+F): ")
					CConverto=CConverto.replace(' ', '').split("+")
					T = CConverto[1].lower()
					if T == "c":
						print("")
						answer = float(CConverto[0])
						Unit = "°C --> (°C)"
						print("______________________________")
						print("Final Temperature (C):")
						print(str(answer)+"°C")
						print("______________________________")	
					if T == "k":
						print("")
						answer = float(CConverto[0])-273.15
						Unit = "°K --> (°C)"
						print("______________________________")
						print("Final Temperature (C):")
						print(str(answer)+"°C")
						print("______________________________")	
					if T == "f":
						print("")
						answer3 = float(CConverto[0])-32
						answer2 = float(answer3)*5
						answer = float(answer2)/9
						Unit = "°F --> (°C)"
						print("______________________________")
						print("Final Temperature (C):")
						print(str(answer)+"°C")
						print("______________________________")
				if questionpo == "k":
					print("")
					KConverto = input("What is your original Temperature (32+F): ")
					KConverto=KConverto.replace(' ', '').split("+")
					T = KConverto[1].lower()
					if T == "c":
						print("")
						answer = float(KConverto[0])+273.15
						Unit = "°C --> (°K)"
						print("______________________________")
						print("Final Temperature (K):")
						print(str(answer)+"°K")
						print("______________________________")	
					if T == "k":
						print("")
						answer = float(KConverto[0])
						Unit = "°K --> (°K)"
						print("______________________________")
						print("Final Temperature (K):")
						print(str(answer)+"°K")
						print("______________________________")	
					if T == "f":
						print("")
						answer4 = float(KConverto[0])-32
						answer3 = float(answer4)*5
						answer2 = float(answer3)/9
						answer = float(answer2)+273.15
						Unit = "°F --> (°K)"
						print("______________________________")
						print("Final Temperature (K):")
						print(str(answer)+"°K")
						print("______________________________")	
				if questionpo == "f":
					print("")
					FConverto = input("What is your original Temperature (32+F): ")
					FConverto=FConverto.replace(' ', '').split("+")
					T = FConverto[1].lower()
					if T == "c":
						print("")
						answer2 = float(FConverto[0])*1/8
						answer = float(answer2)+32
						Unit = "°C --> (°F)"
						print("______________________________")
						print("Final Temperature (F):")
						print(str(answer)+"°F")
						print("______________________________")	
					if T == "k":
						print("")
						answer3 = float(FConverto[0])-273.15
						answer2 = float(answer3)*1.8
						answer = float(answer2)+32
						Unit = "°K --> (°F)"
						print("______________________________")
						print("Final Temperature (F):")
						print(str(answer)+"°F")
						print("______________________________")
					if T == "f":
						print("")
						answer = float(FConverto[0])
						Unit = "°F --> (°F)"
						print("______________________________")
						print("Final Temperature (F):")
						print(str(answer)+"°F")
						print("______________________________")
				print("")
				SaveQ = input("Do you want to save the answer? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1
			if chemistry_machine == "hl":
				print("________________________________________________________________________________________________________")
				#HalfLife Calculator
				question = input("What are you trying to find (t1/2 or k): ").lower()
				print("")
				if question == "t1/2":
					T12A = input("Enter the constant (k): ")
					T12Aanswer = float(0.69)/float(T12A)
					print("")
					print("______________________________")
					print("Final HalfLife:")
					print(str(T12Aanswer))
					print("______________________________")
					answer = T12Aanswer
					Unit = "T1/2"
				if question == "k":
					KA = input("Enter the halflife (t1/2): ")
					KAanswer = float(0.69)/float(KA)
					print("")
					print("______________________________")
					print("Final Constant:")
					print(str(KAanswer))
					print("______________________________")
					answer = KAanswer
					Unit = "K"
				SaveQ = input("Do you want to save the answer? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1
			if chemistry_machine == "sh":
				print("________________________________________________________________________________________________________")
				#Q = MCdelta T calculator (Heat Formula)
				question = input("What are you trying to find? (Q, M, C, TI, TF, or DT): ").lower()
				if question == "q":
					waterList = []
					#Q = (M)(C)(DELTAT)
					print("")
					print("(Heat Selected)")
					print("")
					Mass_Orig = input("Enter the Mass: (+g, +kg, +mg, or +oz): ").lower()
					Mass=Mass_Orig.replace(' ', '').split("+")
					SpecificHeat = input("Enter the Specific Heat: ").lower()
					waterList.append(SpecificHeat)
					if "water" in waterList:
						SpecificHeat = 4.186
					Temperature_Orig = input("Enter the Change in Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					if "water" in waterList:
						Constant = "J"
					if "water" not in waterList:
						Constant = input("What unit of Heat from Specific Heat? (J or KJ): ").upper()
					REPConstant = input("What final unit of Heat (J, KJ, Kcal, or Cal): ").upper()
					#Mass Unit --> g
					if Mass[1] == "g":
						FMass = float(Mass[0])
					if Mass[1] == "kg":
						FMass = float(Mass[0])*1000
					if Mass[1] == "mg":
						FMass = float(Mass[0])/1000
					if Mass[1] == "oz":
						FMass = float(Mass[0])*28.3495
					#Temperature --> C
					if Temperature[1] == "c":
						FTemp = float(Temperature[0])
					if Temperature[1] == "k":
						FTemp = float(Temperature[0])-273.15
					if Temperature[1] == "f":
						FTemp2 = float(Temperature[0])-32
						FTemp1 = float(FTemp2)*5
						FTemp = float(FTemp1)/9
					answer1 = float(FMass)*float(FTemp)
					answer = float(answer1)*float(SpecificHeat)
					if REPConstant == "J":
						if Constant == "J":
							print("")
						if Constant == "KJ":
							answer = float(answer)*1000
							print("")
					if REPConstant == "KJ":
						if Constant == "KJ":
							print("")
						if Constant == "J":
							answer = float(answer)/1000
							print("")
					if REPConstant == "KCAL":
						if Constant == "J":
							answer = float(answer)/4184
							print("")
						if Constant == "KJ":
							answer = float(answer)/4.184
							print("")
						REPConstant="Kcal"
					if REPConstant == "CAL":
						if Constant == "J":
							answer = float(answer)/4.184
							print("")
						if Constant == "KJ":
							answer = float(answer)*238.90296
							print("")
						print("")
						REPConstant="Cal"
					print("______________________________")
					print("Final Heat:")
					print(str(answer), REPConstant)
					print("______________________________")
					print("")
					Unit = REPConstant
				if question == "m":
					print("")
					print("(Mass Selected)")
					print("")
					waterList = []
					#M = Q/CdelatT
					Heat_Orig = input("Enter the Heat (+J, +KJ, +Cal, or +Kcal): ").lower()
					Heat=Heat_Orig.replace(' ', '').split("+")
					SpecificHeat = input("Enter the Specific Heat: ").lower()
					waterList.append(SpecificHeat)
					if "water" in waterList:
						SpecificHeat = 4.186
					Temperature_Orig = input("Enter the Change in Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					if "water" in waterList:
						Constant = "J"
					if "water" not in waterList:
						Constant = input("What unit of Heat from Specific Heat? (J or KJ): ").upper()
					Unit = input("What Final Unit of Mass? (g, kg, mg, or oz): ").lower()
					#Heat --> KJ to J
					if Heat[1] == "kj":
						if Constant == "J":
							Heato = float(Heat[0])*1000
						if Constant == "KJ":
							Heato = float(Heat[0])
					if Heat[1] == "j":
						if Constant == "KJ":
							Heato = float(Heat[0])/1000
						if Constant == "J":
							Heato = float(Heat[0])
					if Heat[1] == "kcal":
						if Constant == "KJ":
							Heato = float(Heat[0])*4.184
						if Constant == "J":
							Heato = float(Heat[0])*4184
					if Heat[1] == "cal":
						if Constant == "KJ":
							Heato = float(Heat[0])/238.90296
						if Constant == "J":
							Heato = float(Heat[0])*4.184
					print("")
					#Temperature --> C
					if Temperature[1] == "c":
						FTemp = float(Temperature[0])
					if Temperature[1] == "k":
						FTemp = float(Temperature[0])-273.15
					if Temperature[1] == "f":
						FTemp2 = float(Temperature[0])-32
						FTemp1 = float(FTemp2)*5
						FTemp = float(FTemp1)/9	
					answer1 = float(SpecificHeat)*float(FTemp)
					answer = float(Heato)/float(answer1)
					if Unit == "g":
						answer = float(answer)
						Unit = "g"
					if Unit == "kg":
						answer = float(answer)/1000
						Unit = "kg"
					if Unit == "mg":
						answer = float(answer)*1000
						Unit = "mg"
					if Unit == "oz":
						answer = float(answer)*0.035274
						Unit = "oz"
					print("______________________________")
					print("Final Mass:")
					print(str(answer), Unit)
					print("______________________________")
					print("")
				if question == "c":
					print("")
					print("(Specific Heat Selected)")
					print("")
					#C = Q/Mdelta T
					Mass_Orig = input("Enter the Mass: (+g, +kg, +mg, or +oz): ").lower()
					Mass=Mass_Orig.replace(' ', '').split("+")
					Heat_Orig = input("Enter the Heat (+J or +KJ): ").lower()
					Heat=Heat_Orig.replace(' ', '').split("+")
					Temperature_Orig = input("Enter the Change in Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					Constant = input("What Final unit of Heat for Specific Heat? (J or KJ): ").upper()
					#Mass Unit --> g
					if Mass[1] == "g":
						FMass = float(Mass[0])
					if Mass[1] == "kg":
						FMass = float(Mass[0])*1000
					if Mass[1] == "mg":
						FMass = float(Mass[0])/1000
					if Mass[1] == "oz":
						FMass = float(Mass[0])*28.3495
					#Temperature --> C
					if Temperature[1] == "c":
						FTemp = float(Temperature[0])
					if Temperature[1] == "k":
						FTemp = float(Temperature[0])-273.15
					if Temperature[1] == "f":
						FTemp2 = float(Temperature[0])-32
						FTemp1 = float(FTemp2)*5
						FTemp = float(FTemp1)/9
					#Heat --> J or KJ
					if Heat[1] == "kj":
						if Constant == "J":
							Heato = float(Heat[0])*1000
						if Constant == "KJ":
							Heato = float(Heat[0])
					if Heat[1] == "j":
						if Constant == "KJ":
							Heato = float(Heat[0])/1000
						if Constant == "J":
							Heato = float(Heat[0])
					if Heat[1] == "kcal":
						if Constant == "KJ":
							Heato = float(Heat[0])*4.184
						if Constant == "J":
							Heato = float(Heat[0])*4184
					if Heat[1] == "cal":
						if Constant == "KJ":
							Heato = float(Heat[0])/238.90296
						if Constant == "J":
							Heato = float(Heat[0])*4.184
					print("")
					answer1 = float(FMass)*float(FTemp)
					answer = float(Heato)/float(answer1)
					if answer == 4.186:
						answer = "Water(l) (4.186)"
					print("______________________________")
					print("Final Specific Heat:")
					print(str(answer), Constant+"/gC")
					print("______________________________")
					print("")
					Unit = Constant+"/gC"
				if question == "ti":
					print("")
					print("(Initial Temperature Selected)")
					print("")
					#(TI) = Q/MC, FT - delta T
					waterList = []
					Mass_Orig = input("Enter the Mass: (+g, +kg, +mg, or +oz): ").lower()
					Mass=Mass_Orig.replace(' ', '').split("+")
					SpecificHeat = input("Enter the Specific Heat: ").lower()
					waterList.append(SpecificHeat)
					if "water" in waterList:
						SpecificHeat = 4.186
					Temperature_Orig = input("Enter the Final Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					if "water" in waterList:
						Constant = "J"
					if "water" not in waterList:
						Constant = input("What unit of Heat from Specific Heat? (J or KJ): ").upper()
					Heat_Orig = input("Enter the Heat (+J or +KJ): ").lower()
					Heat=Heat_Orig.replace(' ', '').split("+")
					Unit = input("Final Temperature Unit (K, C, or F): ").upper()
					#Mass Unit --> g
					if Mass[1] == "g":
						FMass = float(Mass[0])
					if Mass[1] == "kg":
						FMass = float(Mass[0])*1000
					if Mass[1] == "mg":
						FMass = float(Mass[0])/1000
					if Mass[1] == "oz":
						FMass = float(Mass[0])*28.3495
					#Temperature --> C
					if Temperature[1] == "c":
						FTemp = float(Temperature[0])
					if Temperature[1] == "k":
						FTemp = float(Temperature[0])-273.15
					if Temperature[1] == "f":
						FTemp2 = float(Temperature[0])-32
						FTemp1 = float(FTemp2)*5
						FTemp = float(FTemp1)/9
					#Heat --> KJ to J
					if Heat[1] == "kj":
						if Constant == "J":
							Heato = float(Heat[0])*1000
						if Constant == "KJ":
							Heato = float(Heat[0])
					if Heat[1] == "j":
						if Constant == "KJ":
							Heato = float(Heat[0])/1000
						if Constant == "J":
							Heato = float(Heat[0])
					if Heat[1] == "kcal":
						if Constant == "KJ":
							Heato = float(Heat[0])*4.184
						if Constant == "J":
							Heato = float(Heat[0])*4184
					if Heat[1] == "cal":
						if Constant == "KJ":
							Heato = float(Heat[0])/238.90296
						if Constant == "J":
							Heato = float(Heat[0])*4.184
					answer2 = float(FMass)*float(SpecificHeat)
					answer1 = float(Heato)/float(answer2)
					answer = float(FTemp)-float(answer1)
					#answerUnit --> Unit_Input
					if Unit == "K":
						answer = float(answer)+273.15
					if Unit == "C":
						answer = float(answer)
					if Unit == "F":
						FTanswer1 = float(answer)*1.8
						answer = float(FTanswer1)+32
					if answer1 > 0:
						FUnit = "+"
					if answer1 < 0:
						FUnit = ""
					print("")
					print("______________________________")
					print("Initial Temperature:", str(answer), Unit)
					print("")
					print("Delta T:", FUnit + str(answer1), Unit)
					print("______________________________")
					print("")
				if question == "tf":
					print("")
					print("(Final Temperature Selected)")
					print("")
					#(TF) = Q/MC, FI + delta T
					waterList = []
					Mass_Orig = input("Enter the Mass: (+g, +kg, +mg, or +oz): ").lower()
					Mass=Mass_Orig.replace(' ', '').split("+")
					SpecificHeat = input("Enter the Specific Heat: ").lower()
					waterList.append(SpecificHeat)
					if "water" in waterList:
						SpecificHeat = 4.186
					Temperature_Orig = input("Enter the Initial Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					if "water" in waterList:
						Constant = "J"
					if "water" not in waterList:
						Constant = input("What unit of Heat from Specific Heat? (J or KJ): ").upper()
					Heat_Orig = input("Enter the Heat (+J or +KJ): ").lower()
					Heat=Heat_Orig.replace(' ', '').split("+")
					Unit = input("Final Temperature Unit (K, C, or F): ").upper()
					#Mass Unit --> g
					if Mass[1] == "g":
						FMass = float(Mass[0])
					if Mass[1] == "kg":
						FMass = float(Mass[0])*1000
					if Mass[1] == "mg":
						FMass = float(Mass[0])/1000
					if Mass[1] == "oz":
						FMass = float(Mass[0])*28.3495
					#Temperature --> C
					if Temperature[1] == "c":
						FTemp = float(Temperature[0])
					if Temperature[1] == "k":
						FTemp = float(Temperature[0])-273.15
					if Temperature[1] == "f":
						FTemp2 = float(Temperature[0])-32
						FTemp1 = float(FTemp2)*5
						FTemp = float(FTemp1)/9
					#Heat --> KJ to J
					if Heat[1] == "kj":
						if Constant == "J":
							Heato = float(Heat[0])*1000
						if Constant == "KJ":
							Heato = float(Heat[0])
					if Heat[1] == "j":
						if Constant == "KJ":
							Heato = float(Heat[0])/1000
						if Constant == "J":
							Heato = float(Heat[0])
					if Heat[1] == "kcal":
						if Constant == "KJ":
							Heato = float(Heat[0])*4.184
						if Constant == "J":
							Heato = float(Heat[0])*4184
					if Heat[1] == "cal":
						if Constant == "KJ":
							Heato = float(Heat[0])/238.90296
						if Constant == "J":
							Heato = float(Heat[0])*4.184
					answer2 = float(FMass)*float(SpecificHeat)
					answer1 = float(Heato)/float(answer2)
					answer = float(FTemp)+float(answer1)
					#answerUnit --> Unit_Input
					if Unit == "K":
						answer = float(answer)+273.15
					if Unit == "C":
						answer = float(answer)
					if Unit == "F":
						FTanswer1 = float(answer)*1.8
						answer = float(FTanswer1)+32
					if answer1 > 0:
						FUnit = "+"
					if answer1 < 0:
						FUnit = ""
					print("")
					print("______________________________")
					print("Final Temperature:", str(answer), Unit)
					print("")
					print("Delta T:", FUnit + str(answer1), Unit)
					print("______________________________")
					print("")
				if question == "dt":
					print("")
					print("(Change in Temperature Selected)")
					print("")
					#DT = Q/MC
					waterList = []
					Mass_Orig = input("Enter the Mass: (+g, +kg, +mg, or +oz): ").lower()
					Mass=Mass_Orig.replace(' ', '').split("+")
					SpecificHeat = input("Enter the Specific Heat: ").lower()
					waterList.append(SpecificHeat)
					if "water" in waterList:
						SpecificHeat = 4.186
					if "water" in waterList:
						Constant = "J"
					if "water" not in waterList:
						Constant = input("What unit of Heat from Specific Heat? (J or KJ): ").upper()
					Heat_Orig = input("Enter the Heat (+J or +KJ): ").lower()
					Heat=Heat_Orig.replace(' ', '').split("+")
					Unit = input("Final Temperature Unit (K, C, or F): ").upper()
					#Mass Unit --> g
					if Mass[1] == "g":
						FMass = float(Mass[0])
					if Mass[1] == "kg":
						FMass = float(Mass[0])*1000
					if Mass[1] == "mg":
						FMass = float(Mass[0])/1000
					if Mass[1] == "oz":
						FMass = float(Mass[0])*28.3495
					#Heat --> KJ to J
					if Heat[1] == "kj":
						if Constant == "J":
							Heato = float(Heat[0])*1000
						if Constant == "KJ":
							Heato = float(Heat[0])
					if Heat[1] == "j":
						if Constant == "KJ":
							Heato = float(Heat[0])/1000
						if Constant == "J":
							Heato = float(Heat[0])
					if Heat[1] == "kcal":
						if Constant == "KJ":
							Heato = float(Heat[0])*4.184
						if Constant == "J":
							Heato = float(Heat[0])*4184
					if Heat[1] == "cal":
						if Constant == "KJ":
							Heato = float(Heat[0])/238.90296
						if Constant == "J":
							Heato = float(Heat[0])*4.184
					answer2 = float(FMass)*float(SpecificHeat)
					answer = float(Heato)/float(answer2)
					#answerUnit --> Unit_Input
					if Unit == "K":
						answer = float(answer)+273.15
					if Unit == "C":
						answer = float(answer)
					if Unit == "F":
						FTanswer1 = float(answer)*1.8
						answer = float(FTanswer1)+32
					print("")
					print("______________________________")
					print("ΔT:")
					print(str(answer), Unit)
					print("______________________________")
					print("")	
				SaveQ = input("Do you want to save the answer? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1
			if chemistry_machine == "ps":
				print("________________________________________________________________________________________________________")
				questionpo = input("What Pressure are you Trying to Find (atm, KPa, Pa, Torr, mmHg, or Bar): ").lower()
				if questionpo == "bar":
					print("")
					barConverto = input("What is your original Pressure (4.5+KPa): ")
					barConverto=barConverto.replace(' ', '').split("+")
					P = barConverto[1].lower()
					if P == "kpa":
						Unit = "KPa --> (bar)"
						answer = float(barConverto[0])/100
						print("______________________________")
						print("Final Pressure (bar):")
						print(str(answer)+" bar")
						print("______________________________")
					if P == "pa":
						Unit = "Pa --> (bar)"
						answer = float(barConverto[0])/100000
						print("______________________________")
						print("Final Pressure (bar):")
						print(str(answer)+" bar")
						print("______________________________")
					if P == "torr":
						Unit = "torr --> (bar)"
						answer = float(barConverto[0])/750.06156130264
						print("______________________________")
						print("Final Pressure (bar):")
						print(str(answer)+" bar")
						print("______________________________")
					if P == "mmhg":
						Unit = "mmhg --> (bar)"
						answer = float(barConverto[0])/750.06156130264
						print("______________________________")
						print("Final Pressure (bar):")
						print(str(answer)+" bar")
						print("______________________________")
					if P == "atm":
						Unit = "atm --> (bar)"
						answer = float(barConverto[0])*1.01325
						print("______________________________")
						print("Final Pressure (bar):")
						print(str(answer)+" bar")
						print("______________________________")
					if P == "bar":
						Unit = "bar --> (bar)"
						answer = float(barConverto[0])/1
						print("______________________________")
						print("Final Pressure (bar):")
						print(str(answer)+" bar")
						print("______________________________")
				if questionpo == "atm":
					print("")
					atmConverto = input("What is your original Pressure (4.5+KPa): ")
					atmConverto=atmConverto.replace(' ', '').split("+")
					P = atmConverto[1].lower()
					if P == "kpa":
						Unit = "kpa --> (atm)"
						answer = float(atmConverto[0])/101.325
						print("______________________________")
						print("Final Pressure (atm):")
						print(str(answer)+" atm")
						print("______________________________")
					if P == "pa":
						Unit = "Pa --> (atm)"
						answer = float(atmConverto[0])/101325
						print("______________________________")
						print("Final Pressure (atm):")
						print(str(answer)+" atm")
						print("______________________________")
					if P == "torr":
						Unit = "torr --> (atm)"
						answer = float(atmConverto[0])/760
						print("______________________________")
						print("Final Pressure (atm):")
						print(str(answer)+" atm")
						print("______________________________")
					if P == "mmhg":
						Unit = "mmhg --> (atm)"
						answer = float(atmConverto[0])/760
						print("______________________________")
						print("Final Pressure (atm):")
						print(str(answer)+" atm")
						print("______________________________")
					if P == "atm":
						Unit = "atm --> (atm)"
						answer = float(atmConverto[0])/1
						print("______________________________")
						print("Final Pressure (atm):")
						print(str(answer)+" atm")
						print("______________________________")
					if P == "bar":
						Unit = "bar --> (atm)"
						answer = float(atmConverto[0])/1.01325
						print("______________________________")
						print("Final Pressure (atm):")
						print(str(answer)+" atm")
						print("______________________________")
				if questionpo == "kpa":
					print("")
					KPaConverto = input("What is your original Pressure (4.5+atm): ")
					KPaConverto=KPaConverto.replace(' ', '').split("+")
					P = KPaConverto[1].lower()
					if P == "kpa":
						Unit = "KPa --> (KPa)"
						answer = float(KPaConverto[0])/1
						print("______________________________")
						print("Final Pressure (KPa):")
						print(str(answer)+" KPa")
						print("______________________________")
					if P == "pa":
						Unit = "Pa --> (KPa)"
						answer = float(KPaConverto[0])/1000
						print("______________________________")
						print("Final Pressure (KPa):")
						print(str(answer)+" KPa")
						print("______________________________")
					if P == "torr":
						Unit = "torr --> (KPa)"
						answer = float(KPaConverto[0])/7.501
						print("______________________________")
						print("Final Pressure (KPa):")
						print(str(answer)+" KPa")
						print("______________________________")
					if P == "mmhg":
						Unit = "mmhg --> (KPa)"
						answer = float(KPaConverto[0])/7.501
						print("______________________________")
						print("Final Pressure (KPa):")
						print(str(answer)+" KPa")
						print("______________________________")
					if P == "atm":
						Unit = "atm --> (KPa)"
						answer = float(KPaConverto[0])*101.325
						print("______________________________")
						print("Final Pressure (KPa):")
						print(str(answer)+" KPa")
						print("______________________________")
					if P == "bar":
						Unit = "bar --> (KPa)"
						answer = float(KPaConverto[0])*100
						print("______________________________")
						print("Final Pressure (KPa):")
						print(str(answer)+" KPa")
						print("______________________________")
				if questionpo == "pa":
					print("")
					PaConverto = input("What is your original Pressure (4.5+atm): ")
					PaConverto=PaConverto.replace(' ', '').split("+")
					P = PaConverto[1].lower()
					if P == "kpa":
						Unit = "KPa --> (Pa)"
						answer = float(PaConverto[0])*1000
						print("______________________________")
						print("Final Pressure (Pa):")
						print(str(answer)+" Pa")
						print("______________________________")
					if P == "pa":
						Unit = "Pa --> (Pa)"
						answer = float(PaConverto[0])/1
						print("______________________________")
						print("Final Pressure (Pa):")
						print(str(answer)+" Pa")
						print("______________________________")
					if P == "torr":
						Unit = "torr --> (Pa)"
						answer = float(PaConverto[0])/133.322
						print("______________________________")
						print("Final Pressure (Pa):")
						print(str(answer)+" Pa")
						print("______________________________")
					if P == "mmhg":
						Unit = "mmhg --> (Pa)"
						answer = float(PaConverto[0])*133.322
						print("______________________________")
						print("Final Pressure (Pa):")
						print(str(answer)+" Pa")
						print("______________________________")
					if P == "atm":
						Unit = "atm --> (Pa)"
						answer = float(PaConverto[0])*101325
						print("______________________________")
						print("Final Pressure (Pa):")
						print(str(answer)+" Pa")
						print("______________________________")
					if P == "bar":
						Unit = "bar --> (Pa)"
						answer = float(PaConverto[0])*100000
						print("______________________________")
						print("Final Pressure (Pa):")
						print(str(answer)+" Pa")
						print("______________________________")
				if questionpo == "torr":
					print("")
					TorrConverto = input("What is your original Pressure (4.5+atm): ")
					TorrConverto=TorrConverto.replace(' ', '').split("+")
					P = TorrConverto[1].lower()
					if P == "kpa":
						Unit = "KPa --> (torr)"
						answer = float(TorrConverto[0])*7.50062
						print("______________________________")
						print("Final Pressure (torr):")
						print(str(answer)+" torr")
						print("______________________________")
					if P == "pa":
						Unit = "Pa --> (torr)"
						answer = float(TorrConverto[0])/133.322 
						print("______________________________")
						print("Final Pressure (torr):")
						print(str(answer)+" torr")
						print("______________________________")
					if P == "torr":
						Unit = "torr --> (torr)"
						answer = float(TorrConverto[0])/1
						print("______________________________")
						print("Final Pressure (torr):")
						print(str(answer)+" torr")
						print("______________________________")
					if P == "mmhg":
						Unit = "mmhg --> (torr)"
						answer = float(TorrConverto[0])/1
						print("______________________________")
						print("Final Pressure (torr):")
						print(str(answer)+" torr")
						print("______________________________")
					if P == "atm":
						Unit = "atm --> (torr)"
						answer = float(TorrConverto[0])*760
						print("______________________________")
						print("Final Pressure (torr):")
						print(str(answer)+" torr")
						print("______________________________")
					if P == "bar":
						Unit = "bar --> (torr)"
						answer = float(TorrConverto[0])*750.06156130264
						print("______________________________")
						print("Final Pressure (torr):")
						print(str(answer)+" torr")
						print("______________________________")
				if questionpo == "mmhg":
					print("")
					mmHgConverto = input("What is your original Pressure (4.5+atm): ")
					mmHgConverto=mmHgConverto.replace(' ', '').split("+")
					P = mmHgConverto[1].lower()
					if P == "kpa":
						Unit = "KPa --> (mmhg)"
						answer = float(mmHgConverto[0])*7.50062
						print("______________________________")
						print("Final Pressure (mmHg):")
						print(str(answer)+" mmHg")
						print("______________________________")
					if P == "pa":
						Unit = "Pa --> (mmhg)"
						answer = float(mmHgConverto[0])/133.322 
						print("______________________________")
						print("Final Pressure (mmHg):")
						print(str(answer)+" mmHg")
						print("______________________________")
					if P == "torr":
						Unit = "torr --> (mmhg)"
						answer = float(mmHgConverto[0])/1
						print("______________________________")
						print("Final Pressure (mmHg):")
						print(str(answer)+" mmHg")
						print("______________________________")
					if P == "mmhg":
						Unit = "mmhg --> (mmhg)"
						answer = float(mmHgConverto[0])/1
						print("______________________________")
						print("Final Pressure (mmHg):")
						print(str(answer)+" mmHg")
						print("______________________________")
					if P == "atm":
						Unit = "atm --> (mmhg)"
						answer = float(mmHgConverto[0])*760
						print("______________________________")
						print("Final Pressure (mmHg):")
						print(str(answer)+" mmHg")
						print("______________________________")
					if P == "bar":
						Unit = "bar --> (mmhg)"
						answer = float(mmHgConverto[0])*750.06156130264
						print("______________________________")
						print("Final Pressure (mmHg):")
						print(str(answer)+" mmHg")
						print("______________________________")
				print("")
				SaveQ = input("Do you want to save the answer? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1
			if chemistry_machine == "os":
				print("________________________________________________________________________________________________________")
				myList=[]
				Opening_orig = input("Element[E] or Other[O]: ").lower()
				print("")
				if Opening_orig == "o":
					ComName=[]
					ComMW=[]
					Compound = input("What is the Compound and Molecular Weight (EX: H2O+18.015): ")
					Compound=Compound.replace(' ', '').split("+")
					ComName.append(Compound[0])
					ComMW.append(Compound[1])
					Opening = input("What are you trying to find (Mol or Mass): ").lower()
					if Opening == "mol":
						WUOM = input("What is the Mass (+g  +kg  +mg  +oz): ").lower()
						WUOM=WUOM.replace(' ', '').split("+")
						if WUOM[1] == "g":
							Mass = float(WUOM[0])
							print(Mass)
						if WUOM[1] == "kg":
							Mass = float(WUOM[0])*1000
							print(Mass)
						if WUOM[1] == "mg":
							Mass = float(WUOM[0])/1000
							print(Mass)
						if WUOM[1] == "oz":
							Mass = float(WUOM[0])*28.34952
							print(Mass)
						answer = float(Mass)/float(Compound[1])
						print("")
						print("______________________________")
						print(str(Compound[0]) +" = "+ str(answer) +" mols")
						print("______________________________")
						Unit = "mols " + Compound[0]						
					if Opening == "mass":
						WUOMA = input("How many mols: ")
						UNIT = input("What is the Final Unit (g  kg  mg  oz): ").lower()
						if UNIT == "g":
							R="g"
						if UNIT == "kg":
							R="kg"
						if UNIT == "mg":
							R="mg"
						if UNIT == "oz":
							R="oz"
						answer = float(WUOMA)*float(Compound[1])
						if UNIT == "g":
							answer=str(answer)
						if UNIT == "kg":
							answer = float(answer)/1000
						if UNIT == "mg":
							answer = float(answer)*1000
						if UNIT == "oz":
							answer = float(answer)/28.34952
						print("")
						print("______________________________")
						print(str(Compound[0]) +" = "+ str(answer) +" "+str(R))
						print("______________________________")
						Unit = R +" "+ Compound[0]
				if Opening_orig == "e":
					Opening = input("What are you trying to find (Mol or Mass): ").lower()
					if Opening == "mol":
						question = input("Which Element and Quantity (He+2): ")
						question=question.replace(' ', '').split("+")
						WUOM = input("What is the Mass (+g  +kg  +mg): ")
						WUOM=WUOM.replace(' ', '').split("+")
						myList.append(WUOM[1])
						[x.lower() for x in myList]
						if question[0] == "H":
							E1=1.008
						if question[0] == "He":
							E1=4.0026
						if question[0] == "Li":
							E1=6.94
						if question[0] == "Be":
							E1=9.0122
						if question[0] == "B":
							E1=10.81
						if question[0] == "C":	
							E1=12.011
						if question[0] == "N":	
							E1=14.007
						if question[0] == "O":
							E1=15.999
						if question[0] == "F":	
							E1=18.998
						if question[0] == "Ne":	
							E1=20.180
						if question[0] == "Na":	
							E1=22.990
						if question[0] == "Mg":	
							E1=24.305
						if question[0] == "Al":	
							E1=26.982
						if question[0] == "Si":	
							E1=28.085
						if question[0] == "P":	
							E1=30.974
						if question[0] == "S":	
							E1=32.06
						if question[0] == "Cl":	
							E1=35.45
						if question[0] == "Ar":	
							E1=39.98
						if question[0] == "K":	
							E1=39.098
						if question[0] == "Ca":	
							E1=40.078
						if question[0] == "Sc":	
							E1=44.956
						if question[0] == "Ti":	
							E1=47.867
						if question[0] == "V":	
							E1=50.942
						if question[0] == "Cr":	
							E1=51.996
						if question[0] == "Mn":	
							E1=54.938
						if question[0] == "Fe":	
							E1=55.845
						if question[0] == "Co":	
							E1=58.993
						if question[0] == "Ni":	
							E1=58.693
						if question[0] == "Cu":	
							E1=63.546
						if question[0] == "Zn":	
							E1=65.38
						if question[0] == "Ga":	
							E1=69.723
						if question[0] == "Ge":	
							E1=72.630
						if question[0] == "As":	
							E1=74.992
						if question[0] == "Se":	
							E1=78.971
						if question[0] == "Br":	
							E1=79.904
						if question[0] == "Kr":	
							E1=83.798
						if question[0] == "Rb":	
							E1=85.468
						if question[0] == "Sr":	
							E1=87.62
						if question[0] == "Y":	
							E1=88.906
						if question[0] == "Zr":	
							E1=91.224
						if question[0] == "Nb":	
							E1=92.906
						if question[0] == "Mo":	
							E1=95.95
						if question[0] == "Tc":	
							E1=98
						if question[0] == "Ru":	
							E1=101.07
						if question[0] == "Rh":	
							E1=102.91
						if question[0] == "Pd":	
							E1=106.42
						if question[0] == "Ag":	
							E1=107.87
						if question[0] == "Cd":	
							E1=112.41
						if question[0] == "In":	
							E1=114.82
						if question[0] == "Sn":	
							E1=118.71
						if question[0] == "Sb":	
							E1=121.76
						if question[0] == "Te":	
							E1=127.60
						if question[0] == "I":	
							E1=126.90
						if question[0] == "Xe":	
							E1=131.29
						if question[0] == "Cs":	
							E1=132.91
						if question[0] == "Ba":	
							E1=137.33
						if question[0] == "La":	
							E1=138.91
						if question[0] == "Ce":
							E1=140.12
						if question[0] == "Pr":	
							E1=140.91
						if question[0] == "Nd":	
							E1=144.24
						if question[0] == "Pm":	
							E1=145
						if question[0] == "Sm":	
							E1=150.36
						if question[0] == "Eu":	
							E1=151.96
						if question[0] == "Gd":	
							E1=157.25
						if question[0] == "Tb":	
							E1=158.93
						if question[0] == "Dy":	
							E1=162.50
						if question[0] == "Ho":	
							E1=164.93
						if question[0] == "Er":	
							E1=167.26
						if question[0] == "Tm":	
							E1=168.93
						if question[0] == "Yb":	
							E1=173.05
						if question[0] == "Lu":	
							E1=174.97
						if question[0] == "Hf":	
							E1=178.49
						if question[0] == "Ta":	
							E1=180.95
						if question[0] == "W":	
							E1=183.84
						if question[0] == "Re":	
							E1=186.21
						if question[0] == "Os":	
							E1=190.23
						if question[0] == "Ir":	
							E1=192.22
						if question[0] == "Pt":	
							E1=195.08
						if question[0] == "Au":	
							E1=196.97
						if question[0] == "Hg":	
							E1=200.59
						if question[0] == "Tl":	
							E1=204.38
						if question[0] == "Pb":	
							E1=207.2
						if question[0] == "Bi":	
							E1=208.98
						if question[0] == "Po":	
							E1=209
						if question[0] == "At":	
							E1=210
						if question[0] == "Rn":	
							E1=222
						if question[0] == "Fr":	
							E1=223
						if question[0] == "Ra":	
							E1=226
						if question[0] == "Ac":	
							E1=227
						if question[0] == "Th":	
							E1=232.04
						if question[0] == "Pa":	
							E1=231.04
						if question[0] == "U":	
							E1=238.03
						if question[0] == "Np":	
							E1=237
						if question[0] == "Pu":	
							E1=244
						if question[0] == "Am":	
							E1=243
						if question[0] == "Cm":	
							E1=247
						if question[0] == "Bk":	
							E1=247
						if question[0] == "Cf":	
							E1=251
						if question[0] == "Es":	
							E1=252
						if question[0] == "Fm":	
							E1=257
						if question[0] == "Md":	
							E1=258
						if question[0] == "No":	
							E1=259
						if question[0] == "Lr":	
							E1=266
						if question[0] == "Rf":	
							E1=267
						if question[0] == "Db":	
							E1=268
						if question[0] == "Sg":	
							E1=269
						if question[0] == "Bh":
							E1=270
						if question[0] == "Hs":	
							E1=277
						if question[0] == "Mt":	
							E1=278
						if question[0] == "Ds":	
							E1=281
						if question[0] == "Rg":	
							E1=282
						if question[0] == "Cn":	
							E1=285
						if question[0] == "Nh":	
							E1=286
						if question[0] == "Fl":	
							E1=289
						if question[0] == "Mc":	
							E1=290
						if question[0] == "Lv":	
							E1=293
						if question[0] == "Ts":	
							E1=294
						if question[0] == "Og":
							E1=294
						if myList[0] == "kg":
							M = float(WUOM[0])*1000
						if myList[0] == "mg":
							M = float(WUOM[0])/1000
						if myList[0] == "g":
							M = float(WUOM[0])
						E1 = float(E1)*float(question[1])
						answer = float(M)/float(E1)
						print("")
						print("______________________________")
						print(str(question[0]) +" = "+ str(answer) +" mols")
						print("______________________________")
						Unit = "mols " + question[0]
					if Opening == "mass":
						question = input("Which Element and Quantity (He+2): ")
						question=question.replace(' ', '').split("+")
						Mols = float(input("How many Mols: "))
						FMV = input("What final mass value do you want (g or kg or mg): ").lower()
						if question[0] == "H":
							E1=1.008
						if question[0] == "He":
							E1=4.0026
						if question[0] == "Li":
							E1=6.94
						if question[0] == "Be":
							E1=9.0122
						if question[0] == "B":
							E1=10.81
						if question[0] == "C":	
							E1=12.011
						if question[0] == "N":	
							E1=14.007
						if question[0] == "O":
							E1=15.999
						if question[0] == "F":	
							E1=18.998
						if question[0] == "Ne":	
							E1=20.180
						if question[0] == "Na":	
							E1=22.990
						if question[0] == "Mg":	
							E1=24.305
						if question[0] == "Al":	
							E1=26.982
						if question[0] == "Si":	
							E1=28.085
						if question[0] == "P":	
							E1=30.974
						if question[0] == "S":	
							E1=32.06
						if question[0] == "Cl":	
							E1=35.45
						if question[0] == "Ar":	
							E1=39.98
						if question[0] == "K":	
							E1=39.098
						if question[0] == "Ca":	
							E1=40.078
						if question[0] == "Sc":	
							E1=44.956
						if question[0] == "Ti":	
							E1=47.867
						if question[0] == "V":	
							E1=50.942
						if question[0] == "Cr":	
							E1=51.996
						if question[0] == "Mn":	
							E1=54.938
						if question[0] == "Fe":	
							E1=55.845
						if question[0] == "Co":	
							E1=58.993
						if question[0] == "Ni":	
							E1=58.693
						if question[0] == "Cu":	
							E1=63.546
						if question[0] == "Zn":	
							E1=65.38
						if question[0] == "Ga":	
							E1=69.723
						if question[0] == "Ge":	
							E1=72.630
						if question[0] == "As":	
							E1=74.992
						if question[0] == "Se":	
							E1=78.971
						if question[0] == "Br":	
							E1=79.904
						if question[0] == "Kr":	
							E1=83.798
						if question[0] == "Rb":	
							E1=85.468
						if question[0] == "Sr":	
							E1=87.62
						if question[0] == "Y":	
							E1=88.906
						if question[0] == "Zr":	
							E1=91.224
						if question[0] == "Nb":	
							E1=92.906
						if question[0] == "Mo":	
							E1=95.95
						if question[0] == "Tc":	
							E1=98
						if question[0] == "Ru":	
							E1=101.07
						if question[0] == "Rh":	
							E1=102.91
						if question[0] == "Pd":	
							E1=106.42
						if question[0] == "Ag":	
							E1=107.87
						if question[0] == "Cd":	
							E1=112.41
						if question[0] == "In":	
							E1=114.82
						if question[0] == "Sn":	
							E1=118.71
						if question[0] == "Sb":	
							E1=121.76
						if question[0] == "Te":	
							E1=127.60
						if question[0] == "I":	
							E1=126.90
						if question[0] == "Xe":	
							E1=131.29
						if question[0] == "Cs":	
							E1=132.91
						if question[0] == "Ba":	
							E1=137.33
						if question[0] == "La":	
							E1=138.91
						if question[0] == "Ce":
							E1=140.12
						if question[0] == "Pr":	
							E1=140.91
						if question[0] == "Nd":	
							E1=144.24
						if question[0] == "Pm":	
							E1=145
						if question[0] == "Sm":	
							E1=150.36
						if question[0] == "Eu":	
							E1=151.96
						if question[0] == "Gd":	
							E1=157.25
						if question[0] == "Tb":	
							E1=158.93
						if question[0] == "Dy":	
							E1=162.50
						if question[0] == "Ho":	
							E1=164.93
						if question[0] == "Er":	
							E1=167.26
						if question[0] == "Tm":	
							E1=168.93
						if question[0] == "Yb":	
							E1=173.05
						if question[0] == "Lu":	
							E1=174.97
						if question[0] == "Hf":	
							E1=178.49
						if question[0] == "Ta":	
							E1=180.95
						if question[0] == "W":	
							E1=183.84
						if question[0] == "Re":	
							E1=186.21
						if question[0] == "Os":	
							E1=190.23
						if question[0] == "Ir":	
							E1=192.22
						if question[0] == "Pt":	
							E1=195.08
						if question[0] == "Au":	
							E1=196.97
						if question[0] == "Hg":	
							E1=200.59
						if question[0] == "Tl":	
							E1=204.38
						if question[0] == "Pb":	
							E1=207.2
						if question[0] == "Bi":	
							E1=208.98
						if question[0] == "Po":	
							E1=209
						if question[0] == "At":	
							E1=210
						if question[0] == "Rn":	
							E1=222
						if question[0] == "Fr":	
							E1=223
						if question[0] == "Ra":	
							E1=226
						if question[0] == "Ac":	
							E1=227
						if question[0] == "Th":	
							E1=232.04
						if question[0] == "Pa":	
							E1=231.04
						if question[0] == "U":	
							E1=238.03
						if question[0] == "Np":	
							E1=237
						if question[0] == "Pu":	
							E1=244
						if question[0] == "Am":	
							E1=243
						if question[0] == "Cm":	
							E1=247
						if question[0] == "Bk":	
							E1=247
						if question[0] == "Cf":	
							E1=251
						if question[0] == "Es":	
							E1=252
						if question[0] == "Fm":	
							E1=257
						if question[0] == "Md":	
							E1=258
						if question[0] == "No":	
							E1=259
						if question[0] == "Lr":	
							E1=266
						if question[0] == "Rf":	
							E1=267
						if question[0] == "Db":	
							E1=268
						if question[0] == "Sg":	
							E1=269
						if question[0] == "Bh":
							E1=270
						if question[0] == "Hs":	
							E1=277
						if question[0] == "Mt":	
							E1=278
						if question[0] == "Ds":	
							E1=281
						if question[0] == "Rg":	
							E1=282
						if question[0] == "Cn":	
							E1=285
						if question[0] == "Nh":	
							E1=286
						if question[0] == "Fl":	
							E1=289
						if question[0] == "Mc":	
							E1=290
						if question[0] == "Lv":	
							E1=293
						if question[0] == "Ts":	
							E1=294
						if question[0] == "Og":
							E1=294
						E1 = float(E1)*float(question[1])
						answer_orig = float(E1)*float(Mols)
						if FMV == "kg":
							answer = float(answer_orig)/1000
							U = " kg"
						if FMV == "mg":
							answer = float(answer_orig)*1000
							U = " mg"
						if FMV == "g":
							answer = str(answer_orig)
							U = " g"
						print("")
						print("______________________________")
						print(str(question[0]) +" = "+ str(answer)+U)
						print("______________________________")
						Unit = U +" "+ question[0]
				print("")
				SaveQ = input("Do you want to save the answer? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1
			if chemistry_machine == "pc":
				myList=[]
				ELName=[]
				ELNO=[]
				ELPerc=[]
				COMName=[]
				COMPName=[]
				WaterList=[]
				y=0
				qno=1
				print("________________________________________________________________________________________________________")
				question = int(input("How many Elements: "))
				if question == "":
					chem = False
				print("")
				NOT = int(question)
				while y in range(0, question):
					Enter = input("Enter Element NO. "+str(qno)+" and Quantity (He+2): ")
					
					Enter=Enter.replace(' ', '').split("+")	
					myList.append(Enter)
					COMName.append(Enter)
					qno+=1
					y += 1
					if myList[0][0] == "H":
						E1=1.008
					if myList[0][0] == "He":
						E1=4.0026
					if myList[0][0] == "Li":
						E1=6.94
					if myList[0][0] == "Be":
						E1=9.0122
					if myList[0][0] == "B":
						E1=10.81
					if myList[0][0] == "C":	
						E1=12.011
					if myList[0][0] == "N":	
						E1=14.007
					if myList[0][0] == "O":
						E1=15.999
					if myList[0][0] == "F":	
						E1=18.998
					if myList[0][0] == "Ne":	
						E1=20.180
					if myList[0][0] == "Na":	
						E1=22.990
					if myList[0][0] == "Mg":	
						E1=24.305
					if myList[0][0] == "Al":	
						E1=26.982
					if myList[0][0] == "Si":	
						E1=28.085
					if myList[0][0] == "P":	
						E1=30.974
					if myList[0][0] == "S":	
						E1=32.06
					if myList[0][0] == "Cl":	
						E1=35.45
					if myList[0][0] == "Ar":	
						E1=39.98
					if myList[0][0] == "K":	
						E1=39.098
					if myList[0][0] == "Ca":	
						E1=40.078
					if myList[0][0] == "Sc":	
						E1=44.956
					if myList[0][0] == "Ti":	
						E1=47.867
					if myList[0][0] == "V":	
						E1=50.942
					if myList[0][0] == "Cr":	
						E1=51.996
					if myList[0][0] == "Mn":	
						E1=54.938
					if myList[0][0] == "Fe":	
						E1=55.845
					if myList[0][0] == "Co":	
						E1=58.993
					if myList[0][0] == "Ni":	
						E1=58.693
					if myList[0][0] == "Cu":	
						E1=63.546
					if myList[0][0] == "Zn":	
						E1=65.38
					if myList[0][0] == "Ga":	
						E1=69.723
					if myList[0][0] == "Ge":	
						E1=72.630
					if myList[0][0] == "As":	
						E1=74.992
					if myList[0][0] == "Se":	
						E1=78.971
					if myList[0][0] == "Br":	
						E1=79.904
					if myList[0][0] == "Kr":	
						E1=83.798
					if myList[0][0] == "Rb":	
						E1=85.468
					if myList[0][0] == "Sr":	
						E1=87.62
					if myList[0][0] == "Y":	
						E1=88.906
					if myList[0][0] == "Zr":	
						E1=91.224
					if myList[0][0] == "Nb":	
						E1=92.906
					if myList[0][0] == "Mo":	
						E1=95.95
					if myList[0][0] == "Tc":	
						E1=98
					if myList[0][0] == "Ru":	
						E1=101.07
					if myList[0][0] == "Rh":	
						E1=102.91
					if myList[0][0] == "Pd":	
						E1=106.42
					if myList[0][0] == "Ag":	
						E1=107.87
					if myList[0][0] == "Cd":	
						E1=112.41
					if myList[0][0] == "In":	
						E1=114.82
					if myList[0][0] == "Sn":	
						E1=118.71
					if myList[0][0] == "Sb":	
						E1=121.76
					if myList[0][0] == "Te":	
						E1=127.60
					if myList[0][0] == "I":	
						E1=126.90
					if myList[0][0] == "Xe":	
						E1=131.29
					if myList[0][0] == "Cs":	
						E1=132.91
					if myList[0][0] == "Ba":	
						E1=137.33
					if myList[0][0] == "La":	
						E1=138.91
					if myList[0][0] == "Ce":
						E1=140.12
					if myList[0][0] == "Pr":	
						E1=140.91
					if myList[0][0] == "Nd":	
						E1=144.24
					if myList[0][0] == "Pm":	
						E1=145
					if myList[0][0] == "Sm":	
						E1=150.36
					if myList[0][0] == "Eu":	
						E1=151.96
					if myList[0][0] == "Gd":	
						E1=157.25
					if myList[0][0] == "Tb":	
						E1=158.93
					if myList[0][0] == "Dy":	
						E1=162.50
					if myList[0][0] == "Ho":	
						E1=164.93
					if myList[0][0] == "Er":	
						E1=167.26
					if myList[0][0] == "Tm":	
						E1=168.93
					if myList[0][0] == "Yb":	
						E1=173.05
					if myList[0][0] == "Lu":	
						E1=174.97
					if myList[0][0] == "Hf":	
						E1=178.49
					if myList[0][0] == "Ta":	
						E1=180.95
					if myList[0][0] == "W":	
						E1=183.84
					if myList[0][0] == "Re":	
						E1=186.21
					if myList[0][0] == "Os":	
						E1=190.23
					if myList[0][0] == "Ir":	
						E1=192.22
					if myList[0][0] == "Pt":	
						E1=195.08
					if myList[0][0] == "Au":	
						E1=196.97
					if myList[0][0] == "Hg":	
						E1=200.59
					if myList[0][0] == "Tl":	
						E1=204.38
					if myList[0][0] == "Pb":	
						E1=207.2
					if myList[0][0] == "Bi":	
						E1=208.98
					if myList[0][0] == "Po":	
						E1=209
					if myList[0][0] == "At":	
						E1=210
					if myList[0][0] == "Rn":	
						E1=222
					if myList[0][0] == "Fr":	
						E1=223
					if myList[0][0] == "Ra":	
						E1=226
					if myList[0][0] == "Ac":	
						E1=227
					if myList[0][0] == "Th":	
						E1=232.04
					if myList[0][0] == "Pa":	
						E1=231.04
					if myList[0][0] == "U":	
						E1=238.03
					if myList[0][0] == "Np":	
						E1=237
					if myList[0][0] == "Pu":	
						E1=244
					if myList[0][0] == "Am":	
						E1=243
					if myList[0][0] == "Cm":	
						E1=247
					if myList[0][0] == "Bk":	
						E1=247
					if myList[0][0] == "Cf":	
						E1=251
					if myList[0][0] == "Es":	
						E1=252
					if myList[0][0] == "Fm":	
						E1=257
					if myList[0][0] == "Md":	
						E1=258
					if myList[0][0] == "No":	
						E1=259
					if myList[0][0] == "Lr":	
						E1=266
					if myList[0][0] == "Rf":	
						E1=267
					if myList[0][0] == "Db":	
						E1=268
					if myList[0][0] == "Sg":	
						E1=269
					if myList[0][0] == "Bh":
						E1=270
					if myList[0][0] == "Hs":	
						E1=277
					if myList[0][0] == "Mt":	
						E1=278
					if myList[0][0] == "Ds":	
						E1=281
					if myList[0][0] == "Rg":	
						E1=282
					if myList[0][0] == "Cn":	
						E1=285
					if myList[0][0] == "Nh":	
						E1=286
					if myList[0][0] == "Fl":	
						E1=289
					if myList[0][0] == "Mc":	
						E1=290
					if myList[0][0] == "Lv":	
						E1=293
					if myList[0][0] == "Ts":	
						E1=294
					if myList[0][0] == "Og":
						E1=294
					if myList[0][0] == "H2O":
						E1=18.018
					x=True
					if myList[0][0] == "H2O":
						hydrate = myList[0][0]
						WaterList.append(hydrate)
					noCOF=float(str(myList[0][1]))
					ElementNOorig=float(E1*noCOF)
					ElementNO=str(ElementNOorig)
					ELName.append(myList[0][0])
					ELNO.append(ElementNO)
					myList.clear()
					ELNO = [float(i) for i in ELNO]
				SUMELNO = sum(ELNO)
				z=0
				k=0
				CN=0
				CNU=0
				CNC=1
				while CN in range(0, question):
					COMNO = COMName[CNU][CNC]
					if COMNO == "1":
						COMNO = ""
					COMP = COMName[CNU][0]+COMNO
					CNU+=1
					CN+=1
					if COMP == "H2O"+COMNO:
						COMP = "~"+COMNO+"H2O"
					COMPName.append(COMP)
				while z in range(0, question):
					ELPDivision_Orig = float(ELNO[k])/float(SUMELNO)
					ELPDivision = float(ELPDivision_Orig)*100
					ELPerc.append(ELPDivision)
					k+=1
					z+=1
				f=0
				if SUMELNO == 18.015:
					COMMMname = " (water)"
				elif SUMELNO == 44.009:
					COMMMname = " (Carbon Dioxide)"
				elif SUMELNO == 180.156:
					COMMMname = " (Glucose)"
				else:
					COMMMname = ""
				print("")
				print("______________________________")
				while f in range(0, question):
					print(str(ELName[f]) +" = "+ str(ELPerc[f])+"%")
					f+=1
				print("")
				print("Compound Formula: "+("".join([str(n) for n in COMPName]))+COMMMname)
				print("Molecular Weight = "+str(SUMELNO)+ " g/mol")
				print("______________________________")
				Unit = "g/mol "+("".join([str(n) for n in COMPName]))
				answer = SUMELNO
				print("")
				SaveQ = input("Do you want to save the MW? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1
			if chemistry_machine == "p":
				#pH/poH/H+/& OH- Calculator
				print("________________________________________________________________________________________________________")
				pohcalc = input("What do you want to solve for? (pH, pOH, H, OH, or All(A)): ").lower()
				print("")
				if pohcalc == "ph":
					acidobase = input("Which value do you have? (pOH, H, or OH): ").lower()
					print("")
					if acidobase == "h":
						hconc=float(input("What is the hydrogen ion concentration? (Molarity): "))
						print("")
						neglog= (math.log(hconc,10))
						fneglog = float(neglog)*-1
						print("______________________________")
						print("Final pH:")
						print(str(fneglog))
						print("______________________________")
						answer = fneglog
					if acidobase == "oh":
						ohconc=float(input("What is the hydroxide ion concentration? (Molarity): "))
						print("")
						neglog= (math.log(ohconc,10))
						fneglog = float(neglog)*-1
						ffneglog = 14 - float(fneglog)
						print("______________________________")
						print("Final pH:")
						print(str(ffneglog))
						print("______________________________")
						answer = ffneglog
					if acidobase == "poh":
						phpoh=float(input("What is the pOH: "))
						print("")
						answer = 14 - float(phpoh)
						print("______________________________")
						print("Final pH:")
						print(str(answer))
						print("______________________________")
					Unit = "pH"
					print("")
					SaveQ = input("Do you want to save the pH? (y or n): ").lower()
					if SaveQ == "y":
						if len(Save1) == 0:
							Save1.append(answer)
							Save1.append(Unit)
						elif len(Save2) == 0:
							Save2.append(answer)
							Save2.append(Unit)
						elif len(Save3) == 0:
							Save3.append(answer)
							Save3.append(Unit)
						elif len(Save4) == 0:
							Save4.append(answer)
							Save4.append(Unit)
						elif len(Save5) == 0:
							Save5.append(answer)
							Save5.append(Unit)
						elif len(Save6) == 0:
							Save6.append(answer)
							Save6.append(Unit)
						elif len(Save7) == 0:
							Save7.append(answer)
							Save7.append(Unit)
						elif len(Save8) == 0:
							Save8.append(answer)
							Save8.append(Unit)
						elif len(Save9) == 0:
							Save9.append(answer)
							Save9.append(Unit)
						elif len(Save10) == 0:
							Save10.append(answer)
							Save10.append(Unit)
						print("(Saved)")
						time.sleep(.25)
					if SaveQ == "n":
						x=1
				if pohcalc == "poh":
					pohpo = input("Which value do you have? (pH, H, or OH): ").lower()
					if pohpo == "ph":
						pohph = float(input("Enter the pH: "))
						answer = 14-float(pohph)
						print("______________________________")
						print("Final pOH:")
						print(str(answer))
						print("______________________________")
					if pohpo == "h":
						pohh = float(input("Enter the H+ Concentration: "))
						answer2 = (math.log(pohh,10))
						answer1 = float(answer2)*-1
						answer = 14-float(answer1)
						print("______________________________")
						print("Final pOH:")
						print(str(answer))
						print("______________________________")
					if pohpo == "oh":
						pohoh = float(input("Enter the OH- Concentration: "))
						answer2 = (math.log(pohoh,10))
						answer = float(answer2)*-1
						print("______________________________")
						print("Final pOH:")
						print(str(answer))
						print("______________________________")
					Unit = "pOH"
					print("")
					SaveQ = input("Do you want to save the pOH? (y or n): ").lower()
					if SaveQ == "y":
						if len(Save1) == 0:
							Save1.append(answer)
							Save1.append(Unit)
						elif len(Save2) == 0:
							Save2.append(answer)
							Save2.append(Unit)
						elif len(Save3) == 0:
							Save3.append(answer)
							Save3.append(Unit)
						elif len(Save4) == 0:
							Save4.append(answer)
							Save4.append(Unit)
						elif len(Save5) == 0:
							Save5.append(answer)
							Save5.append(Unit)
						elif len(Save6) == 0:
							Save6.append(answer)
							Save6.append(Unit)
						elif len(Save7) == 0:
							Save7.append(answer)
							Save7.append(Unit)
						elif len(Save8) == 0:
							Save8.append(answer)
							Save8.append(Unit)
						elif len(Save9) == 0:
							Save9.append(answer)
							Save9.append(Unit)
						elif len(Save10) == 0:
							Save10.append(answer)
							Save10.append(Unit)
						print("(Saved)")
						time.sleep(.25)
					if SaveQ == "n":
						x=1					
				if pohcalc == "h":
					hpo = input("Which value do you have? (pH, pOH, or OH): ").lower()
					if hpo == "ph":
						hph = float(input("Enter the pH: "))
						answer1 = float(hph)*-1
						answer = 10 ** float(answer1)
						print("______________________________")
						print("Final H+ Concentration:")
						print(str(answer))
						print("______________________________")
					if hpo == "poh":
						hpoh = float(input("Enter the pOH: "))
						answer2 = 14-float(hpoh)
						answer1 = float(answer2)*-1
						answer = 10 ** float(answer1)
						print("______________________________")
						print("Final H+ Concentration:")
						print(str(answer))
						print("______________________________")
					if hpo == "oh":
						hoh = float(input("Enter the OH- Concentration: "))
						answer = 0.00000000000001/float(hoh)
						print("______________________________")
						print("Final H+ Concentration:")
						print(str(answer))
						print("______________________________")	
					Unit = "H+"
					print("")
					SaveQ = input("Do you want to save the H+? (y or n): ").lower()
					if SaveQ == "y":
						if len(Save1) == 0:
							Save1.append(answer)
							Save1.append(Unit)
						elif len(Save2) == 0:
							Save2.append(answer)
							Save2.append(Unit)
						elif len(Save3) == 0:
							Save3.append(answer)
							Save3.append(Unit)
						elif len(Save4) == 0:
							Save4.append(answer)
							Save4.append(Unit)
						elif len(Save5) == 0:
							Save5.append(answer)
							Save5.append(Unit)
						elif len(Save6) == 0:
							Save6.append(answer)
							Save6.append(Unit)
						elif len(Save7) == 0:
							Save7.append(answer)
							Save7.append(Unit)
						elif len(Save8) == 0:
							Save8.append(answer)
							Save8.append(Unit)
						elif len(Save9) == 0:
							Save9.append(answer)
							Save9.append(Unit)
						elif len(Save10) == 0:
							Save10.append(answer)
							Save10.append(Unit)
						print("(Saved)")
						time.sleep(.25)
					if SaveQ == "n":
						x=1					
				if pohcalc == "oh":
					ohpo = input("Which value do you have? (pH, pOH, or H): ").lower()
					if ohpo == "ph":
						ohph = float(input("Enter the pH: "))
						answer2 = 14 - float(ohph)
						answer1 = float(answer2)*-1
						answer = 10 ** float(answer1)
						print("______________________________")
						print("Final OH- Concentration:")
						print(str(answer))
						print("______________________________")
					if ohpo == "poh":
						pohoh = float(input("Enter the pOH: "))
						answer1 = float(pohoh)*-1
						answer = 10 ** float(answer1)
						print("______________________________")
						print("Final OH- Concentration:")
						print(str(answer))
						print("______________________________")
					if ohpo == "h":
						ohh = float(input("Enter the H+ Concentration: "))
						answer = 0.00000000000001/float(ohh)
						print("______________________________")
						print("Final Oh- Concentration:")
						print(str(answer))
						print("______________________________")
					Unit = "OH-"
					print("")
					SaveQ = input("Do you want to save the OH-? (y or n): ").lower()
					if SaveQ == "y":
						if len(Save1) == 0:
							Save1.append(answer)
							Save1.append(Unit)
						elif len(Save2) == 0:
							Save2.append(answer)
							Save2.append(Unit)
						elif len(Save3) == 0:
							Save3.append(answer)
							Save3.append(Unit)
						elif len(Save4) == 0:
							Save4.append(answer)
							Save4.append(Unit)
						elif len(Save5) == 0:
							Save5.append(answer)
							Save5.append(Unit)
						elif len(Save6) == 0:
							Save6.append(answer)
							Save6.append(Unit)
						elif len(Save7) == 0:
							Save7.append(answer)
							Save7.append(Unit)
						elif len(Save8) == 0:
							Save8.append(answer)
							Save8.append(Unit)
						elif len(Save9) == 0:
							Save9.append(answer)
							Save9.append(Unit)
						elif len(Save10) == 0:
							Save10.append(answer)
							Save10.append(Unit)
						print("(Saved)")
						time.sleep(.25)
					if SaveQ == "n":
						x=1					
				if pohcalc == "a":
					allvaluepo = input("Which value do you have? (pH, pOH, H, or OH): ").lower()
					if allvaluepo == "ph":
						ph = float(input("What is the pH: "))
						#_______________pOH
						answerpohph = 14-float(ph)
						#_______________H
						answer1 = float(ph)*-1
						answerhph = 10 ** float(answer1)
						#_______________OH
						answer2 = 14 - float(ph)
						answer1 = float(answer2)*-1
						answerohph = 10 ** float(answer1)
						#_________________
						
						if ph < 7:
							abn = "Acid"
						if ph > 7:
							abn = "Base"
						if ph == 7:
							abn = "Neutral"
						print("")
						print("______________________________")
						print("pH = "+str(ph))
						print("pOH = "+str(answerpohph))
						print("H+ = "+str(answerhph))
						print("OH- = "+str(answerohph))
						print("")
						print("pH Range = "+abn)
						print("______________________________")
					if allvaluepo == "poh":
						poh = float(input("What is the pOH: "))
						#_______________pH
						answerphpoh = 14 - float(poh)
						#_______________H
						answer2 = 14-float(poh)
						answer1 = float(answer2)*-1
						answerhpoh = 10 ** float(answer1)
						#_______________OH
						answer1 = float(poh)*-1
						answerohpoh = 10 ** float(answer1)
						#_________________	
						
						if answerphpoh < 7:
							abn = "Acid"
						if answerphpoh > 7:
							abn = "Base"
						if answerphpoh == 7:
							abn = "Neutral"
						print("")
						print("______________________________")
						print("pH = "+str(answerphpoh))
						print("pOH = "+str(poh))
						print("H+ = "+str(answerhpoh))
						print("OH- = "+str(answerohpoh))
						print("")
						print("pH Range = "+abn)
						print("______________________________")
					if allvaluepo == "h":
						h = float(input("What is the H+ Concentration: "))
						#_______________pOH
						answer2 = (math.log(h,10))
						answer1 = float(answer2)*-1
						answerpohh = 14-float(answer1)	
						#_______________pH
						neglog= (math.log(h,10))
						answerphh = float(neglog)*-1		
						#_______________OH
						answerohh = 0.00000000000001/float(h)		
						#_________________	
						
						if answerphh < 7:
							abn = "Acid"
						if answerphh > 7:
							abn = "Base"
						if answerphh == 7:
							abn = "Neutral"
						print("")
						print("______________________________")
						print("pH = "+str(answerphh))
						print("pOH = "+str(answerpohh))
						print("H+ = "+str(h))
						print("OH- = "+str(answerohh))
						print("")
						print("pH Range = "+abn)
						print("______________________________")
					if allvaluepo == "oh":
						oh = float(input("What is the OH- Concentration: "))
						#_______________pOH
						answer2 = (math.log(oh,10))
						answerpohoh = float(answer2)*-1
						#_______________H
						answerhoh = 0.00000000000001/float(oh)
						#_______________pH
						neglog= (math.log(oh,10))
						fneglog = float(neglog)*-1
						answerphoh = 14 - float(fneglog)		
						#_________________	
						
						if answerphoh < 7:
							abn = "Acid"
						if answerphoh > 7:
							abn = "Base"
						if answerphoh == 7:
							abn = "Neutral"
						print("")
						print("______________________________")
						print("pH = "+str(answerphoh))
						print("pOH = "+str(answerpohoh))
						print("H+ = "+str(answerhoh))
						print("OH- = "+str(oh))
						print("")
						print("pH Range = "+abn)
						print("______________________________")
			if chemistry_machine == "i":
				print("________________________________________________________________________________________________________")
				IGL=input("What are you trying to find? (P, V, n, R, or T): ").lower()
				if IGL == "r":
					print("")
					print("(Constant Selected)")
					print("")
					Constant = input("Which Pressure (mmHg, atm, kPa, or torr): ").lower()
					if Constant == "mmhg":
						print("")
						FIGLP = 62.4
						print("______________________________")
						print("Final Constant:")
						print(str(FIGLP))
						print("______________________________")
						print("")					
					if Constant == "atm":
						FIGLP = 0.0821
						print("______________________________")
						print("Final Constant:")
						print(str(FIGLP))
						print("______________________________")
						print("")	
					if Constant == "kpa":
						FIGLP = 8.31
						print("______________________________")
						print("Final Constant:")
						print(str(FIGLP))
						print("______________________________")
						print("")	
					if Constant == "torr":
						FIGLP = 62.4
						print("______________________________")
						print("Final Constant:")
						print(str(FIGLP))
						print("______________________________")
						print("")
					answer = FIGLP
					Unit = "R"
				if IGL == "p":
					#PV=nRT
					print("")
					print("(Pressure Selected)")
					print("")
					Volume_Orig = input("Enter the Volume: (+mL or +L): ").lower()
					Moles = input("Enter number of Moles: ")
					Temperature_Orig = input("Enter the Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					Volume=Volume_Orig.replace(' ', '').split("+")
					Constant = input("What unit of pressure? (mmHg, atm, kPa, or torr): ").lower()
					#0: Temperature, 1: C or K
					if Temperature[1] == "c":
						Temperature.remove('c')
						Temperature = float(Temperature[0])+273.15
					elif Temperature[1] == "f":
						Temperature.remove('f')
						Temperature = float(Temperature[0])-32
						Temperature = float(Temperature)*5
						Temperature = float(Temperature)/9
						Temperature = float(Temperature)+273.15
					else:
						Temperature.remove('k')
						Temperature = float(Temperature[0])
					if Constant == "mmhg":
						R = 62.4
						Unit = "mmHg"
					if Constant == "atm":
						R = 0.0821
						Unit = "atm"
					if Constant == "kpa":
						R = 8.31
						Unit = "kPa"
					if Constant == "torr":
						R = 62.4
						Unit = "torr"
					if Volume[1] == "ml":
						Volume.remove('ml')
						Volume = float(Volume[0])/1000
					else:
						Volume.remove('l')
						Volume = float(Volume[0])
					#P=nRT/V
					IGLP1 = float(Moles)*float(R)*float(Temperature)
					FIGLP = float(IGLP1)/float(Volume)
					print("")
					print("______________________________")
					print("Final Pressure:")
					print(str(FIGLP), Unit)
					print("______________________________")
					print("")					
					answer = FIGLP
				if IGL == "v":
					print("")
					print("(Volume Selected)")
					print("")
					Moles = input("Enter number of Moles: ")
					Temperature_Orig = input("Enter the Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					Pressure_Orig = input("Enter the Pressure (+mmHg, +atm, +kPa, or +torr): ").lower()
					Pressure=Pressure_Orig.replace(' ', '').split("+")
					Unit = input("Final Unit of Volume (mL or L): ").lower()
					#0: Temperature, 1: C or K
					if Temperature[1] == "c":
						Temperature.remove('c')
						Temperature = float(Temperature[0])+273.15
					elif Temperature[1] == "f":
						Temperature.remove('f')
						Temperature = float(Temperature[0])-32
						Temperature = float(Temperature)*5
						Temperature = float(Temperature)/9
						Temperature = float(Temperature)+273.15
					else:
						Temperature.remove('k')
						Temperature = float(Temperature[0])
					if Pressure[1] == "mmhg":
						R = 62.4
					if Pressure[1] == "atm":
						R = 0.0821
					if Pressure[1] == "kpa":
						R = 8.31
					if Pressure[1] == "torr":
						R = 62.4
					Pressure.remove(Pressure[1])
					Pressure = float(Pressure[0])
					#V=nRT/P
					IGLV1 = float(Moles)*float(R)*float(Temperature)
					FIGLV = float(IGLV1)/float(Pressure)
					if Unit == "ml":
						FIGLV2 = float(FIGLV)*1000
						Unit = "mL"
					if Unit == "l":
						FIGLV2 = float(FIGLV)*1
						Unit = "L"
					print("")
					print("______________________________")
					print("Final Volume:")
					print(str(FIGLV2), Unit)
					print("______________________________")
					print("")
					answer = FIGLV2
				if IGL == "n":
					print("")
					print("(Moles Selected)")
					print("")
					Volume_Orig = input("Enter the Volume: (+mL or +L): ").lower()
					Volume=Volume_Orig.replace(' ', '').split("+")
					Temperature_Orig = input("Enter the Temperature (+K, +C, or +F): ").lower()
					Temperature=Temperature_Orig.replace(' ', '').split("+")
					Pressure_Orig = input("Enter the Pressure (+mmHg, +atm, +kPa, or +torr): ").lower()
					Pressure=Pressure_Orig.replace(' ', '').split("+")
					#0: Temperature, 1: C or K
					if Temperature[1] == "c":
						Temperature.remove('c')
						Temperature = float(Temperature[0])+273.15
					elif Temperature[1] == "f":
						Temperature.remove('f')
						Temperature = float(Temperature[0])-32
						Temperature = float(Temperature)*5
						Temperature = float(Temperature)/9
						Temperature = float(Temperature)+273.15
					else:
						Temperature.remove('k')
						Temperature = float(Temperature[0])
					if Pressure[1] == "mmhg":
						R = 62.4
					if Pressure[1] == "atm":
						R = 0.0821
					if Pressure[1] == "kpa":
						R = 8.31
					if Pressure[1] == "torr":
						R = 62.4
					Pressure.remove(Pressure[1])
					Pressure = float(Pressure[0])
					if Volume[1] == "ml":
						Volume.remove('ml')
						Volume = float(Volume[0])/1000
					else:
						Volume.remove('l')
						Volume = float(Volume[0])
					#n=PV/RT
					IGLn1 = float(Pressure)*float(Volume)
					FIGLn = float(R)*float(Temperature)
					FIGnV2 = float(IGLn1)/float(FIGLn)
					print("")
					print("______________________________")
					print("Final Mol Count:")
					print(str(FIGnV2), "mols")
					print("______________________________")
					print("")
					Unit = "mols"
					answer = FIGnV2
				if IGL == "t":
					print("")
					print("(Temperature Selected)")
					print("")
					Volume_Orig = input("Enter the Volume: (+mL or +L): ").lower()
					Volume=Volume_Orig.replace(' ', '').split("+")
					Moles=input("Enter number of Moles: ")
					Pressure_Orig = input("Enter the Pressure (+mmHg, +atm, +kPa, or +torr): ").lower()
					Pressure=Pressure_Orig.replace(' ', '').split("+")
					Unit = input("Final Temperature Unit (K, C, or F): ").upper()
					if Pressure[1] == "mmhg":
						R = 62.4
					if Pressure[1] == "atm":
						R = 0.0821
					if Pressure[1] == "kpa":
						R = 8.31
					if Pressure[1] == "torr":
						R = 62.4
					Pressure.remove(Pressure[1])
					Pressure = float(Pressure[0])
					if Volume[1] == "ml":
						Volume.remove('ml')
						Volume = float(Volume[0])/1000
					else:
						Volume.remove('l')
						Volume = float(Volume[0])
					#T=PV/nR
					
					IGLT1 = float(Pressure)*float(Volume)
					FIGLT = float(R)*float(Moles)
					FFIGTV2 = float(IGLT1)/float(FIGLT)
					print("")
					if Unit == "C":
						FFIGTV2 = float(FFIGTV2)-273.15
					if Unit == "F":
						FerFIGTV2 = float(FFIGTV2)-273.15
						FerFFIGTV2 = float(FerFIGTV2)*1.8
						FFIGTV2 = float(FerFFIGTV2)+32
					print("______________________________")
					print("Final Temperature:")
					print(str(FFIGTV2), Unit)
					print("______________________________")
					print("")
					answer = FFIGTV2
				print("")
				SaveQ = input("Do you want to save the answer? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)
						Save1.append(Unit)
					elif len(Save2) == 0:
						Save2.append(answer)
						Save2.append(Unit)
					elif len(Save3) == 0:
						Save3.append(answer)
						Save3.append(Unit)
					elif len(Save4) == 0:
						Save4.append(answer)
						Save4.append(Unit)
					elif len(Save5) == 0:
						Save5.append(answer)
						Save5.append(Unit)
					elif len(Save6) == 0:
						Save6.append(answer)
						Save6.append(Unit)
					elif len(Save7) == 0:
						Save7.append(answer)
						Save7.append(Unit)
					elif len(Save8) == 0:
						Save8.append(answer)
						Save8.append(Unit)
					elif len(Save9) == 0:
						Save9.append(answer)
						Save9.append(Unit)
					elif len(Save10) == 0:
						Save10.append(answer)
						Save10.append(Unit)
					print("(Saved)")
					time.sleep(.25)
				if SaveQ == "n":
					x=1				
			if chemistry_machine == "fm":
				#Molecular Formula & Emperical Formula Calculator
				print("________________________________________________________________________________________________________")
				EFMFPo = input("Do you want to solve for EF or MF?: ").lower()
				print("")
				print("")
				EFNO=int(input("How many elements do you have? (2-5): "))
				print("")
				if EFNO == 2:
					emList=[]
					EM2P1_one = question=input("Enter your first element, percent, & atomic weight (EX: He+5+4): ")
					EM2P1_two = question=input("Enter your second element, percent, & atomic weight (EX: He+5+4): ")
					if EFMFPo == "mf":
						MFM1= question = input("Enter the Molar Mass: ")
					EM2P1=EM2P1_one.replace(' ', '').split("+")
					EM2P2=EM2P1_two.replace(' ', '').split("+")
					
					#0: Reactant, 1: Percent [mass (g)], 2: atomic weight
					
					EM2C1 = float(EM2P1[1])/float(EM2P1[2])
					EM2C2 = float(EM2P2[1])/float(EM2P2[2])
					if EM2C1 < EM2C2:
						EM2FA1 = float(EM2C1)/float(EM2C1)
						EM2FFA1 = int((round(float(EM2FA1), 0)))
						EM2FA2 = float(EM2C2)/float(EM2C1)
						EM2FFA2 = int((round(float(EM2FA2), 0)))
						print("")
						if EM2FFA1 != EM2FFA2:
							print("Empirical Formula:")
							print("______________________________")
							print(str(EM2P1[0])+" = "+str(EM2FFA1))
							print(str(EM2P2[0])+" = "+str(EM2FFA2))
							print("")
							print("Together: "+str((str(EM2P1[0])+str(EM2P2[0])+str(EM2FFA2))))
							print("______________________________")
							answer = str((str(EM2P1[0])+str(EM2P2[0])+str(EM2FFA2)))
						if EM2FFA1 == EM2FFA2:
							print("Empirical Formula:")
							print("______________________________")
							print(str(EM2P1[0])+" = "+str(EM2FFA1))
							print(str(EM2P2[0])+" = "+str(EM2FFA2))
							print("")
							print("Together: "+str((str(EM2P1[0])+str(EM2P2[0]))))
							print("______________________________")
							answer = str((str(EM2P1[0])+str(EM2P2[0])))
						if EFMFPo == "mf":
							print("")
							MOE1 = float(EM2P1[2])*float(EM2FFA1)
							MOE2 = float(EM2P2[2])*float(EM2FFA2)
							MOE = float(MOE1)+float(MOE2)
							MFR_o = float(MFM1)/float(MOE)
							MFR = int((round(float(MFR_o), 0)))
							E1_o = float(EM2FFA1) * float(MFR)
							E2_o = float(EM2FFA2) * float(MFR)
							E1 = int((round(float(E1_o), 0)))
							E2 = int((round(float(E2_o), 0)))
							print("")
							print("Molecular Formula:")
							print("______________________________")
							print(str(EM2P1[0])+" = "+str(E1))
							print(str(EM2P2[0])+" = "+str(E2))
							print("")
							print("Together: "+str((str(EM2P1[0])+str(E1)+str(EM2P2[0])+str(E2))))
							print("______________________________")
							answer = str((str(EM2P1[0])+str(E1)+str(EM2P2[0])+str(E2)))
						print("")
					if EM2C1 > EM2C2:
						EM2FA3 = float(EM2C1)/float(EM2C2)
						EM2FFA3 = int((round(float(EM2FA3), 0)))
						EM2FA4 = float(EM2C2)/float(EM2C2)
						EM2FFA4 = int((round(float(EM2FA4), 0)))
						print("")
						if EM2FFA3 != EM2FFA4:
							print("Empirical Formula:")
							print("______________________________")
							print(str(EM2P1[0])+" = "+str(EM2FFA3))
							print(str(EM2P2[0])+" = "+str(EM2FFA4))		
							print("")
							print("Together: "+str((str(EM2P1[0])+str(EM2FFA3)+str(EM2P2[0]))))
							print("______________________________")
							answer = str((str(EM2P1[0])+str(EM2FFA3)+str(EM2P2[0])))
						if EM2FFA3 == EM2FFA4:
							print("Empirical Formula:")
							print("______________________________")
							print(str(EM2P1[0])+" = "+str(EM2FFA3))
							print(str(EM2P2[0])+" = "+str(EM2FFA4))		
							print("")
							print("Together: "+str((EM2P1[0]+EM2P2[0])))
							print("______________________________")
							answer = str((EM2P1[0]+EM2P2[0]))
						if EFMFPo == "mf":
							MOE1 = float(EM2P1[2])*float(EM2FFA3)
							MOE2 = float(EM2P2[2])*float(EM2FFA4)
							MOE = float(MOE1)+float(MOE2)
							MFR_o = float(MFM1)/float(MOE)
							MFR = int((round(float(MFR_o), 0)))
							E1_o = float(EM2FFA3) * float(MFR)
							E2_o = float(EM2FFA4) * float(MFR)
							E1 = int((round(float(E1_o), 0)))
							E2 = int((round(float(E2_o), 0)))
							print("")
							print("")
							print("Molecular Formula:")
							print("______________________________")
							print(str(EM2P1[0])+" = "+str(E1))
							print(str(EM2P2[0])+" = "+str(E2))
							print("")
							print("Together: "+str((str(EM2P1[0])+str(E1)+str(EM2P2[0])+str(E2))))
							print("______________________________")
							answer = str((str(EM2P1[0])+str(E1)+str(EM2P2[0])+str(E2)))
				if EFNO == 3:
					emList=[]
					EM3P1_one = question=input("Enter your first element, percent, & atomic weight (EX: He+5+4): ")
					EM3P1_two = question=input("Enter your second element, percent, & atomic weight (EX: He+5+4): ")
					EM3P1_three = question=input("Enter your third element, percent, & atomic weight (EX: He+5+4): ")
					if EFMFPo == "mf":
						MFM1= question = input("Enter the Molar Mass: ")
					EM3P1=EM3P1_one.replace(' ', '').split("+")
					EM3P2=EM3P1_two.replace(' ', '').split("+")
					EM3P3=EM3P1_three.replace(' ', '').split("+")
					
					#0: Reactant, 1: Percent [mass (g)], 2: atomic weight
					
					EM3C1 = float(EM3P1[1])/float(EM3P1[2])
					EM3C2 = float(EM3P2[1])/float(EM3P2[2])
					EM3C3 = float(EM3P3[1])/float(EM3P3[2])
					
					if EM3C1 < EM3C2:
						if EM3C1 < EM3C3:
							EM3FA1 = float(EM3C1)/float(EM3C1)
							EM3FFA1 = int((round(float(EM3FA1), 0)))
							EM3FA2 = float(EM3C2)/float(EM3C1)
							EM3FFA2 = int((round(float(EM3FA2), 0)))
							EM3FA3 = float(EM3C3)/float(EM3C1)
							EM3FFA3 = int((round(float(EM3FA3), 0)))		
							print("")
							print("Empirical Formula:")
							print("______________________________")
							print(str(EM3P1[0])+" = "+str(EM3FFA1))
							print(str(EM3P2[0])+" = "+str(EM3FFA2))
							print(str(EM3P3[0])+" = "+str(EM3FFA3))
							print("")
							print("Together: "+str((str(EM3P1[0])+str(EM3P2[0])+str(EM3FFA2)+str(EM3P3[0])+str(EM3FFA3))))
							print("______________________________")
							answer = str((str(EM3P1[0])+str(EM3P2[0])+str(EM3FFA2)+str(EM3P3[0])+str(EM3FFA3)))
							if EFMFPo == "mf":
								MOE1 = float(EM3P1[2])*float(EM3FFA1)
								MOE2 = float(EM3P2[2])*float(EM3FFA2)
								MOE3 = float(EM3P3[2])*float(EM3FFA3)
								MOE = float(MOE1)+float(MOE2)+float(MOE3)
								MFR_o = float(MFM1)/float(MOE)
								MFR = int((round(float(MFR_o), 0)))
								E1_o = float(EM3FFA1) * float(MFR)
								E2_o = float(EM3FFA2) * float(MFR)
								E3_o = float(EM3FFA3) * float(MFR)
								E1 = int((round(float(E1_o), 0)))
								E2 = int((round(float(E2_o), 0)))
								E3 = int((round(float(E3_o), 0)))
								print("")
								print("")
								print("Molecular Formula:")
								print("______________________________")
								print(str(EM3P1[0])+" = "+str(E1))
								print(str(EM3P2[0])+" = "+str(E2))
								print(str(EM3P3[0])+" = "+str(E3))
								print("")
								print("Together: "+str((str(EM3P1[0])+str(E1)+str(EM3P2[0])+str(E2)+str(EM3P3[0])+str(E3))))
								print("______________________________")
								answer = str((str(EM3P1[0])+str(E1)+str(EM3P2[0])+str(E2)+str(EM3P3[0])+str(E3)))
					if EM3C2 < EM3C3:
						if EM3C2 < EM3C1:
							EM3FA1 = float(EM3C1)/float(EM3C2)
							EM3FFA1 = int((round(float(EM3FA1), 0)))
							EM3FA2 = float(EM3C2)/float(EM3C2)
							EM3FFA2 = int((round(float(EM3FA2), 0)))
							EM3FA3 = float(EM3C3)/float(EM3C2)
							EM3FFA3 = int((round(float(EM3FA3), 0)))		
							print("")
							print("Empirical Formula:")
							print("______________________________")
							print(str(EM3P1[0])+" = "+str(EM3FFA1))
							print(str(EM3P2[0])+" = "+str(EM3FFA2))
							print(str(EM3P3[0])+" = "+str(EM3FFA3))
							print("")
							print("Together: "+str((str(EM3P1[0])+str(EM3FFA1)+str(EM3P2[0])+str(EM3P3[0])+str(EM3FFA3))))
							print("______________________________")
							answer = str((str(EM3P1[0])+str(EM3FFA1)+str(EM3P2[0])+str(EM3P3[0])+str(EM3FFA3)))
							if EFMFPo == "mf":
								MOE1 = float(EM3P1[2])*float(EM3FFA1)
								MOE2 = float(EM3P2[2])*float(EM3FFA2)
								MOE3 = float(EM3P3[2])*float(EM3FFA3)
								MOE = float(MOE1)+float(MOE2)+float(MOE3)
								MFR_o = float(MFM1)/float(MOE)
								MFR = int((round(float(MFR_o), 0)))
								E1_o = float(EM3FFA1) * float(MFR)
								E2_o = float(EM3FFA2) * float(MFR)
								E3_o = float(EM3FFA3) * float(MFR)
								E1 = int((round(float(E1_o), 0)))
								E2 = int((round(float(E2_o), 0)))
								E3 = int((round(float(E3_o), 0)))
								print("")
								print("")
								print("Molecular Formula:")
								print("______________________________")
								print(str(EM3P1[0])+" = "+str(E1))
								print(str(EM3P2[0])+" = "+str(E2))
								print(str(EM3P3[0])+" = "+str(E3))
								print("")
								print("Together: "+str((str(EM3P1[0])+str(E1)+str(EM3P2[0])+str(E2)+str(EM3P3[0])+str(E3))))
								print("______________________________")
								answer = str((str(EM3P1[0])+str(E1)+str(EM3P2[0])+str(E2)+str(EM3P3[0])+str(E3)))
					if EM3C3 < EM3C1:
						if EM3C3 < EM3C2:
							EM3FA1 = float(EM3C1)/float(EM3C3)
							EM3FFA1 = int((round(float(EM3FA1), 0)))
							EM3FA2 = float(EM3C2)/float(EM3C3)
							EM3FFA2 = int((round(float(EM3FA2), 0)))
							EM3FA3 = float(EM3C3)/float(EM3C3)
							EM3FFA3 = int((round(float(EM3FA3), 0)))		
							print("")
							print("Empirical Formula:")
							print("______________________________")
							print(str(EM3P1[0])+" = "+str(EM3FFA1))
							print(str(EM3P2[0])+" = "+str(EM3FFA2))
							print(str(EM3P3[0])+" = "+str(EM3FFA3))
							print("")
							print("Together: "+str((str(EM3P1[0])+str(EM3FFA1)+str(EM3P2[0])+str(EM3FFA2)+str(EM3P3[0]))))
							print("______________________________")
							answer = str((str(EM3P1[0])+str(EM3FFA1)+str(EM3P2[0])+str(EM3FFA2)+str(EM3P3[0])))
							if EFMFPo == "mf":
								MOE1 = float(EM3P1[2])*float(EM3FFA1)
								MOE2 = float(EM3P2[2])*float(EM3FFA2)
								MOE3 = float(EM3P3[2])*float(EM3FFA3)
								MOE = float(MOE1)+float(MOE2)+float(MOE3)
								MFR_o = float(MFM1)/float(MOE)
								MFR = int((round(float(MFR_o), 0)))
								E1_o = float(EM3FFA1) * float(MFR)
								E2_o = float(EM3FFA2) * float(MFR)
								E3_o = float(EM3FFA3) * float(MFR)
								E1 = int((round(float(E1_o), 0)))
								E2 = int((round(float(E2_o), 0)))
								E3 = int((round(float(E3_o), 0)))
								print("")
								print("")
								print("Molecular Formula:")
								print("______________________________")
								print(str(EM3P1[0])+" = "+str(E1))
								print(str(EM3P2[0])+" = "+str(E2))
								print(str(EM3P3[0])+" = "+str(E3))
								print("")
								print("Together: "+str((str(EM3P1[0])+str(E1)+str(EM3P2[0])+str(E2)+str(EM3P3[0])+str(E3))))
								print("______________________________")
								answer = str((str(EM3P1[0])+str(E1)+str(EM3P2[0])+str(E2)+str(EM3P3[0])+str(E3)))
				if EFNO == 4:
					emList=[]
					EM4P1_one = question=input("Enter your first element, percent, & atomic weight (EX: He+5+4): ")
					EM4P1_two = question=input("Enter your second element, percent, & atomic weight (EX: He+5+4): ")
					EM4P1_three = question=input("Enter your third element, percent, & atomic weight (EX: He+5+4): ")
					EM4P1_four = question=input("Enter your fourth element, percent, & atomic weight (EX: He+5+4): ")
					if EFMFPo == "mf":
						MFM1= question = input("Enter the Molar Mass: ")
					
					EM4P1=EM4P1_one.replace(' ', '').split("+")
					EM4P2=EM4P1_two.replace(' ', '').split("+")
					EM4P3=EM4P1_three.replace(' ', '').split("+")
					EM4P4=EM4P1_four.replace(' ', '').split("+")
					
					#0: Reactant, 1: Percent [mass (g)], 2: atomic weight
					
					EM4C1 = float(EM4P1[1])/float(EM4P1[2])
					EM4C2 = float(EM4P2[1])/float(EM4P2[2])
					EM4C3 = float(EM4P3[1])/float(EM4P3[2])
					EM4C4 = float(EM4P4[1])/float(EM4P4[2])
					
					if EM4C1 < EM4C2:
						if EM4C1 < EM4C3:
							if EM4C1 < EM4C4:
								EM4FA1 = float(EM4C1)/float(EM4C1)
								EM4FFA1 = int((round(float(EM4FA1), 0)))
								EM4FA2 = float(EM4C2)/float(EM4C1)
								EM4FFA2 = int((round(float(EM4FA2), 0)))
								EM4FA3 = float(EM4C3)/float(EM4C1)
								EM4FFA3 = int((round(float(EM4FA3), 0)))
								EM4FA4 = float(EM4C4)/float(EM4C1)
								EM4FFA4 = int((round(float(EM4FA4), 0)))		
								print("")
								print("Empirical Formula:")
								print("______________________________")
								print(str(EM4P1[0])+" = "+str(EM4FFA1))
								print(str(EM4P2[0])+" = "+str(EM4FFA2))
								print(str(EM4P3[0])+" = "+str(EM4FFA3))
								print(str(EM4P4[0])+" = "+str(EM4FFA4))
								print("")
								print("Together: "+str((str(EM4P1[0])+str(EM4P2[0])+str(EM4FFA2)+str(EM4P3[0])+str(EM4FFA3)+str(EM4P4[0])+str(EM4FFA4))))
								print("______________________________")
								answer = str((str(EM4P1[0])+str(EM4P2[0])+str(EM4FFA2)+str(EM4P3[0])+str(EM4FFA3)+str(EM4P4[0])+str(EM4FFA4)))
								if EFMFPo == "mf":
									MOE1 = float(EM4P1[2])*float(EM4FFA1)
									MOE2 = float(EM4P2[2])*float(EM4FFA2)
									MOE3 = float(EM4P3[2])*float(EM4FFA3)
									MOE4 = float(EM4P4[2])*float(EM4FFA4)
									MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)
									MFR_o = float(MFM1)/float(MOE)
									MFR = int((round(float(MFR_o), 0)))
									E1_o = float(EM4FFA1) * float(MFR)
									E2_o = float(EM4FFA2) * float(MFR)
									E3_o = float(EM4FFA3) * float(MFR)
									E4_o = float(EM4FFA4) * float(MFR)
									E1 = int((round(float(E1_o), 0)))
									E2 = int((round(float(E2_o), 0)))
									E3 = int((round(float(E3_o), 0)))
									E4 = int((round(float(E4_o), 0)))
									print("")
									print("")
									print("Molecular Formula:")
									print("______________________________")
									print(str(EM4P1[0])+" = "+str(E1))
									print(str(EM4P2[0])+" = "+str(E2))
									print(str(EM4P3[0])+" = "+str(E3))
									print(str(EM4P4[0])+" = "+str(E4))
									print("")
									print("Together: "+str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4))))
									print("______________________________")
									answer = str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4)))
					if EM4C2 < EM4C3:
						if EM4C2 < EM4C1:
							if EM4C2 < EM4C4:
								EM4FA1 = float(EM4C1)/float(EM4C2)
								EM4FFA1 = int((round(float(EM4FA1), 0)))
								EM4FA2 = float(EM4C2)/float(EM4C2)
								EM4FFA2 = int((round(float(EM4FA2), 0)))
								EM4FA3 = float(EM4C3)/float(EM4C2)
								EM4FFA3 = int((round(float(EM4FA3), 0)))
								EM4FA4 = float(EM4C4)/float(EM4C2)
								EM4FFA4 = int((round(float(EM4FA4), 0)))	
								print("")
								print("Empirical Formula:")
								print("______________________________")
								print(str(EM4P1[0])+" = "+str(EM4FFA1))
								print(str(EM4P2[0])+" = "+str(EM4FFA2))
								print(str(EM4P3[0])+" = "+str(EM4FFA3))
								print(str(EM4P4[0])+" = "+str(EM4FFA4))
								print("")
								print("Together: "+str((str(EM4P1[0])+str(EM4FFA1)+str(EM4P2[0])+str(EM4P3[0])+str(EM4FFA3)+str(EM4P4[0])+str(EM4FFA4))))
								print("______________________________")
								answer = str((str(EM4P1[0])+str(EM4FFA1)+str(EM4P2[0])+str(EM4P3[0])+str(EM4FFA3)+str(EM4P4[0])+str(EM4FFA4)))
								if EFMFPo == "mf":
									MOE1 = float(EM4P1[2])*float(EM4FFA1)
									MOE2 = float(EM4P2[2])*float(EM4FFA2)
									MOE3 = float(EM4P3[2])*float(EM4FFA3)
									MOE4 = float(EM4P4[2])*float(EM4FFA4)
									MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)
									MFR_o = float(MFM1)/float(MOE)
									MFR = int((round(float(MFR_o), 0)))
									E1_o = float(EM4FFA1) * float(MFR)
									E2_o = float(EM4FFA2) * float(MFR)
									E3_o = float(EM4FFA3) * float(MFR)
									E4_o = float(EM4FFA4) * float(MFR)
									E1 = int((round(float(E1_o), 0)))
									E2 = int((round(float(E2_o), 0)))
									E3 = int((round(float(E3_o), 0)))
									E4 = int((round(float(E4_o), 0)))
									print("")
									print("")
									print("Molecular Formula:")
									print("______________________________")
									print(str(EM4P1[0])+" = "+str(E1))
									print(str(EM4P2[0])+" = "+str(E2))
									print(str(EM4P3[0])+" = "+str(E3))
									print(str(EM4P4[0])+" = "+str(E4))
									print("")
									print("Together: "+str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4))))
									print("______________________________")
									answer = str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4)))
					if EM4C3 < EM4C1:
						if EM4C3 < EM4C2:
							if EM4C3 < EM4C4:
								EM4FA1 = float(EM4C1)/float(EM4C3)
								EM4FFA1 = int((round(float(EM4FA1), 0)))
								EM4FA2 = float(EM4C2)/float(EM4C3)
								EM4FFA2 = int((round(float(EM4FA2), 0)))
								EM4FA3 = float(EM4C3)/float(EM4C3)
								EM4FFA3 = int((round(float(EM4FA3), 0)))
								EM4FA4 = float(EM4C4)/float(EM4C3)
								EM4FFA4 = int((round(float(EM4FA4), 0)))					
								print("")
								print("Empirical Formula:")
								print("______________________________")
								print(str(EM4P1[0])+" = "+str(EM4FFA1))
								print(str(EM4P2[0])+" = "+str(EM4FFA2))
								print(str(EM4P3[0])+" = "+str(EM4FFA3))
								print(str(EM4P4[0])+" = "+str(EM4FFA4))
								print("")
								print("Together: "+str((str(EM4P1[0])+str(EM4FFA1)+str(EM4P2[0])+str(EM4FFA2)+str(EM4P3[0])+str(EM4P4[0])+str(EM4FFA4))))
								print("______________________________")
								answer = str((str(EM4P1[0])+str(EM4FFA1)+str(EM4P2[0])+str(EM4FFA2)+str(EM4P3[0])+str(EM4P4[0])+str(EM4FFA4)))
								if EFMFPo == "mf":
									MOE1 = float(EM4P1[2])*float(EM4FFA1)
									MOE2 = float(EM4P2[2])*float(EM4FFA2)
									MOE3 = float(EM4P3[2])*float(EM4FFA3)
									MOE4 = float(EM4P4[2])*float(EM4FFA4)
									MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)
									MFR_o = float(MFM1)/float(MOE)
									MFR = int((round(float(MFR_o), 0)))
									E1_o = float(EM4FFA1) * float(MFR)
									E2_o = float(EM4FFA2) * float(MFR)
									E3_o = float(EM4FFA3) * float(MFR)
									E4_o = float(EM4FFA4) * float(MFR)
									E1 = int((round(float(E1_o), 0)))
									E2 = int((round(float(E2_o), 0)))
									E3 = int((round(float(E3_o), 0)))
									E4 = int((round(float(E4_o), 0)))
									print("")
									print("")
									print("Molecular Formula:")
									print("______________________________")
									print(str(EM4P1[0])+" = "+str(E1))
									print(str(EM4P2[0])+" = "+str(E2))
									print(str(EM4P3[0])+" = "+str(E3))
									print(str(EM4P4[0])+" = "+str(E4))
									print("")
									print("Together: "+str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4))))
									print("______________________________")
									answer = str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4)))
					if EM4C4 < EM4C1:
						if EM4C4 < EM4C2:
							if EM4C4 < EM4C3:
								EM4FA1 = float(EM4C1)/float(EM4C4)
								EM4FFA1 = int((round(float(EM4FA1), 0)))
								EM4FA2 = float(EM4C2)/float(EM4C4)
								EM4FFA2 = int((round(float(EM4FA2), 0)))
								EM4FA3 = float(EM4C3)/float(EM4C4)
								EM4FFA3 = int((round(float(EM4FA3), 0)))
								EM4FA4 = float(EM4C4)/float(EM4C4)
								EM4FFA4 = int((round(float(EM4FA4), 0)))					
								print("")
								print("Empirical Formula:")
								print("______________________________")
								print(str(EM4P1[0])+" = "+str(EM4FFA1))
								print(str(EM4P2[0])+" = "+str(EM4FFA2))
								print(str(EM4P3[0])+" = "+str(EM4FFA3))
								print(str(EM4P4[0])+" = "+str(EM4FFA4))
								print("")
								print("Together: "+str((str(EM4P1[0])+str(EM4FFA1)+str(EM4P2[0])+str(EM4FFA2)+str(EM4P3[0])+str(EM4FFA3)+str(EM4P4[0]))))
								print("______________________________")
								answer = str((str(EM4P1[0])+str(EM4FFA1)+str(EM4P2[0])+str(EM4FFA2)+str(EM4P3[0])+str(EM4FFA3)+str(EM4P4[0])))
								if EFMFPo == "mf":
									MOE1 = float(EM4P1[2])*float(EM4FFA1)
									MOE2 = float(EM4P2[2])*float(EM4FFA2)
									MOE3 = float(EM4P3[2])*float(EM4FFA3)
									MOE4 = float(EM4P4[2])*float(EM4FFA4)
									MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)
									MFR_o = float(MFM1)/float(MOE)
									MFR = int((round(float(MFR_o), 0)))
									E1_o = float(EM4FFA1) * float(MFR)
									E2_o = float(EM4FFA2) * float(MFR)
									E3_o = float(EM4FFA3) * float(MFR)
									E4_o = float(EM4FFA4) * float(MFR)
									E1 = int((round(float(E1_o), 0)))
									E2 = int((round(float(E2_o), 0)))
									E3 = int((round(float(E3_o), 0)))
									E4 = int((round(float(E4_o), 0)))
									print("")
									print("")
									print("Molecular Formula:")
									print("______________________________")
									print(str(EM4P1[0])+" = "+str(E1))
									print(str(EM4P2[0])+" = "+str(E2))
									print(str(EM4P3[0])+" = "+str(E3))
									print(str(EM4P4[0])+" = "+str(E4))
									print("")
									print("Together: "+str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4))))
									print("______________________________")
									answer = str((str(EM4P1[0])+str(E1)+str(EM4P2[0])+str(E2)+str(EM4P3[0])+str(E3)+str(EM4P4[0])+str(E4)))
				if EFNO == 5:
					emList=[]
					EM5P1_one = question=input("Enter your first element, percent, & atomic weight (EX: He+5+4): ")
					EM5P1_two = question=input("Enter your second element, percent, & atomic weight (EX: He+5+4): ")
					EM5P1_three = question=input("Enter your third element, percent, & atomic weight (EX: He+5+4): ")
					EM5P1_four = question=input("Enter your fourth element, percent, & atomic weight (EX: He+5+4): ")
					EM5P1_five = question=input("Enter your fifth element, percent, & atomic weight (EX: He+5+4): ")
					if EFMFPo == "mf":
						MFM1= question = input("Enter the Molar Mass: ")
					
					EM5P1=EM5P1_one.replace(' ', '').split("+")
					EM5P2=EM5P1_two.replace(' ', '').split("+")
					EM5P3=EM5P1_three.replace(' ', '').split("+")
					EM5P4=EM5P1_four.replace(' ', '').split("+")
					EM5P5=EM5P1_five.replace(' ', '').split("+")
					
					#0: Reactant, 1: Percent [mass (g)], 2: atomic weight
					
					EM5C1 = float(EM5P1[1])/float(EM5P1[2])
					EM5C2 = float(EM5P2[1])/float(EM5P2[2])
					EM5C3 = float(EM5P3[1])/float(EM5P3[2])
					EM5C4 = float(EM5P4[1])/float(EM5P4[2])
					EM5C5 = float(EM5P5[1])/float(EM5P5[2])
					
					if EM5C1 < EM5C2:
						if EM5C1 < EM5C3:
							if EM5C1 < EM5C4:
								if EM5C1 < EM5C5:
									EM5FA1 = float(EM5C1)/float(EM5C1)
									EM5FFA1 = int((round(float(EM5FA1), 0)))
									EM5FA2 = float(EM5C2)/float(EM5C1)
									EM5FFA2 = int((round(float(EM5FA2), 0)))
									EM5FA3 = float(EM5C3)/float(EM5C1)
									EM5FFA3 = int((round(float(EM5FA3), 0)))
									EM5FA4 = float(EM5C4)/float(EM5C1)
									EM5FFA4 = int((round(float(EM5FA4), 0)))
									EM5FA5 = float(EM5C5)/float(EM5C1)
									EM5FFA5 = int((round(float(EM5FA5), 0)))	
									print("Empirical Formula:")	
									print("")
									print("______________________________")
									print(str(EM5P1[0])+" = "+str(EM5FFA1))
									print(str(EM5P2[0])+" = "+str(EM5FFA2))
									print(str(EM5P3[0])+" = "+str(EM5FFA3))
									print(str(EM5P4[0])+" = "+str(EM5FFA4))
									print(str(EM5P5[0])+" = "+str(EM5FFA5))
									print("")
									print("Together: "+str((str(EM5P1[0])+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0])+str(EM5FFA5))))
									print("______________________________")
									answer = str((str(EM5P1[0])+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0])+str(EM5FFA5)))
									if EFMFPo == "mf":
										MOE1 = float(EM5P1[2])*float(EM5FFA1)
										MOE2 = float(EM5P2[2])*float(EM5FFA2)
										MOE3 = float(EM5P3[2])*float(EM5FFA3)
										MOE4 = float(EM5P4[2])*float(EM5FFA4)
										MOE5 = float(EM5P5[2])*float(EM5FFA5)
										MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)+float(MOE5)
										MFR_o = float(MFM1)/float(MOE)
										MFR = int((round(float(MFR_o), 0)))
										E1_o = float(EM5FFA1) * float(MFR)
										E2_o = float(EM5FFA2) * float(MFR)
										E3_o = float(EM5FFA3) * float(MFR)
										E4_o = float(EM5FFA4) * float(MFR)
										E5_o = float(EM5FFA5) * float(MFR)
										E1 = int((round(float(E1_o), 0)))
										E2 = int((round(float(E2_o), 0)))
										E3 = int((round(float(E3_o), 0)))
										E4 = int((round(float(E4_o), 0)))
										E5 = int((round(float(E5_o), 0)))
										print("")
										print("")
										print("Molecular Formula:")
										print("______________________________")
										print(str(EM5P1[0])+" = "+str(E1))
										print(str(EM5P2[0])+" = "+str(E2))
										print(str(EM5P3[0])+" = "+str(E3))
										print(str(EM5P4[0])+" = "+str(E4))
										print(str(EM5P5[0])+" = "+str(E5))
										print("")
										print("Together: "+str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5))))
										print("______________________________")
										answer = str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5)))
					if EM5C2 < EM5C1:
						if EM5C2 < EM5C3:
							if EM5C2 < EM5C4:
								if EM5C2 < EM5C5:
									EM5FA1 = float(EM5C1)/float(EM5C2)
									EM5FFA1 = int((round(float(EM5FA1), 0)))
									EM5FA2 = float(EM5C2)/float(EM5C2)
									EM5FFA2 = int((round(float(EM5FA2), 0)))
									EM5FA3 = float(EM5C3)/float(EM5C2)
									EM5FFA3 = int((round(float(EM5FA3), 0)))
									EM5FA4 = float(EM5C4)/float(EM5C2)
									EM5FFA4 = int((round(float(EM5FA4), 0)))
									EM5FA5 = float(EM5C5)/float(EM5C2)
									EM5FFA5 = int((round(float(EM5FA5), 0)))		
									print("")
									print("Empirical Formula:")
									print("______________________________")
									print(str(EM5P1[0])+" = "+str(EM5FFA1))
									print(str(EM5P2[0])+" = "+str(EM5FFA2))
									print(str(EM5P3[0])+" = "+str(EM5FFA3))
									print(str(EM5P4[0])+" = "+str(EM5FFA4))
									print(str(EM5P5[0])+" = "+str(EM5FFA5))
									print("")
									print("Together: "+str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0])+str(EM5FFA5))))
									print("______________________________")
									answer = str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0])+str(EM5FFA5)))
									if EFMFPo == "mf":
										MOE1 = float(EM5P1[2])*float(EM5FFA1)
										MOE2 = float(EM5P2[2])*float(EM5FFA2)
										MOE3 = float(EM5P3[2])*float(EM5FFA3)
										MOE4 = float(EM5P4[2])*float(EM5FFA4)
										MOE5 = float(EM5P5[2])*float(EM5FFA5)
										MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)+float(MOE5)
										MFR_o = float(MFM1)/float(MOE)
										MFR = int((round(float(MFR_o), 0)))
										E1_o = float(EM5FFA1) * float(MFR)
										E2_o = float(EM5FFA2) * float(MFR)
										E3_o = float(EM5FFA3) * float(MFR)
										E4_o = float(EM5FFA4) * float(MFR)
										E5_o = float(EM5FFA5) * float(MFR)
										E1 = int((round(float(E1_o), 0)))
										E2 = int((round(float(E2_o), 0)))
										E3 = int((round(float(E3_o), 0)))
										E4 = int((round(float(E4_o), 0)))
										E5 = int((round(float(E5_o), 0)))
										print("")
										print("")
										print("Molecular Formula:")
										print("______________________________")
										print(str(EM5P1[0])+" = "+str(E1))
										print(str(EM5P2[0])+" = "+str(E2))
										print(str(EM5P3[0])+" = "+str(E3))
										print(str(EM5P4[0])+" = "+str(E4))
										print(str(EM5P5[0])+" = "+str(E5))
										print("")
										print("Together: "+str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5))))
										print("______________________________")
										answer = str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5)))
					if EM5C3 < EM5C1:
						if EM5C3 < EM5C2:
							if EM5C3 < EM5C4:
								if EM5C3 < EM5C5:
									EM5FA1 = float(EM5C1)/float(EM5C3)
									EM5FFA1 = int((round(float(EM5FA1), 0)))
									EM5FA2 = float(EM5C2)/float(EM5C3)
									EM5FFA2 = int((round(float(EM5FA2), 0)))
									EM5FA3 = float(EM5C3)/float(EM5C3)
									EM5FFA3 = int((round(float(EM5FA3), 0)))
									EM5FA4 = float(EM5C4)/float(EM5C3)
									EM5FFA4 = int((round(float(EM5FA4), 0)))
									EM5FA5 = float(EM5C5)/float(EM5C3)
									EM5FFA5 = int((round(float(EM5FA5), 0)))
									print("")
									print("Empirical Formula:")
									print("______________________________")
									print(str(EM5P1[0])+" = "+str(EM5FFA1))
									print(str(EM5P2[0])+" = "+str(EM5FFA2))
									print(str(EM5P3[0])+" = "+str(EM5FFA3))
									print(str(EM5P4[0])+" = "+str(EM5FFA4))
									print(str(EM5P5[0])+" = "+str(EM5FFA5))
									print("")
									print("Together: "+str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0])+str(EM5FFA5))))
									print("______________________________")
									answer = str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0])+str(EM5FFA5)))
									if EFMFPo == "mf":
										MOE1 = float(EM5P1[2])*float(EM5FFA1)
										MOE2 = float(EM5P2[2])*float(EM5FFA2)
										MOE3 = float(EM5P3[2])*float(EM5FFA3)
										MOE4 = float(EM5P4[2])*float(EM5FFA4)
										MOE5 = float(EM5P5[2])*float(EM5FFA5)
										MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)+float(MOE5)
										MFR_o = float(MFM1)/float(MOE)
										MFR = int((round(float(MFR_o), 0)))
										E1_o = float(EM5FFA1) * float(MFR)
										E2_o = float(EM5FFA2) * float(MFR)
										E3_o = float(EM5FFA3) * float(MFR)
										E4_o = float(EM5FFA4) * float(MFR)
										E5_o = float(EM5FFA5) * float(MFR)
										E1 = int((round(float(E1_o), 0)))
										E2 = int((round(float(E2_o), 0)))
										E3 = int((round(float(E3_o), 0)))
										E4 = int((round(float(E4_o), 0)))
										E5 = int((round(float(E5_o), 0)))
										print("")
										print("")
										print("Molecular Formula:")
										print("______________________________")
										print(str(EM5P1[0])+" = "+str(E1))
										print(str(EM5P2[0])+" = "+str(E2))
										print(str(EM5P3[0])+" = "+str(E3))
										print(str(EM5P4[0])+" = "+str(E4))
										print(str(EM5P5[0])+" = "+str(E5))
										print("")
										print("Together: "+str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5))))
										print("______________________________")
										answer = str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5)))
					if EM5C4 < EM5C1:
						if EM5C4 < EM5C2:
							if EM5C4 < EM5C3:
								if EM5C4 < EM5C5:
									EM5FA1 = float(EM5C1)/float(EM5C4)
									EM5FFA1 = int((round(float(EM5FA1), 0)))
									EM5FA2 = float(EM5C2)/float(EM5C4)
									EM5FFA2 = int((round(float(EM5FA2), 0)))
									EM5FA3 = float(EM5C3)/float(EM5C4)
									EM5FFA3 = int((round(float(EM5FA3), 0)))
									EM5FA4 = float(EM5C4)/float(EM5C4)
									EM5FFA4 = int((round(float(EM5FA4), 0)))
									EM5FA5 = float(EM5C5)/float(EM5C4)
									EM5FFA5 = int((round(float(EM5FA5), 0)))		
									print("")
									print("Empirical Formula:")
									print("______________________________")
									print(str(EM5P1[0])+" = "+str(EM5FFA1))
									print(str(EM5P2[0])+" = "+str(EM5FFA2))
									print(str(EM5P3[0])+" = "+str(EM5FFA3))
									print(str(EM5P4[0])+" = "+str(EM5FFA4))
									print(str(EM5P5[0])+" = "+str(EM5FFA5))
									print("")
									print("Together: "+str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5P5[0])+str(EM5FFA5))))
									print("______________________________")
									answer = str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5P5[0])+str(EM5FFA5)))
									if EFMFPo == "mf":
										MOE1 = float(EM5P1[2])*float(EM5FFA1)
										MOE2 = float(EM5P2[2])*float(EM5FFA2)
										MOE3 = float(EM5P3[2])*float(EM5FFA3)
										MOE4 = float(EM5P4[2])*float(EM5FFA4)
										MOE5 = float(EM5P5[2])*float(EM5FFA5)
										MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)+float(MOE5)
										MFR_o = float(MFM1)/float(MOE)
										MFR = int((round(float(MFR_o), 0)))
										E1_o = float(EM5FFA1) * float(MFR)
										E2_o = float(EM5FFA2) * float(MFR)
										E3_o = float(EM5FFA3) * float(MFR)
										E4_o = float(EM5FFA4) * float(MFR)
										E5_o = float(EM5FFA5) * float(MFR)
										E1 = int((round(float(E1_o), 0)))
										E2 = int((round(float(E2_o), 0)))
										E3 = int((round(float(E3_o), 0)))
										E4 = int((round(float(E4_o), 0)))
										E5 = int((round(float(E5_o), 0)))
										print("")
										print("")
										print("Molecular Formula:")
										print("______________________________")
										print(str(EM5P1[0])+" = "+str(E1))
										print(str(EM5P2[0])+" = "+str(E2))
										print(str(EM5P3[0])+" = "+str(E3))
										print(str(EM5P4[0])+" = "+str(E4))
										print(str(EM5P5[0])+" = "+str(E5))
										print("")
										print("Together: "+str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5))))
										print("______________________________")
										answer = str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5)))				
					if EM5C5 < EM5C1:
						if EM5C5 < EM5C2:
							if EM5C5 < EM5C3:
								if EM5C5 < EM5C4:
									EM5FA1 = float(EM5C1)/float(EM5C5)
									EM5FFA1 = int((round(float(EM5FA1), 0)))
									EM5FA2 = float(EM5C2)/float(EM5C5)
									EM5FFA2 = int((round(float(EM5FA2), 0)))
									EM5FA3 = float(EM5C3)/float(EM5C5)
									EM5FFA3 = int((round(float(EM5FA3), 0)))
									EM5FA4 = float(EM5C4)/float(EM5C5)
									EM5FFA4 = int((round(float(EM5FA4), 0)))
									EM5FA5 = float(EM5C5)/float(EM5C5)
									EM5FFA5 = int((round(float(EM5FA5), 0)))		
									print("")
									print("Empirical Formula:")
									print("______________________________")
									print(str(EM5P1[0])+" = "+str(EM5FFA1))
									print(str(EM5P2[0])+" = "+str(EM5FFA2))
									print(str(EM5P3[0])+" = "+str(EM5FFA3))
									print(str(EM5P4[0])+" = "+str(EM5FFA4))
									print(str(EM5P5[0])+" = "+str(EM5FFA5))
									print("")
									print("Together: "+str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0]))))
									print("______________________________")
									answer = str((str(EM5P1[0])+str(EM5FFA1)+str(EM5P2[0])+str(EM5FFA2)+str(EM5P3[0])+str(EM5FFA3)+str(EM5P4[0])+str(EM5FFA4)+str(EM5P5[0])))
									if EFMFPo == "mf":
										MOE1 = float(EM5P1[2])*float(EM5FFA1)
										MOE2 = float(EM5P2[2])*float(EM5FFA2)
										MOE3 = float(EM5P3[2])*float(EM5FFA3)
										MOE4 = float(EM5P4[2])*float(EM5FFA4)
										MOE5 = float(EM5P5[2])*float(EM5FFA5)
										MOE = float(MOE1)+float(MOE2)+float(MOE3)+float(MOE4)+float(MOE5)
										MFR_o = float(MFM1)/float(MOE)
										MFR = int((round(float(MFR_o), 0)))
										E1_o = float(EM5FFA1) * float(MFR)
										E2_o = float(EM5FFA2) * float(MFR)
										E3_o = float(EM5FFA3) * float(MFR)
										E4_o = float(EM5FFA4) * float(MFR)
										E5_o = float(EM5FFA5) * float(MFR)
										E1 = int((round(float(E1_o), 0)))
										E2 = int((round(float(E2_o), 0)))
										E3 = int((round(float(E3_o), 0)))
										E4 = int((round(float(E4_o), 0)))
										E5 = int((round(float(E5_o), 0)))
										print("")
										print("")
										print("Molecular Formula:")
										print("______________________________")
										print(str(EM5P1[0])+" = "+str(E1))
										print(str(EM5P2[0])+" = "+str(E2))
										print(str(EM5P3[0])+" = "+str(E3))
										print(str(EM5P4[0])+" = "+str(E4))
										print(str(EM5P5[0])+" = "+str(E5))
										print("")
										print("Together: "+str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5))))
										print("______________________________")
										answer = str((str(EM5P1[0])+str(E1)+str(EM5P2[0])+str(E2)+str(EM5P3[0])+str(E3)+str(EM5P4[0])+str(E4)+str(EM5P5[0])+str(E5)))
				print("")
				SaveQ = input("Do you want to save the EF or MF? (y or n): ").lower()
				if SaveQ == "y":
					if len(Save1) == 0:
						Save1.append(answer)								
					elif len(Save2) == 0:
						Save2.append(answer)								
					elif len(Save3) == 0:
						Save3.append(answer)								
					elif len(Save4) == 0:
						Save4.append(answer)								
					elif len(Save5) == 0:
						Save5.append(answer)								
					elif len(Save6) == 0:
						Save6.append(answer)								
					elif len(Save7) == 0:
						Save7.append(answer)								
					elif len(Save8) == 0:
						Save8.append(answer)								
					elif len(Save9) == 0:
						Save9.append(answer)								
					elif len(Save10) == 0:
						Save10.append(answer)
					print("(Saved)")
					time.sleep(.25)								
				if SaveQ == "n":
					x=1				
			if chemistry_machine == "m":
				#Limiting and Excess Reagents/Reactants/PQ/LR:
				print("________________________________________________________________________________________________________")
				reactNO = int(input("How many reactants do you have? (2 or 3): "))
				print("")
				if reactNO == 2:
					reactant_one = input("Enter your first reactant, quantity (g), atomic weight, & coefficient (EX: He+5+4+2): ")
					reactant_two = input("Enter your second reactant, quantity (g), atomic weight, & coefficient (EX: He+5+4+2): ")
					product = input("Enter your given product, atomic weight, & coefficient (EX: He+4+2): ")
					R1=reactant_one.replace(' ', '').split("+")
					R2=reactant_two.replace(' ', '').split("+")
					P1=product.replace(' ', '').split("+")
					# 0:reactant, 1: quantity(g), 2: atomic weight, 3: number of moles in ratio
					# 0:product, 1: atomic weight, 2: number of moles in ratio
					CA1E1=float(R1[1])/float(R1[2])
					CA1E2=float(CA1E1)*float(P1[2])
					CA1E3=float(CA1E2)/float(R1[3])
					HMP1=float(CA1E3)*float(P1[1])
					NOEM1=float(HMP1)/float(P1[1])
					CA2E1=float(R2[1])/float(R2[2])
					CA2E2=float(CA2E1)*float(P1[2])
					CA2E3=float(CA2E2)/float(R2[3])
					HMP2=float(CA2E3)*float(P1[1])
					NOEM2=float(HMP2)/float(P1[1])
					if float(CA1E3) < float(CA2E3):
						CS1E1 = float(CA1E3)*float(R2[3])
						CS1E2 = float(CS1E1)/float(P1[2])
						CS1E3 = float(CS1E2)*float(R2[2])
						HME1 = float(R2[1])-float(CS1E3)
						NOM1 = float(HME1)/float(R2[2])
						print("")
						print("______________________________")
						print("Quantity of Product: ", str(HMP1), "g", "("+str(NOEM1)+" mols)")
						print("Limiting Reagent: ", str(R1[0]))
						print("Excess Reagent: ", str(R2[0]))
						print("Leftover Reagent: ", str(HME1), "g", "("+str(NOM1)+" mols)")
						print("______________________________")
					if float(CA1E3) > float(CA2E3):
						CS2E1 = float(CA2E3)*float(R1[3])
						CS2E2 = float(CS2E1)/float(P1[2])
						CS2E3 = float(CS2E2)*float(R1[2])
						HME2 = float(R1[1])-float(CS2E3)
						NOM2 = float(HME2)/float(R1[2])
						print("")
						print("______________________________")
						print("Quantity of Product: ", str(HMP2), "g", "("+str(NOEM2)+" mols)")
						print("Limiting Reagent: ", str(R2[0]))
						print("Excess Reagent: ", str(R1[0]))
						print("Leftover Reagent: ", str(HME2), "g", "("+str(NOM2)+" mols)")
						print("______________________________")
				if reactNO == 3:
					reactant_one = input("Enter your first reactant, quantity (g), atomic weight, & coefficient (EX: He+5+4+2): ")
					reactant_two = input("Enter your second reactant, quantity (g), atomic weight, & coefficient (EX: He+5+4+2): ")
					reactant_three = input("Enter your third reactant, quantity (g), atomic weight, & coefficient (EX: He+5+4+2): ")
					product = input("Enter your given product, atomic weight, & coefficient (EX: He+4+2): ")
					R1=reactant_one.replace(' ', '').split("+")
					R2=reactant_two.replace(' ', '').split("+")
					R3=reactant_three.replace(' ', '').split("+")
					P1=product.replace(' ', '').split("+")
					# 0:reactant, 1: quantity(g), 2: atomic weight, 3: number of moles in ratio
					# 0:product, 1: atomic weight, 2: number of moles in ratio
					CA1E1=float(R1[1])/float(R1[2])
					CA1E2=float(CA1E1)*float(P1[2])
					CA1E3=float(CA1E2)/float(R1[3])
					HMP1=float(CA1E3)*float(P1[1])
					#To Use Mols:
					NOEM1=float(HMP1)/float(P1[1])			
					CA2E1=float(R2[1])/float(R2[2])
					CA2E2=float(CA2E1)*float(P1[2])
					CA2E3=float(CA2E2)/float(R2[3])
					HMP2=float(CA2E3)*float(P1[1])
					#To Use Mols:
					NOEM2=float(HMP2)/float(P1[1])	
					CA3E1=float(R3[1])/float(R3[2])
					CA3E2=float(CA3E1)*float(P1[2])
					CA3E3=float(CA3E2)/float(R3[3])
					HMP3=float(CA3E3)*float(P1[1])
					#To Use Mols:
					NOEM3=float(HMP3)/float(P1[1])	
					# 0:reactant, 1: quantity(g), 2: atomic weight, 3: number of moles in ratio
					# 0:product, 1: atomic weight, 2: number of moles in ratio
					if HMP1 < HMP2:
						if HMP1 < HMP3:
							CS1E1 = float(CA1E3)*float(R2[3])
							CS1E2 = float(CS1E1)/float(P1[2])
							CS1E3 = float(CS1E2)*float(R2[2])
							HME1 = float(R2[1])-float(CS1E3)
							NOM1 = float(HME1)/float(R2[2])

							CS1E12 = float(CA1E3)*float(R3[3])
							CS1E22 = float(CS1E12)/float(P1[2])
							CS1E32 = float(CS1E22)*float(R3[2])
							HME12 = float(R3[1])-float(CS1E32)
							NOM12 = float(HME12)/float(R3[2])
							print("")
							print("")
							print("______________________________")
							print("Quantity of Product: ", str(HMP1), "g", "("+str(NOEM1)+" mols)")
							print("Limiting Reagent: ", str(R1[0]))
							print("Excess Reagent: ", str(R2[0])+" + "+ str(R3[0]))
							print("Leftover Reagent"+"("+str(R2[0])+")"+": ", str(HME1), "g", "("+str(NOM1)+" mols)")
							print("Leftover Reagent"+"("+str(R3[0])+")"+": ", str(HME12), "g", "("+str(NOM12)+" mols)")
							print("______________________________")		
					if HMP2 < HMP1:
						if HMP2 < HMP3:
							CS2E1 = float(CA2E3)*float(R1[3])
							CS2E2 = float(CS2E1)/float(P1[2])
							CS2E3 = float(CS2E2)*float(R1[2])
							HME2 = float(R1[1])-float(CS2E3)
							NOM2 = float(HME2)/float(R1[2])
							
							CS2E12 = float(CA2E3)*float(R3[3])
							CS2E22 = float(CS2E12)/float(P1[2])
							CS2E32 = float(CS2E22)*float(R3[2])
							HME22 = float(R3[1])-float(CS2E32)
							NOM22 = float(HME22)/float(R3[2])
							print("")
							print("")
							print("______________________________")
							print("Quantity of Product: ", str(HMP1), "g", "("+str(NOEM1)+" mols)")
							print("Limiting Reagent: ", str(R2[0]))
							print("Excess Reagent: ", str(R1[0])+" + "+ str(R3[0]))
							print("Leftover Reagent"+"("+str(R1[0])+")"+": ", str(HME2), "g", "("+str(NOM2)+" mols)")
							print("Leftover Reagent"+"("+str(R3[0])+")"+": ", str(HME22), "g", "("+str(NOM22)+" mols)")
							print("______________________________")
							
					if HMP3 < HMP1:
						if HMP3 < HMP2:
							CS2E1 = float(CA3E3)*float(R1[3])
							CS2E2 = float(CS2E1)/float(P1[2])
							CS2E3 = float(CS2E2)*float(R1[2])
							HME2 = float(R1[1])-float(CS2E3)
							NOM2 = float(HME2)/float(R1[2])
							
							CS2E12 = float(CA3E3)*float(R2[3])
							CS2E22 = float(CS2E12)/float(P1[2])
							CS2E32 = float(CS2E22)*float(R2[2])
							HME22 = float(R2[1])-float(CS2E32)
							NOM22 = float(HME22)/float(R2[2])
							print("")
							print("")
							print("______________________________")
							print("Quantity of Product: ", str(HMP1), "g", "("+str(NOEM1)+" mols)")
							print("Limiting Reagent: ", str(R3[0]))
							print("Excess Reagent: ", str(R1[0])+" + "+ str(R2[0]))
							print("Leftover Reagent"+"("+str(R1[0])+")"+": ", str(HME2), "g", "("+str(NOM2)+" mols)")
							print("Leftover Reagent"+"("+str(R2[0])+")"+": ", str(HME22), "g", "("+str(NOM22)+" mols)")
							print("______________________________")										
			if chemistry_machine == "ei":
				print("")
				print("________________________________________________________________________________________________________")
				Start=input("Enter an element: ").lower()
				print("")
				print("")
				if Start == "h":
					Start="hydrogen"
				if Start == "he":
					Start="helium"
				if Start == "li":
					Start="lithium"
				if Start == "be":
					Start="beryllium"
				if Start == "b":
					Start="boron"
				if Start == "c":	
					Start="carbon"
				if Start == "n":	
					Start="nitrogen"
				if Start == "o":
					Start="oxygen"
				if Start == "f":	
					Start="fluorine"
				if Start == "ne":	
					Start="neon"
				if Start == "na":	
					Start="sodium"
				if Start == "mg":	
					Start="magnesium"
				if Start == "al":	
					Start="aluminum"
				if Start == "si":	
					Start="silicon"
				if Start == "p":	
					Start="phosphorus"
				if Start == "s":	
					Start="sulfur"
				if Start == "cl":	
					Start="chlorine"
				if Start == "ar":
					Start="argon"
				if Start == "k":
					Start="potassium"
				if Start == "ca":
					Start="calcium"
				if Start == "sc":	
					Start="scandium"
				if Start == "ti":	
					Start="titanium"
				if Start == "v":	
					Start="vanadium"
				if Start == "cr":	
					Start="chromium"
				if Start == "mn":	
					Start="manganese"
				if Start == "fe":	
					Start="iron"
				if Start == "co":	
					Start="cobalt"
				if Start == "ni":	
					Start="nickel"
				if Start == "cu":	
					Start="copper"
				if Start == "zn":	
					Start="zinc"
				if Start == "ga":	
					Start="gallium"
				if Start == "ge":	
					Start="germanium"
				if Start == "as":	
					Start="arsenic"
				if Start == "se":	
					Start="selenium"
				if Start == "br":	
					Start="bromine"
				if Start == "kr":	
					Start="krypton"
				if Start == "rb":	
					Start="rubidium"
				if Start == "sr":	
					Start="strontium"
				if Start == "y":	
					Start="yttrium"
				if Start == "zr":	
					Start="zirconium"
				if Start == "nb":	
					Start="niobium"
				if Start == "mo":	
					Start="molybdenum"
				if Start == "tc":	
					Start="technetium"
				if Start == "ru":	
					Start="ruthenium"
				if Start == "rh":	
					Start="rhodium"
				if Start == "pd":	
					Start="palladium"
				if Start == "ag":	
					Start="silver"
				if Start == "cd":	
					Start="cadmium"
				if Start == "in":	
					Start="indium"
				if Start == "sn":	
					Start="tin"
				if Start == "sb":	
					Start="antimony"
				if Start == "te":	
					Start="tellurium"
				if Start == "i":	
					Start="iodine"
				if Start == "xe":	
					Start="xenon"
				if Start == "cs":	
					Start="caesium"
				if Start == "ba":	
					Start="barium"
				if Start == "la":	
					Start="lanthanum"
				if Start == "ce":
					Start="cerium"
				if Start == "pr":	
					Start="praseodymium"
				if Start == "nd":	
					Start="neodymium"
				if Start == "pm":	
					Start="promethium"
				if Start == "sm":	
					Start="samarium"
				if Start == "eu":	
					Start="europium"
				if Start == "gd":	
					Start="gadolinium"
				if Start == "tb":	
					Start="terbium"
				if Start == "dy":	
					Start="dysprosium"
				if Start == "ho":	
					Start="holmium"
				if Start == "er":	
					Start="erbium"
				if Start == "tm":	
					Start="thulium"
				if Start == "yb":	
					Start="ytterbium"
				if Start == "lu":	
					Start="lutetium"
				if Start == "hf":	
					Start="hafnium"
				if Start == "ta":	
					Start="tantalum"
				if Start == "w":	
					Start="tungsten"
				if Start == "re":	
					Start="rhenium"
				if Start == "os":	
					Start="osmium"
				if Start == "ir":	
					Start="iridium"
				if Start == "pt":	
					Start="platinum"
				if Start == "au":	
					Start="gold"
				if Start == "hg":	
					Start="mercury"
				if Start == "tl":	
					Start="thallium"
				if Start == "pb":	
					Start="lead"
				if Start == "bi":	
					Start="bismuth"
				if Start == "po":	
					Start="polonium"
				if Start == "at":	
					Start="astatine"
				if Start == "rn":	
					Start="radon"
				if Start == "fr":	
					Start="francium"
				if Start == "ra":	
					Start="radium"
				if Start == "ac":	
					Start="actinium"
				if Start == "th":	
					Start="thorium"
				if Start == "pa":	
					Start="protactinium"
				if Start == "u":	
					Start="uranium"
				if Start == "np":	
					Start="neptunium"
				if Start == "pu":	
					Start="plutonium"
				if Start == "am":	
					Start="americium"
				if Start == "cm":	
					Start="curium"
				if Start == "bk":	
					Start="berkelium"
				if Start == "cf":	
					Start="californium"
				if Start == "es":	
					Start="einsteinium"
				if Start == "fm":	
					Start="fermium"
				if Start == "md":	
					Start="mendelevium"
				if Start == "no":	
					Start="nobelium"
				if Start == "lr":	
					Start="lawrencium"
				if Start == "rf":	
					Start="rutherfordium"
				if Start == "db":	
					Start="dubnium"
				if Start == "sg":	
					Start="seaborgium"
				if Start == "bh":
					Start="bohrium"
				if Start == "hs":	
					Start="hassium"
				if Start == "mt":	
					Start="meitnerium"
				if Start == "ds":	
					Start="darmstadtium"
				if Start == "rg":	
					Start="roentgenium"
				if Start == "cn":	
					Start="copernicium"
				if Start == "nh":	
					Start="nihonium"
				if Start == "fl":	
					Start="flerovium"
				if Start == "mc":	
					Start="moscovium"
				if Start == "lv":	
					Start="livermorium"
				if Start == "ts":	
					Start="tennessine"
				if Start == "og":
					Start="oganesson"
				if Start == "hydrogen":
					print("")
					print("Hydrogen:")
					print("______________________________")
					print("Atomic Number: ", Hydrogen["atomicNO"])
					print("Atomic Weight: ", Hydrogen["atomicWeight"])
					print("Electron Configuration: ", Hydrogen["electronConfig"])
					print("Valence Electrons: ", Hydrogen["valElectrons"])
					print("Type of Element: ", Hydrogen["Type"])
					print("Element Symbol: ", Hydrogen["elementSymbol"])
					print("Density: ", Hydrogen["density"], "g/l")
					print("Melting Point: ", Hydrogen["meltingPoint"])
					print("Boiling Point: ", Hydrogen["boilingPoint"])
					print("______________________________")
				if Start == "helium":
					print("")
					print("Helium:")
					print("______________________________")
					print("Atomic Number: ", Helium["atomicNO"])
					print("Atomic Weight: ", Helium["atomicWeight"])
					print("Electron Configuration: ", Helium["electronConfig"])
					print("Valence Electrons: ", Helium["valElectrons"])
					print("Type of Element: ", Helium["Type"])
					print("Element Symbol: ", Helium["elementSymbol"])
					print("Density: ", Helium["density"], "g/l")
					print("Melting Point: ", Helium["meltingPoint"])
					print("Boiling Point: ", Helium["boilingPoint"])
					print("______________________________")
				if Start == "lithium":
					print("")
					print("Lithium:")
					print("______________________________")
					print("Atomic Number: ", Lithium["atomicNO"])
					print("Atomic Weight: ", Lithium["atomicWeight"])
					print("Electron Configuration: ", Lithium["electronConfig"])
					print("Valence Electrons: ", Lithium["valElectrons"])
					print("Type of Element: ", Lithium["Type"])
					print("Element Symbol: ", Lithium["elementSymbol"])
					print("Density: ", Lithium["density"], "g/cm3")
					print("Melting Point: ", Lithium["meltingPoint"])
					print("Boiling Point: ", Lithium["boilingPoint"])
					print("______________________________")
				if Start == "beryllium":
					print("")
					print("Beryllium:")
					print("______________________________")
					print("Atomic Number: ", Beryllium["atomicNO"])
					print("Atomic Weight: ", Beryllium["atomicWeight"])
					print("Electron Configuration: ", Beryllium["electronConfig"])
					print("Valence Electrons: ", Beryllium["valElectrons"])
					print("Type of Element: ", Beryllium["Type"])
					print("Element Symbol: ", Beryllium["elementSymbol"])
					print("Density: ", Beryllium["density"], "g/cm3")
					print("Melting Point: ", Beryllium["meltingPoint"])
					print("Boiling Point: ", Beryllium["boilingPoint"])
					print("______________________________")
				if Start == "boron":
					print("")
					print("Boron:")
					print("______________________________")
					print("Atomic Number: ", Boron["atomicNO"])
					print("Atomic Weight: ", Boron["atomicWeight"])
					print("Electron Configuration: ", Boron["electronConfig"])
					print("Valence Electrons: ", Boron["valElectrons"])
					print("Type of Element: ", Boron["Type"])
					print("Element Symbol: ", Boron["elementSymbol"])
					print("Density: ", Boron["density"], "g/l")
					print("Melting Point: ", Boron["meltingPoint"])
					print("Boiling Point: ", Boron["boilingPoint"])
					print("______________________________")
				if Start == "carbon":
					print("")
					print("Carbon:")
					print("______________________________")
					print("Atomic Number: ", Carbon["atomicNO"])
					print("Atomic Weight: ", Carbon["atomicWeight"])
					print("Electron Configuration: ", Carbon["electronConfig"])
					print("Valence Electrons: ", Carbon["valElectrons"])
					print("Type of Element: ", Carbon["Type"])
					print("Element Symbol: ", Carbon["elementSymbol"])
					print("Density: ", Carbon["density"], "g/l")
					print("Melting Point: ", Carbon["meltingPoint"])
					print("Boiling Point: ", Carbon["boilingPoint"])
					print("______________________________")
				if Start == "nitrogen":
					print("")
					print("Nitrogen:")
					print("______________________________")
					print("Atomic Number: ", Nitrogen["atomicNO"])
					print("Atomic Weight: ", Nitrogen["atomicWeight"])
					print("Electron Configuration: ", Nitrogen["electronConfig"])
					print("Valence Electrons: ", Nitrogen["valElectrons"])
					print("Type of Element: ", Nitrogen["Type"])
					print("Element Symbol: ", Nitrogen["elementSymbol"])
					print("Density: ", Nitrogen["density"], "g/l")
					print("Melting Point: ", Nitrogen["meltingPoint"])
					print("Boiling Point: ", Nitrogen["boilingPoint"])
					print("______________________________")
				if Start == "oxygen":
					print("")
					print("Oxygen:")
					print("______________________________")
					print("Atomic Number: ", Oxygen["atomicNO"])
					print("Atomic Weight: ", Oxygen["atomicWeight"])
					print("Electron Configuration: ", Oxygen["electronConfig"])
					print("Valence Electrons: ", Oxygen["valElectrons"])
					print("Type of Element: ", Oxygen["Type"])
					print("Element Symbol: ", Oxygen["elementSymbol"])
					print("Density: ", Oxygen["density"], "g/l")
					print("Melting Point: ", Oxygen["meltingPoint"])
					print("Boiling Point: ", Oxygen["boilingPoint"])
					print("______________________________")
				if Start == "fluorine":
					print("")
					print("Fluorine:")
					print("______________________________")
					print("Atomic Number: ", Fluorine["atomicNO"])
					print("Atomic Weight: ", Fluorine["atomicWeight"])
					print("Electron Configuration: ", Fluorine["electronConfig"])
					print("Valence Electrons: ", Fluorine["valElectrons"])
					print("Type of Element: ", Fluorine["Type"])
					print("Element Symbol: ", Fluorine["elementSymbol"])
					print("Density: ", Fluorine["density"], "g/l")
					print("Melting Point: ", Fluorine["meltingPoint"])
					print("Boiling Point: ", Fluorine["boilingPoint"])
					print("______________________________")
				if Start == "neon":
					print("")
					print("Neon:")
					print("______________________________")
					print("Atomic Number: ", Neon["atomicNO"])
					print("Atomic Weight: ", Neon["atomicWeight"])
					print("Electron Configuration: ", Neon["electronConfig"])
					print("Valence Electrons: ", Neon["valElectrons"])
					print("Type of Element: ", Neon["Type"])
					print("Element Symbol: ", Neon["elementSymbol"])
					print("Density: ", Neon["density"], "g/l")
					print("Melting Point: ", Neon["meltingPoint"])
					print("Boiling Point: ", Neon["boilingPoint"])
					print("______________________________")
				if Start == "sodium":
					print("")
					print("Sodium:")
					print("______________________________")
					print("Atomic Number: ", Sodium["atomicNO"])
					print("Atomic Weight: ", Sodium["atomicWeight"])
					print("Electron Configuration: ", Sodium["electronConfig"])
					print("Valence Electrons: ", Sodium["valElectrons"])
					print("Type of Element: ", Sodium["Type"])
					print("Element Symbol: ", Sodium["elementSymbol"])
					print("Density: ", Sodium["density"], "g/l")
					print("Melting Point: ", Sodium["meltingPoint"])
					print("Boiling Point: ", Sodium["boilingPoint"])
					print("______________________________")
				if Start == "magnesium":
					print("")
					print("Magnesium:")
					print("______________________________")
					print("Atomic Number: ", Magnesium["atomicNO"])
					print("Atomic Weight: ", Magnesium["atomicWeight"])
					print("Electron Configuration: ", Magnesium["electronConfig"])
					print("Valence Electrons: ", Magnesium["valElectrons"])
					print("Type of Element: ", Magnesium["Type"])
					print("Element Symbol: ", Magnesium["elementSymbol"])
					print("Density: ", Magnesium["density"], "g/l")
					print("Melting Point: ", Magnesium["meltingPoint"])
					print("Boiling Point: ", Magnesium["boilingPoint"])
					print("______________________________")
				if Start == "aluminum":
					print("")
					print("Aluminum:")
					print("______________________________")
					print("Atomic Number: ", Aluminum["atomicNO"])
					print("Atomic Weight: ", Aluminum["atomicWeight"])
					print("Electron Configuration: ", Aluminum["electronConfig"])
					print("Valence Electrons: ", Aluminum["valElectrons"])
					print("Type of Element: ", Aluminum["Type"])
					print("Element Symbol: ", Aluminum["elementSymbol"])
					print("Density: ", Aluminum["density"], "g/l")
					print("Melting Point: ", Aluminum["meltingPoint"])
					print("Boiling Point: ", Aluminum["boilingPoint"])
					print("______________________________")
				if Start == "silicon":
					print("")
					print("Silicon:")
					print("______________________________")
					print("Atomic Number: ", Silicon["atomicNO"])
					print("Atomic Weight: ", Silicon["atomicWeight"])
					print("Electron Configuration: ", Silicon["electronConfig"])
					print("Valence Electrons: ", Silicon["valElectrons"])
					print("Type of Element: ", Silicon["Type"])
					print("Element Symbol: ", Silicon["elementSymbol"])
					print("Density: ", Silicon["density"], "g/l")
					print("Melting Point: ", Silicon["meltingPoint"])
					print("Boiling Point: ", Silicon["boilingPoint"])
					print("______________________________")
				if Start == "phosphorus":
					print("")
					print("Phosphorus:")
					print("______________________________")
					print("Atomic Number: ", Phosphorus["atomicNO"])
					print("Atomic Weight: ", Phosphorus["atomicWeight"])
					print("Electron Configuration: ", Phosphorus["electronConfig"])
					print("Valence Electrons: ", Phosphorus["valElectrons"])
					print("Type of Element: ", Phosphorus["Type"])
					print("Element Symbol: ", Phosphorus["elementSymbol"])
					print("Density: ", Phosphorus["density"], "g/l")
					print("Melting Point: ", Phosphorus["meltingPoint"])
					print("Boiling Point: ", Phosphorus["boilingPoint"])
					print("______________________________")
				if Start == "sulfur":
					print("")
					print("Sulfur:")
					print("______________________________")
					print("Atomic Number: ", Sulfur["atomicNO"])
					print("Atomic Weight: ", Sulfur["atomicWeight"])
					print("Electron Configuration: ", Sulfur["electronConfig"])
					print("Valence Electrons: ", Sulfur["valElectrons"])
					print("Type of Element: ", Sulfur["Type"])
					print("Element Symbol: ", Sulfur["elementSymbol"])
					print("Density: ", Sulfur["density"], "g/l")
					print("Melting Point: ", Sulfur["meltingPoint"])
					print("Boiling Point: ", Sulfur["boilingPoint"])
					print("______________________________")
				if Start == "chlorine":
					print("")
					print("Chlorine:")
					print("______________________________")
					print("Atomic Number: ", Chlorine["atomicNO"])
					print("Atomic Weight: ", Chlorine["atomicWeight"])
					print("Electron Configuration: ", Chlorine["electronConfig"])
					print("Valence Electrons: ", Chlorine["valElectrons"])
					print("Type of Element: ", Chlorine["Type"])
					print("Element Symbol: ", Chlorine["elementSymbol"])
					print("Density: ", Chlorine["density"], "g/l")
					print("Melting Point: ", Chlorine["meltingPoint"])
					print("Boiling Point: ", Chlorine["boilingPoint"])
					print("______________________________")
				if Start == "argon":
					print("")
					print("Argon:")
					print("______________________________")
					print("Atomic Number: ", Argon["atomicNO"])
					print("Atomic Weight: ", Argon["atomicWeight"])
					print("Electron Configuration: ", Argon["electronConfig"])
					print("Valence Electrons: ", Argon["valElectrons"])
					print("Type of Element: ", Argon["Type"])
					print("Element Symbol: ", Argon["elementSymbol"])
					print("Density: ", Argon["density"], "g/l")
					print("Melting Point: ", Argon["meltingPoint"])
					print("Boiling Point: ", Argon["boilingPoint"])
					print("______________________________")
				if Start == "potassium":
					print("")
					print("Potassium:")
					print("______________________________")
					print("Atomic Number: ", Potassium["atomicNO"])
					print("Atomic Weight: ", Potassium["atomicWeight"])
					print("Electron Configuration: ", Potassium["electronConfig"])
					print("Valence Electrons: ", Potassium["valElectrons"])
					print("Type of Element: ", Potassium["Type"])
					print("Element Symbol: ", Potassium["elementSymbol"])
					print("Density: ", Potassium["density"], "g/l")
					print("Melting Point: ", Potassium["meltingPoint"])
					print("Boiling Point: ", Potassium["boilingPoint"])
					print("______________________________")
				if Start == "calcium":
					print("")
					print("Calcium:")
					print("______________________________")
					print("Atomic Number: ", Calcium["atomicNO"])
					print("Atomic Weight: ", Calcium["atomicWeight"])
					print("Electron Configuration: ", Calcium["electronConfig"])
					print("Valence Electrons: ", Calcium["valElectrons"])
					print("Type of Element: ", Calcium["Type"])
					print("Element Symbol: ", Calcium["elementSymbol"])
					print("Density: ", Calcium["density"], "g/l")
					print("Melting Point: ", Calcium["meltingPoint"])
					print("Boiling Point: ", Calcium["boilingPoint"])
					print("______________________________")
				if Start == "scandium":
					print("")
					print("Scandium:")
					print("______________________________")
					print("Atomic Number: ", Scandium["atomicNO"])
					print("Atomic Weight: ", Scandium["atomicWeight"])
					print("Electron Configuration: ", Scandium["electronConfig"])
					print("Valence Electrons: ", Scandium["valElectrons"])
					print("Type of Element: ", Scandium["Type"])
					print("Element Symbol: ", Scandium["elementSymbol"])
					print("Density: ", Scandium["density"], "g/l")
					print("Melting Point: ", Scandium["meltingPoint"])
					print("Boiling Point: ", Scandium["boilingPoint"])
					print("______________________________")
				if Start == "titanium":
					print("")
					print("Titanium:")
					print("______________________________")
					print("Atomic Number: ", Titanium["atomicNO"])
					print("Atomic Weight: ", Titanium["atomicWeight"])
					print("Electron Configuration: ", Titanium["electronConfig"])
					print("Valence Electrons: ", Titanium["valElectrons"])
					print("Type of Element: ", Titanium["Type"])
					print("Element Symbol: ", Titanium["elementSymbol"])
					print("Density: ", Titanium["density"], "g/l")
					print("Melting Point: ", Titanium["meltingPoint"])
					print("Boiling Point: ", Titanium["boilingPoint"])
					print("______________________________")
				if Start == "vanadium":
					print("")
					print("Vanadium:")
					print("______________________________")
					print("Atomic Number: ", Vanadium["atomicNO"])
					print("Atomic Weight: ", Vanadium["atomicWeight"])
					print("Electron Configuration: ", Vanadium["electronConfig"])
					print("Valence Electrons: ", Vanadium["valElectrons"])
					print("Type of Element: ", Vanadium["Type"])
					print("Element Symbol: ", Vanadium["elementSymbol"])
					print("Density: ", Vanadium["density"], "g/l")
					print("Melting Point: ", Vanadium["meltingPoint"])
					print("Boiling Point: ", Vanadium["boilingPoint"])
					print("______________________________")
				if Start == "chromium":
					print("")
					print("Chromium:")
					print("______________________________")
					print("Atomic Number: ", Chromium["atomicNO"])
					print("Atomic Weight: ", Chromium["atomicWeight"])
					print("Electron Configuration: ", Chromium["electronConfig"])
					print("Valence Electrons: ", Chromium["valElectrons"])
					print("Type of Element: ", Chromium["Type"])
					print("Element Symbol: ", Chromium["elementSymbol"])
					print("Density: ", Chromium["density"], "g/l")
					print("Melting Point: ", Chromium["meltingPoint"])
					print("Boiling Point: ", Chromium["boilingPoint"])
					print("______________________________")
				if Start == "manganese":
					print("")
					print("Manganese:")
					print("______________________________")
					print("Atomic Number: ", Manganese["atomicNO"])
					print("Atomic Weight: ", Manganese["atomicWeight"])
					print("Electron Configuration: ", Manganese["electronConfig"])
					print("Valence Electrons: ", Manganese["valElectrons"])
					print("Type of Element: ", Manganese["Type"])
					print("Element Symbol: ", Manganese["elementSymbol"])
					print("Density: ", Manganese["density"], "g/l")
					print("Melting Point: ", Manganese["meltingPoint"])
					print("Boiling Point: ", Manganese["boilingPoint"])
					print("______________________________")
				if Start == "iron":
					print("")
					print("Iron:")
					print("______________________________")
					print("Atomic Number: ", Iron["atomicNO"])
					print("Atomic Weight: ", Iron["atomicWeight"])
					print("Electron Configuration: ", Iron["electronConfig"])
					print("Valence Electrons: ", Iron["valElectrons"])
					print("Type of Element: ", Iron["Type"])
					print("Element Symbol: ", Iron["elementSymbol"])
					print("Density: ", Iron["density"], "g/l")
					print("Melting Point: ", Iron["meltingPoint"])
					print("Boiling Point: ", Iron["boilingPoint"])
					print("______________________________")
				if Start == "cobalt":
					print("")
					print("Cobalt:")
					print("______________________________")
					print("Atomic Number: ", Cobalt["atomicNO"])
					print("Atomic Weight: ", Cobalt["atomicWeight"])
					print("Electron Configuration: ", Cobalt["electronConfig"])
					print("Valence Electrons: ", Cobalt["valElectrons"])
					print("Type of Element: ", Cobalt["Type"])
					print("Element Symbol: ", Cobalt["elementSymbol"])
					print("Density: ", Cobalt["density"], "g/l")
					print("Melting Point: ", Cobalt["meltingPoint"])
					print("Boiling Point: ", Cobalt["boilingPoint"])
					print("______________________________")
				if Start == "nickel":
					print("")
					print("Nickel:")
					print("______________________________")
					print("Atomic Number: ", Nickel["atomicNO"])
					print("Atomic Weight: ", Nickel["atomicWeight"])
					print("Electron Configuration: ", Nickel["electronConfig"])
					print("Valence Electrons: ", Nickel["valElectrons"])
					print("Type of Element: ", Nickel["Type"])
					print("Element Symbol: ", Nickel["elementSymbol"])
					print("Density: ", Nickel["density"], "g/l")
					print("Melting Point: ", Nickel["meltingPoint"])
					print("Boiling Point: ", Nickel["boilingPoint"])
					print("______________________________")
				if Start == "copper":
					print("")
					print("Copper:")
					print("______________________________")
					print("Atomic Number: ", Copper["atomicNO"])
					print("Atomic Weight: ", Copper["atomicWeight"])
					print("Electron Configuration: ", Copper["electronConfig"])
					print("Valence Electrons: ", Copper["valElectrons"])
					print("Type of Element: ", Copper["Type"])
					print("Element Symbol: ", Copper["elementSymbol"])
					print("Density: ", Copper["density"], "g/l")
					print("Melting Point: ", Copper["meltingPoint"])
					print("Boiling Point: ", Copper["boilingPoint"])
					print("______________________________")
				if Start == "zinc":
					print("")
					print("Zinc:")
					print("______________________________")
					print("Atomic Number: ", Zinc["atomicNO"])
					print("Atomic Weight: ", Zinc["atomicWeight"])
					print("Electron Configuration: ", Zinc["electronConfig"])
					print("Valence Electrons: ", Zinc["valElectrons"])
					print("Type of Element: ", Zinc["Type"])
					print("Element Symbol: ", Zinc["elementSymbol"])
					print("Density: ", Zinc["density"], "g/l")
					print("Melting Point: ", Zinc["meltingPoint"])
					print("Boiling Point: ", Zinc["boilingPoint"])
					print("______________________________")
				if Start == "gallium":
					print("")
					print("Gallium:")
					print("______________________________")
					print("Atomic Number: ", Gallium["atomicNO"])
					print("Atomic Weight: ", Gallium["atomicWeight"])
					print("Electron Configuration: ", Gallium["electronConfig"])
					print("Valence Electrons: ", Gallium["valElectrons"])
					print("Type of Element: ", Gallium["Type"])
					print("Element Symbol: ", Gallium["elementSymbol"])
					print("Density: ", Gallium["density"], "g/l")
					print("Melting Point: ", Gallium["meltingPoint"])
					print("Boiling Point: ", Gallium["boilingPoint"])
					print("______________________________")
				if Start == "germanium":
					print("")
					print("Germanium:")
					print("______________________________")
					print("Atomic Number: ", Germanium["atomicNO"])
					print("Atomic Weight: ", Germanium["atomicWeight"])
					print("Electron Configuration: ", Germanium["electronConfig"])
					print("Valence Electrons: ", Germanium["valElectrons"])
					print("Type of Element: ", Germanium["Type"])
					print("Element Symbol: ", Germanium["elementSymbol"])
					print("Density: ", Germanium["density"], "g/l")
					print("Melting Point: ", Germanium["meltingPoint"])
					print("Boiling Point: ", Germanium["boilingPoint"])
					print("______________________________")
				if Start == "arsenic":
					print("")
					print("Arsenic:")
					print("______________________________")
					print("Atomic Number: ", Arsenic["atomicNO"])
					print("Atomic Weight: ", Arsenic["atomicWeight"])
					print("Electron Configuration: ", Arsenic["electronConfig"])
					print("Valence Electrons: ", Arsenic["valElectrons"])
					print("Type of Element: ", Arsenic["Type"])
					print("Element Symbol: ", Arsenic["elementSymbol"])
					print("Density: ", Arsenic["density"], "g/l")
					print("Melting Point: ", Arsenic["meltingPoint"])
					print("Boiling Point: ", Arsenic["boilingPoint"])
					print("______________________________")
				if Start == "selenium":
					print("")
					print("Selenium:")
					print("______________________________")
					print("Atomic Number: ", Selenium["atomicNO"])
					print("Atomic Weight: ", Selenium["atomicWeight"])
					print("Electron Configuration: ", Selenium["electronConfig"])
					print("Valence Electrons: ", Selenium["valElectrons"])
					print("Type of Element: ", Selenium["Type"])
					print("Element Symbol: ", Selenium["elementSymbol"])
					print("Density: ", Selenium["density"], "g/l")
					print("Melting Point: ", Selenium["meltingPoint"])
					print("Boiling Point: ", Selenium["boilingPoint"])
					print("______________________________")
				if Start == "bromine":
					print("")
					print("Bromine:")
					print("______________________________")
					print("Atomic Number: ", Bromine["atomicNO"])
					print("Atomic Weight: ", Bromine["atomicWeight"])
					print("Electron Configuration: ", Bromine["electronConfig"])
					print("Valence Electrons: ", Bromine["valElectrons"])
					print("Type of Element: ", Bromine["Type"])
					print("Element Symbol: ", Bromine["elementSymbol"])
					print("Density: ", Bromine["density"], "g/l")
					print("Melting Point: ", Bromine["meltingPoint"])
					print("Boiling Point: ", Bromine["boilingPoint"])
					print("______________________________")
				if Start == "krypton":
					print("")
					print("Krypton:")
					print("______________________________")
					print("Atomic Number: ", Krypton["atomicNO"])
					print("Atomic Weight: ", Krypton["atomicWeight"])
					print("Electron Configuration: ", Krypton["electronConfig"])
					print("Valence Electrons: ", Krypton["valElectrons"])
					print("Type of Element: ", Krypton["Type"])
					print("Element Symbol: ", Krypton["elementSymbol"])
					print("Density: ", Krypton["density"], "g/l")
					print("Melting Point: ", Krypton["meltingPoint"])
					print("Boiling Point: ", Krypton["boilingPoint"])
					print("______________________________")
				if Start == "rubidium":
					print("")
					print("Rubidium:")
					print("______________________________")
					print("Atomic Number: ", Rubidium["atomicNO"])
					print("Atomic Weight: ", Rubidium["atomicWeight"])
					print("Electron Configuration: ", Rubidium["electronConfig"])
					print("Valence Electrons: ", Rubidium["valElectrons"])
					print("Type of Element: ", Rubidium["Type"])
					print("Element Symbol: ", Rubidium["elementSymbol"])
					print("Density: ", Rubidium["density"], "g/l")
					print("Melting Point: ", Rubidium["meltingPoint"])
					print("Boiling Point: ", Rubidium["boilingPoint"])
					print("______________________________")
				if Start == "strontium":
					print("")
					print("Strontium:")
					print("______________________________")
					print("Atomic Number: ", Strontium["atomicNO"])
					print("Atomic Weight: ", Strontium["atomicWeight"])
					print("Electron Configuration: ", Strontium["electronConfig"])
					print("Valence Electrons: ", Strontium["valElectrons"])
					print("Type of Element: ", Strontium["Type"])
					print("Element Symbol: ", Strontium["elementSymbol"])
					print("Density: ", Strontium["density"], "g/l")
					print("Melting Point: ", Strontium["meltingPoint"])
					print("Boiling Point: ", Strontium["boilingPoint"])
					print("______________________________")
				if Start == "yttrium":
					print("")
					print("Yttrium:")
					print("______________________________")
					print("Atomic Number: ", Yttrium["atomicNO"])
					print("Atomic Weight: ", Yttrium["atomicWeight"])
					print("Electron Configuration: ", Yttrium["electronConfig"])
					print("Valence Electrons: ", Yttrium["valElectrons"])
					print("Type of Element: ", Yttrium["Type"])
					print("Element Symbol: ", Yttrium["elementSymbol"])
					print("Density: ", Yttrium["density"], "g/l")
					print("Melting Point: ", Yttrium["meltingPoint"])
					print("Boiling Point: ", Yttrium["boilingPoint"])
					print("______________________________")
				if Start == "zirconium":
					print("")
					print("Zirconium:")
					print("______________________________")
					print("Atomic Number: ", Zirconium["atomicNO"])
					print("Atomic Weight: ", Zirconium["atomicWeight"])
					print("Electron Configuration: ", Zirconium["electronConfig"])
					print("Valence Electrons: ", Zirconium["valElectrons"])
					print("Type of Element: ", Zirconium["Type"])
					print("Element Symbol: ", Zirconium["elementSymbol"])
					print("Density: ", Zirconium["density"], "g/l")
					print("Melting Point: ", Zirconium["meltingPoint"])
					print("Boiling Point: ", Zirconium["boilingPoint"])
					print("______________________________")
				if Start == "niobium":
					print("")
					print("Niobium:")
					print("______________________________")
					print("Atomic Number: ", Niobium["atomicNO"])
					print("Atomic Weight: ", Niobium["atomicWeight"])
					print("Electron Configuration: ", Niobium["electronConfig"])
					print("Valence Electrons: ", Niobium["valElectrons"])
					print("Type of Element: ", Niobium["Type"])
					print("Element Symbol: ", Niobium["elementSymbol"])
					print("Density: ", Niobium["density"], "g/l")
					print("Melting Point: ", Niobium["meltingPoint"])
					print("Boiling Point: ", Niobium["boilingPoint"])
					print("______________________________")
				if Start == "molybdenur":
					print("")
					print("Molybdenur:")
					print("______________________________")
					print("Atomic Number: ", Molybdenur["atomicNO"])
					print("Atomic Weight: ", Molybdenur["atomicWeight"])
					print("Electron Configuration: ", Molybdenur["electronConfig"])
					print("Valence Electrons: ", Molybdenur["valElectrons"])
					print("Type of Element: ", Molybdenur["Type"])
					print("Element Symbol: ", Molybdenur["elementSymbol"])
					print("Density: ", Molybdenur["density"], "g/l")
					print("Melting Point: ", Molybdenur["meltingPoint"])
					print("Boiling Point: ", Molybdenur["boilingPoint"])
					print("______________________________")
				if Start == "technetium":
					print("")
					print("Technetium:")
					print("______________________________")
					print("Atomic Number: ", Technetium["atomicNO"])
					print("Atomic Weight: ", Technetium["atomicWeight"])
					print("Electron Configuration: ", Technetium["electronConfig"])
					print("Valence Electrons: ", Technetium["valElectrons"])
					print("Type of Element: ", Technetium["Type"])
					print("Element Symbol: ", Technetium["elementSymbol"])
					print("Density: ", Technetium["density"], "g/l")
					print("Melting Point: ", Technetium["meltingPoint"])
					print("Boiling Point: ", Technetium["boilingPoint"])
					print("______________________________")
				if Start == "ruthenium":
					print("")
					print("Ruthenium:")
					print("______________________________")
					print("Atomic Number: ", Ruthenium["atomicNO"])
					print("Atomic Weight: ", Ruthenium["atomicWeight"])
					print("Electron Configuration: ", Ruthenium["electronConfig"])
					print("Valence Electrons: ", Ruthenium["valElectrons"])
					print("Type of Element: ", Ruthenium["Type"])
					print("Element Symbol: ", Ruthenium["elementSymbol"])
					print("Density: ", Ruthenium["density"], "g/l")
					print("Melting Point: ", Ruthenium["meltingPoint"])
					print("Boiling Point: ", Ruthenium["boilingPoint"])
					print("______________________________")
				if Start == "rhodium":
					print("")
					print("Rhodium:")
					print("______________________________")
					print("Atomic Number: ", Rhodium["atomicNO"])
					print("Atomic Weight: ", Rhodium["atomicWeight"])
					print("Electron Configuration: ", Rhodium["electronConfig"])
					print("Valence Electrons: ", Rhodium["valElectrons"])
					print("Type of Element: ", Rhodium["Type"])
					print("Element Symbol: ", Rhodium["elementSymbol"])
					print("Density: ", Rhodium["density"], "g/l")
					print("Melting Point: ", Rhodium["meltingPoint"])
					print("Boiling Point: ", Rhodium["boilingPoint"])
					print("______________________________")
				if Start == "palladium":
					print("")
					print("Palladium:")
					print("______________________________")
					print("Atomic Number: ", Palladium["atomicNO"])
					print("Atomic Weight: ", Palladium["atomicWeight"])
					print("Electron Configuration: ", Palladium["electronConfig"])
					print("Valence Electrons: ", Palladium["valElectrons"])
					print("Type of Element: ", Palladium["Type"])
					print("Element Symbol: ", Palladium["elementSymbol"])
					print("Density: ", Palladium["density"], "g/l")
					print("Melting Point: ", Palladium["meltingPoint"])
					print("Boiling Point: ", Palladium["boilingPoint"])
					print("______________________________")
				if Start == "silver":
					print("")
					print("Silver:")
					print("______________________________")
					print("Atomic Number: ", Silver["atomicNO"])
					print("Atomic Weight: ", Silver["atomicWeight"])
					print("Electron Configuration: ", Silver["electronConfig"])
					print("Valence Electrons: ", Silver["valElectrons"])
					print("Type of Element: ", Silver["Type"])
					print("Element Symbol: ", Silver["elementSymbol"])
					print("Density: ", Silver["density"], "g/l")
					print("Melting Point: ", Silver["meltingPoint"])
					print("Boiling Point: ", Silver["boilingPoint"])
					print("______________________________")
				if Start == "cadmium":
					print("")
					print("Cadmium:")
					print("______________________________")
					print("Atomic Number: ", Cadmium["atomicNO"])
					print("Atomic Weight: ", Cadmium["atomicWeight"])
					print("Electron Configuration: ", Cadmium["electronConfig"])
					print("Valence Electrons: ", Cadmium["valElectrons"])
					print("Type of Element: ", Cadmium["Type"])
					print("Element Symbol: ", Cadmium["elementSymbol"])
					print("Density: ", Cadmium["density"], "g/l")
					print("Melting Point: ", Cadmium["meltingPoint"])
					print("Boiling Point: ", Cadmium["boilingPoint"])
					print("______________________________")
				if Start == "indium":
					print("")
					print("Indium:")
					print("______________________________")
					print("Atomic Number: ", Indium["atomicNO"])
					print("Atomic Weight: ", Indium["atomicWeight"])
					print("Electron Configuration: ", Indium["electronConfig"])
					print("Valence Electrons: ", Indium["valElectrons"])
					print("Type of Element: ", Indium["Type"])
					print("Element Symbol: ", Indium["elementSymbol"])
					print("Density: ", Indium["density"], "g/l")
					print("Melting Point: ", Indium["meltingPoint"])
					print("Boiling Point: ", Indium["boilingPoint"])
					print("______________________________")
				if Start == "tin":
					print("")
					print("Tin:")
					print("______________________________")
					print("Atomic Number: ", Tin["atomicNO"])
					print("Atomic Weight: ", Tin["atomicWeight"])
					print("Electron Configuration: ", Tin["electronConfig"])
					print("Valence Electrons: ", Tin["valElectrons"])
					print("Type of Element: ", Tin["Type"])
					print("Element Symbol: ", Tin["elementSymbol"])
					print("Density: ", Tin["density"], "g/cm3")
					print("Melting Point: ", Tin["meltingPoint"])
					print("Boiling Point: ", Tin["boilingPoint"])
					print("______________________________")
				if Start == "antimony":
					print("")
					print("Antimony:")
					print("______________________________")
					print("Atomic Number: ", Antimony["atomicNO"])
					print("Atomic Weight: ", Antimony["atomicWeight"])
					print("Electron Configuration: ", Antimony["electronConfig"])
					print("Valence Electrons: ", Antimony["valElectrons"])
					print("Type of Element: ", Antimony["Type"])
					print("Element Symbol: ", Antimony["elementSymbol"])
					print("Density: ", Antimony["density"], "g/cm3")
					print("Melting Point: ", Antimony["meltingPoint"])
					print("Boiling Point: ", Antimony["boilingPoint"])
					print("______________________________")
				if Start == "tellurium":
					print("")
					print("Tellurium:")
					print("______________________________")
					print("Atomic Number: ", Tellurium["atomicNO"])
					print("Atomic Weight: ", Tellurium["atomicWeight"])
					print("Electron Configuration: ", Tellurium["electronConfig"])
					print("Valence Electrons: ", Tellurium["valElectrons"])
					print("Type of Element: ", Tellurium["Type"])
					print("Element Symbol: ", Tellurium["elementSymbol"])
					print("Density: ", Tellurium["density"], "g/cm3")
					print("Melting Point: ", Tellurium["meltingPoint"])
					print("Boiling Point: ", Tellurium["boilingPoint"])
					print("______________________________")
				if Start == "iodine":
					print("")
					print("Iodine:")
					print("______________________________")
					print("Atomic Number: ", Iodine["atomicNO"])
					print("Atomic Weight: ", Iodine["atomicWeight"])
					print("Electron Configuration: ", Iodine["electronConfig"])
					print("Valence Electrons: ", Iodine["valElectrons"])
					print("Type of Element: ", Iodine["Type"])
					print("Element Symbol: ", Iodine["elementSymbol"])
					print("Density: ", Iodine["density"], "g/cm3")
					print("Melting Point: ", Iodine["meltingPoint"])
					print("Boiling Point: ", Iodine["boilingPoint"])
					print("______________________________")
				if Start == "xenon":
					print("")
					print("Xenon:")
					print("______________________________")
					print("Atomic Number: ", Xenon["atomicNO"])
					print("Atomic Weight: ", Xenon["atomicWeight"])
					print("Electron Configuration: ", Xenon["electronConfig"])
					print("Valence Electrons: ", Xenon["valElectrons"])
					print("Type of Element: ", Xenon["Type"])
					print("Element Symbol: ", Xenon["elementSymbol"])
					print("Density: ", Xenon["density"], "g/cm3")
					print("Melting Point: ", Xenon["meltingPoint"])
					print("Boiling Point: ", Xenon["boilingPoint"])
					print("______________________________")
				if Start == "caesium":
					print("")
					print("Caesium:")
					print("______________________________")
					print("Atomic Number: ", Caesium["atomicNO"])
					print("Atomic Weight: ", Caesium["atomicWeight"])
					print("Electron Configuration: ", Caesium["electronConfig"])
					print("Valence Electrons: ", Caesium["valElectrons"])
					print("Type of Element: ", Caesium["Type"])
					print("Element Symbol: ", Caesium["elementSymbol"])
					print("Density: ", Caesium["density"], "g/cm3")
					print("Melting Point: ", Caesium["meltingPoint"])
					print("Boiling Point: ", Caesium["boilingPoint"])
					print("______________________________")
				if Start == "barium":
					print("")
					print("Barium:")
					print("______________________________")
					print("Atomic Number: ", Barium["atomicNO"])
					print("Atomic Weight: ", Barium["atomicWeight"])
					print("Electron Configuration: ", Barium["electronConfig"])
					print("Valence Electrons: ", Barium["valElectrons"])
					print("Type of Element: ", Barium["Type"])
					print("Element Symbol: ", Barium["elementSymbol"])
					print("Density: ", Barium["density"], "g/cm3")
					print("Melting Point: ", Barium["meltingPoint"])
					print("Boiling Point: ", Barium["boilingPoint"])
					print("______________________________")
				if Start == "lanthanum":
					print("")
					print("Lanthanum:")
					print("______________________________")
					print("Atomic Number: ", Lanthanum["atomicNO"])
					print("Atomic Weight: ", Lanthanum["atomicWeight"])
					print("Electron Configuration: ", Lanthanum["electronConfig"])
					print("Valence Electrons: ", Lanthanum["valElectrons"])
					print("Type of Element: ", Lanthanum["Type"])
					print("Element Symbol: ", Lanthanum["elementSymbol"])
					print("Density: ", Lanthanum["density"], "g/cm3")
					print("Melting Point: ", Lanthanum["meltingPoint"])
					print("Boiling Point: ", Lanthanum["boilingPoint"])
					print("______________________________")
				if Start == "cerium":
					print("")
					print("Cerium:")
					print("______________________________")
					print("Atomic Number: ", Cerium["atomicNO"])
					print("Atomic Weight: ", Cerium["atomicWeight"])
					print("Electron Configuration: ", Cerium["electronConfig"])
					print("Valence Electrons: ", Cerium["valElectrons"])
					print("Type of Element: ", Cerium["Type"])
					print("Element Symbol: ", Cerium["elementSymbol"])
					print("Density: ", Cerium["density"], "g/cm3")
					print("Melting Point: ", Cerium["meltingPoint"])
					print("Boiling Point: ", Cerium["boilingPoint"])
					print("______________________________")
				if Start == "praseodymium":
					print("")
					print("Praseodymium:")
					print("______________________________")
					print("Atomic Number: ", Praseodymium["atomicNO"])
					print("Atomic Weight: ", Praseodymium["atomicWeight"])
					print("Electron Configuration: ", Praseodymium["electronConfig"])
					print("Valence Electrons: ", Praseodymium["valElectrons"])
					print("Type of Element: ", Praseodymium["Type"])
					print("Element Symbol: ", Praseodymium["elementSymbol"])
					print("Density: ", Praseodymium["density"], "g/cm3")
					print("Melting Point: ", Praseodymium["meltingPoint"])
					print("Boiling Point: ", Praseodymium["boilingPoint"])
					print("______________________________")
				if Start == "neodymium":
					print("")
					print("Neodymium:")
					print("______________________________")
					print("Atomic Number: ", Neodymium["atomicNO"])
					print("Atomic Weight: ", Neodymium["atomicWeight"])
					print("Electron Configuration: ", Neodymium["electronConfig"])
					print("Valence Electrons: ", Neodymium["valElectrons"])
					print("Type of Element: ", Neodymium["Type"])
					print("Element Symbol: ", Neodymium["elementSymbol"])
					print("Density: ", Neodymium["density"], "g/cm3")
					print("Melting Point: ", Neodymium["meltingPoint"])
					print("Boiling Point: ", Neodymium["boilingPoint"])
					print("______________________________")
				if Start == "promethium":
					print("")
					print("Promethium:")
					print("______________________________")
					print("Atomic Number: ", Promethium["atomicNO"])
					print("Atomic Weight: ", Promethium["atomicWeight"])
					print("Electron Configuration: ", Promethium["electronConfig"])
					print("Valence Electrons: ", Promethium["valElectrons"])
					print("Type of Element: ", Promethium["Type"])
					print("Element Symbol: ", Promethium["elementSymbol"])
					print("Density: ", Promethium["density"], "g/cm3")
					print("Melting Point: ", Promethium["meltingPoint"])
					print("Boiling Point: ", Promethium["boilingPoint"])
					print("______________________________")
				if Start == "samarium":
					print("")
					print("Samarium:")
					print("______________________________")
					print("Atomic Number: ", Samarium["atomicNO"])
					print("Atomic Weight: ", Samarium["atomicWeight"])
					print("Electron Configuration: ", Samarium["electronConfig"])
					print("Valence Electrons: ", Samarium["valElectrons"])
					print("Type of Element: ", Samarium["Type"])
					print("Element Symbol: ", Samarium["elementSymbol"])
					print("Density: ", Samarium["density"], "g/cm3")
					print("Melting Point: ", Samarium["meltingPoint"])
					print("Boiling Point: ", Samarium["boilingPoint"])
					print("______________________________")
				if Start == "europium":
					print("")
					print("Europium:")
					print("______________________________")
					print("Atomic Number: ", Europium["atomicNO"])
					print("Atomic Weight: ", Europium["atomicWeight"])
					print("Electron Configuration: ", Europium["electronConfig"])
					print("Valence Electrons: ", Europium["valElectrons"])
					print("Type of Element: ", Europium["Type"])
					print("Element Symbol: ", Europium["elementSymbol"])
					print("Density: ", Europium["density"], "g/cm3")
					print("Melting Point: ", Europium["meltingPoint"])
					print("Boiling Point: ", Europium["boilingPoint"])
					print("______________________________")
				if Start == "gadolinium":
					print("")
					print("Gadolinium:")
					print("______________________________")
					print("Atomic Number: ", Gadolinium["atomicNO"])
					print("Atomic Weight: ", Gadolinium["atomicWeight"])
					print("Electron Configuration: ", Gadolinium["electronConfig"])
					print("Valence Electrons: ", Gadolinium["valElectrons"])
					print("Type of Element: ", Gadolinium["Type"])
					print("Element Symbol: ", Gadolinium["elementSymbol"])
					print("Density: ", Gadolinium["density"], "g/cm3")
					print("Melting Point: ", Gadolinium["meltingPoint"])
					print("Boiling Point: ", Gadolinium["boilingPoint"])
					print("______________________________")
				if Start == "terbium":
					print("")
					print("Terbium:")
					print("______________________________")
					print("Atomic Number: ", Terbium["atomicNO"])
					print("Atomic Weight: ", Terbium["atomicWeight"])
					print("Electron Configuration: ", Terbium["electronConfig"])
					print("Valence Electrons: ", Terbium["valElectrons"])
					print("Type of Element: ", Terbium["Type"])
					print("Element Symbol: ", Terbium["elementSymbol"])
					print("Density: ", Terbium["density"], "g/cm3")
					print("Melting Point: ", Terbium["meltingPoint"])
					print("Boiling Point: ", Terbium["boilingPoint"])
					print("______________________________")
				if Start == "dysprosium":
					print("")
					print("Dysprosium:")
					print("______________________________")
					print("Atomic Number: ", Dysprosium["atomicNO"])
					print("Atomic Weight: ", Dysprosium["atomicWeight"])
					print("Electron Configuration: ", Dysprosium["electronConfig"])
					print("Valence Electrons: ", Dysprosium["valElectrons"])
					print("Type of Element: ", Dysprosium["Type"])
					print("Element Symbol: ", Dysprosium["elementSymbol"])
					print("Density: ", Dysprosium["density"], "g/cm3")
					print("Melting Point: ", Dysprosium["meltingPoint"])
					print("Boiling Point: ", Dysprosium["boilingPoint"])
					print("______________________________")
				if Start == "holmium":
					print("")
					print("Holmium:")
					print("______________________________")
					print("Atomic Number: ", Holmium["atomicNO"])
					print("Atomic Weight: ", Holmium["atomicWeight"])
					print("Electron Configuration: ", Holmium["electronConfig"])
					print("Valence Electrons: ", Holmium["valElectrons"])
					print("Type of Element: ", Holmium["Type"])
					print("Element Symbol: ", Holmium["elementSymbol"])
					print("Density: ", Holmium["density"], "g/cm3")
					print("Melting Point: ", Holmium["meltingPoint"])
					print("Boiling Point: ", Holmium["boilingPoint"])
					print("______________________________")
				if Start == "erbium":
					print("")
					print("Erbium:")
					print("______________________________")
					print("Atomic Number: ", Erbium["atomicNO"])
					print("Atomic Weight: ", Erbium["atomicWeight"])
					print("Electron Configuration: ", Erbium["electronConfig"])
					print("Valence Electrons: ", Erbium["valElectrons"])
					print("Type of Element: ", Erbium["Type"])
					print("Element Symbol: ", Erbium["elementSymbol"])
					print("Density: ", Erbium["density"], "g/cm3")
					print("Melting Point: ", Erbium["meltingPoint"])
					print("Boiling Point: ", Erbium["boilingPoint"])
					print("______________________________")
				if Start == "thulium":
					print("")
					print("Thulium:")
					print("______________________________")
					print("Atomic Number: ", Thulium["atomicNO"])
					print("Atomic Weight: ", Thulium["atomicWeight"])
					print("Electron Configuration: ", Thulium["electronConfig"])
					print("Valence Electrons: ", Thulium["valElectrons"])
					print("Type of Element: ", Thulium["Type"])
					print("Element Symbol: ", Thulium["elementSymbol"])
					print("Density: ", Thulium["density"], "g/cm3")
					print("Melting Point: ", Thulium["meltingPoint"])
					print("Boiling Point: ", Thulium["boilingPoint"])
					print("______________________________")
				if Start == "ytterbium":
					print("")
					print("Ytterbium:")
					print("______________________________")
					print("Atomic Number: ", Ytterbium["atomicNO"])
					print("Atomic Weight: ", Ytterbium["atomicWeight"])
					print("Electron Configuration: ", Ytterbium["electronConfig"])
					print("Valence Electrons: ", Ytterbium["valElectrons"])
					print("Type of Element: ", Ytterbium["Type"])
					print("Element Symbol: ", Ytterbium["elementSymbol"])
					print("Density: ", Ytterbium["density"], "g/cm3")
					print("Melting Point: ", Ytterbium["meltingPoint"])
					print("Boiling Point: ", Ytterbium["boilingPoint"])
					print("______________________________")
				if Start == "lutetium":
					print("")
					print("Lutetium:")
					print("______________________________")
					print("Atomic Number: ", Lutetium["atomicNO"])
					print("Atomic Weight: ", Lutetium["atomicWeight"])
					print("Electron Configuration: ", Lutetium["electronConfig"])
					print("Valence Electrons: ", Lutetium["valElectrons"])
					print("Type of Element: ", Lutetium["Type"])
					print("Element Symbol: ", Lutetium["elementSymbol"])
					print("Density: ", Lutetium["density"], "g/cm3")
					print("Melting Point: ", Lutetium["meltingPoint"])
					print("Boiling Point: ", Lutetium["boilingPoint"])
					print("______________________________")
				if Start == "hafnium":
					print("")
					print("Hafnium:")
					print("______________________________")
					print("Atomic Number: ", Hafnium["atomicNO"])
					print("Atomic Weight: ", Hafnium["atomicWeight"])
					print("Electron Configuration: ", Hafnium["electronConfig"])
					print("Valence Electrons: ", Hafnium["valElectrons"])
					print("Type of Element: ", Hafnium["Type"])
					print("Element Symbol: ", Hafnium["elementSymbol"])
					print("Density: ", Hafnium["density"], "g/cm3")
					print("Melting Point: ", Hafnium["meltingPoint"])
					print("Boiling Point: ", Hafnium["boilingPoint"])
					print("______________________________")
				if Start == "tantalum":
					print("")
					print("Tantalum:")
					print("______________________________")
					print("Atomic Number: ", Tantalum["atomicNO"])
					print("Atomic Weight: ", Tantalum["atomicWeight"])
					print("Electron Configuration: ", Tantalum["electronConfig"])
					print("Valence Electrons: ", Tantalum["valElectrons"])
					print("Type of Element: ", Tantalum["Type"])
					print("Element Symbol: ", Tantalum["elementSymbol"])
					print("Density: ", Tantalum["density"], "g/cm3")
					print("Melting Point: ", Tantalum["meltingPoint"])
					print("Boiling Point: ", Tantalum["boilingPoint"])
					print("______________________________")
				if Start == "tungsten":
					print("")
					print("Tungsten:")
					print("______________________________")
					print("Atomic Number: ", Tungsten["atomicNO"])
					print("Atomic Weight: ", Tungsten["atomicWeight"])
					print("Electron Configuration: ", Tungsten["electronConfig"])
					print("Valence Electrons: ", Tungsten["valElectrons"])
					print("Type of Element: ", Tungsten["Type"])
					print("Element Symbol: ", Tungsten["elementSymbol"])
					print("Density: ", Tungsten["density"], "g/cm3")
					print("Melting Point: ", Tungsten["meltingPoint"])
					print("Boiling Point: ", Tungsten["boilingPoint"])
					print("______________________________")
				if Start == "rhenium":
					print("")
					print("Rhenium:")
					print("______________________________")
					print("Atomic Number: ", Rhenium["atomicNO"])
					print("Atomic Weight: ", Rhenium["atomicWeight"])
					print("Electron Configuration: ", Rhenium["electronConfig"])
					print("Valence Electrons: ", Rhenium["valElectrons"])
					print("Type of Element: ", Rhenium["Type"])
					print("Element Symbol: ", Rhenium["elementSymbol"])
					print("Density: ", Rhenium["density"], "g/cm3")
					print("Melting Point: ", Rhenium["meltingPoint"])
					print("Boiling Point: ", Rhenium["boilingPoint"])
					print("______________________________")
				if Start == "osmium":
					print("")
					print("Osmium:")
					print("______________________________")
					print("Atomic Number: ", Osmium["atomicNO"])
					print("Atomic Weight: ", Osmium["atomicWeight"])
					print("Electron Configuration: ", Osmium["electronConfig"])
					print("Valence Electrons: ", Osmium["valElectrons"])
					print("Type of Element: ", Osmium["Type"])
					print("Element Symbol: ", Osmium["elementSymbol"])
					print("Density: ", Osmium["density"], "g/cm3")
					print("Melting Point: ", Osmium["meltingPoint"])
					print("Boiling Point: ", Osmium["boilingPoint"])
					print("______________________________")
				if Start == "iridium":
					print
					print("Iridium:")
					print("______________________________")
					print("Atomic Number: ", Iridium["atomicNO"])
					print("Atomic Weight: ", Iridium["atomicWeight"])
					print("Electron Configuration: ", Iridium["electronConfig"])
					print("Valence Electrons: ", Iridium["valElectrons"])
					print("Type of Element: ", Iridium["Type"])
					print("Element Symbol: ", Iridium["elementSymbol"])
					print("Density: ", Iridium["density"], "g/cm3")
					print("Melting Point: ", Iridium["meltingPoint"])
					print("Boiling Point: ", Iridium["boilingPoint"])
					print("______________________________")
				if Start == "platinum":
					print("")
					print("Platinum:")
					print("______________________________")
					print("Atomic Number: ", Platinum["atomicNO"])
					print("Atomic Weight: ", Platinum["atomicWeight"])
					print("Electron Configuration: ", Platinum["electronConfig"])
					print("Valence Electrons: ", Platinum["valElectrons"])
					print("Type of Element: ", Platinum["Type"])
					print("Element Symbol: ", Platinum["elementSymbol"])
					print("Density: ", Platinum["density"], "g/cm3")
					print("Melting Point: ", Platinum["meltingPoint"])
					print("Boiling Point: ", Platinum["boilingPoint"])
					print("______________________________")
				if Start == "gold":
					print("")
					print("Gold:")
					print("______________________________")
					print("Atomic Number: ", Gold["atomicNO"])
					print("Atomic Weight: ", Gold["atomicWeight"])
					print("Electron Configuration: ", Gold["electronConfig"])
					print("Valence Electrons: ", Gold["valElectrons"])
					print("Type of Element: ", Gold["Type"])
					print("Element Symbol: ", Gold["elementSymbol"])
					print("Density: ", Gold["density"], "g/cm3")
					print("Melting Point: ", Gold["meltingPoint"])
					print("Boiling Point: ", Gold["boilingPoint"])
					print("______________________________")
				if Start == "mercury":
					print("")
					print("Mercury:")
					print("______________________________")
					print("Atomic Number: ", Mercury["atomicNO"])
					print("Atomic Weight: ", Mercury["atomicWeight"])
					print("Electron Configuration: ", Mercury["electronConfig"])
					print("Valence Electrons: ", Mercury["valElectrons"])
					print("Type of Element: ", Mercury["Type"])
					print("Element Symbol: ", Mercury["elementSymbol"])
					print("Density: ", Mercury["density"], "g/cm3")
					print("Melting Point: ", Mercury["meltingPoint"])
					print("Boiling Point: ", Mercury["boilingPoint"])
					print("______________________________")
				if Start == "thallium":
					print("")
					print("Thallium:")
					print("______________________________")
					print("Atomic Number: ", Thallium["atomicNO"])
					print("Atomic Weight: ", Thallium["atomicWeight"])
					print("Electron Configuration: ", Thallium["electronConfig"])
					print("Valence Electrons: ", Thallium["valElectrons"])
					print("Type of Element: ", Thallium["Type"])
					print("Element Symbol: ", Thallium["elementSymbol"])
					print("Density: ", Thallium["density"], "g/cm3")
					print("Melting Point: ", Thallium["meltingPoint"])
					print("Boiling Point: ", Thallium["boilingPoint"])
					print("______________________________")
				if Start == "lead":
					print("")
					print("Lead:")
					print("______________________________")
					print("Atomic Number: ", Lead["atomicNO"])
					print("Atomic Weight: ", Lead["atomicWeight"])
					print("Electron Configuration: ", Lead["electronConfig"])
					print("Valence Electrons: ", Lead["valElectrons"])
					print("Type of Element: ", Lead["Type"])
					print("Element Symbol: ", Lead["elementSymbol"])
					print("Density: ", Lead["density"], "g/cm3")
					print("Melting Point: ", Lead["meltingPoint"])
					print("Boiling Point: ", Lead["boilingPoint"])
					print("______________________________")
				if Start == "bismuth":
					print("")
					print("Bismuth:")
					print("______________________________")
					print("Atomic Number: ", Bismuth["atomicNO"])
					print("Atomic Weight: ", Bismuth["atomicWeight"])
					print("Electron Configuration: ", Bismuth["electronConfig"])
					print("Valence Electrons: ", Bismuth["valElectrons"])
					print("Type of Element: ", Bismuth["Type"])
					print("Element Symbol: ", Bismuth["elementSymbol"])
					print("Density: ", Bismuth["density"], "g/cm3")
					print("Melting Point: ", Bismuth["meltingPoint"])
					print("Boiling Point: ", Bismuth["boilingPoint"])
					print("______________________________")
				if Start == "polonium":
					print("")
					print("Polonium:")
					print("______________________________")		
					print("Atomic Number: ", Polonium["atomicNO"])
					print("Atomic Weight: ", Polonium["atomicWeight"])
					print("Electron Configuration: ", Polonium["electronConfig"])
					print("Valence Electrons: ", Polonium["valElectrons"])
					print("Type of Element: ", Polonium["Type"])
					print("Element Symbol: ", Polonium["elementSymbol"])
					print("Density: ", Polonium["density"], "g/cm3")
					print("Melting Point: ", Polonium["meltingPoint"])
					print("Boiling Point: ", Polonium["boilingPoint"])
					print("______________________________")
				if Start == "astatine":
					print("")
					print("Astatine:")
					print("______________________________")
					print("Atomic Number: ", Astatine["atomicNO"])
					print("Atomic Weight: ", Astatine["atomicWeight"])
					print("Electron Configuration: ", Astatine["electronConfig"])
					print("Valence Electrons: ", Astatine["valElectrons"])
					print("Type of Element: ", Astatine["Type"])
					print("Element Symbol: ", Astatine["elementSymbol"])
					print("Density: ", Astatine["density"], "g/cm3")
					print("Melting Point: ", Astatine["meltingPoint"])
					print("Boiling Point: ", Astatine["boilingPoint"])
					print("______________________________")
				if Start == "radon":
					print("")
					print("Radon:")
					print("______________________________")
					print("Atomic Number: ", Radon["atomicNO"])
					print("Atomic Weight: ", Radon["atomicWeight"])
					print("Electron Configuration: ", Radon["electronConfig"])
					print("Valence Electrons: ", Radon["valElectrons"])
					print("Type of Element: ", Radon["Type"])
					print("Element Symbol: ", Radon["elementSymbol"])
					print("Density: ", Radon["density"], "g/cm3")
					print("Melting Point: ", Radon["meltingPoint"])
					print("Boiling Point: ", Radon["boilingPoint"])
					print("______________________________")
				if Start == "francium":
					print("")
					print("Francium:")
					print("______________________________")
					print("Atomic Number: ", Francium["atomicNO"])
					print("Atomic Weight: ", Francium["atomicWeight"])
					print("Electron Configuration: ", Francium["electronConfig"])
					print("Valence Electrons: ", Francium["valElectrons"])
					print("Type of Element: ", Francium["Type"])
					print("Element Symbol: ", Francium["elementSymbol"])
					print("Density: ", Francium["density"], "g/cm3")
					print("Melting Point: ", Francium["meltingPoint"])
					print("Boiling Point: ", Francium["boilingPoint"])
					print("______________________________")
				if Start == "radium":
					print("")
					print("Radium:")
					print("______________________________")
					print("Atomic Number: ", Radium["atomicNO"])
					print("Atomic Weight: ", Radium["atomicWeight"])
					print("Electron Configuration: ", Radium["electronConfig"])
					print("Valence Electrons: ", Radium["valElectrons"])
					print("Type of Element: ", Radium["Type"])
					print("Element Symbol: ", Radium["elementSymbol"])
					print("Density: ", Radium["density"], "g/cm3")
					print("Melting Point: ", Radium["meltingPoint"])
					print("Boiling Point: ", Radium["boilingPoint"])
					print("______________________________")
				if Start == "actinium":
					print("")
					print("Actinium:")
					print("______________________________")
					print("Atomic Number: ", Actinium["atomicNO"])
					print("Atomic Weight: ", Actinium["atomicWeight"])
					print("Electron Configuration: ", Actinium["electronConfig"])
					print("Valence Electrons: ", Actinium["valElectrons"])
					print("Type of Element: ", Actinium["Type"])
					print("Element Symbol: ", Actinium["elementSymbol"])
					print("Density: ", Actinium["density"], "g/cm3")
					print("Melting Point: ", Actinium["meltingPoint"])
					print("Boiling Point: ", Actinium["boilingPoint"])
					print("______________________________")
				if Start == "thorium":
					print("")
					print("Thorium:")
					print("______________________________")
					print("Atomic Number: ", Thorium["atomicNO"])
					print("Atomic Weight: ", Thorium["atomicWeight"])
					print("Electron Configuration: ", Thorium["electronConfig"])
					print("Valence Electrons: ", Thorium["valElectrons"])
					print("Type of Element: ", Thorium["Type"])
					print("Element Symbol: ", Thorium["elementSymbol"])
					print("Density: ", Thorium["density"], "g/cm3")
					print("Melting Point: ", Thorium["meltingPoint"])
					print("Boiling Point: ", Thorium["boilingPoint"])
					print("______________________________")
				if Start == "protactinium":
					print("")
					print("Protactinium:")
					print("______________________________")
					print("Atomic Number: ", Protactinium["atomicNO"])
					print("Atomic Weight: ", Protactinium["atomicWeight"])
					print("Electron Configuration: ", Protactinium["electronConfig"])
					print("Valence Electrons: ", Protactinium["valElectrons"])
					print("Type of Element: ", Protactinium["Type"])
					print("Element Symbol: ", Protactinium["elementSymbol"])
					print("Density: ", Protactinium["density"], "g/cm3")
					print("Melting Point: ", Protactinium["meltingPoint"])
					print("Boiling Point: ", Protactinium["boilingPoint"])
					print("______________________________")
				if Start == "uranium":
					print("")
					print("Uranium:")
					print("______________________________")
					print("Atomic Number: ", Uranium["atomicNO"])
					print("Atomic Weight: ", Uranium["atomicWeight"])
					print("Electron Configuration: ", Uranium["electronConfig"])
					print("Valence Electrons: ", Uranium["valElectrons"])
					print("Type of Element: ", Uranium["Type"])
					print("Element Symbol: ", Uranium["elementSymbol"])
					print("Density: ", Uranium["density"], "g/cm3")
					print("Melting Point: ", Uranium["meltingPoint"])
					print("Boiling Point: ", Uranium["boilingPoint"])
					print("______________________________")
				if Start == "neptunium":
					print("")
					print("Neptunium:")
					print("______________________________")
					print("Atomic Number: ", Neptunium["atomicNO"])
					print("Atomic Weight: ", Neptunium["atomicWeight"])
					print("Electron Configuration: ", Neptunium["electronConfig"])
					print("Valence Electrons: ", Neptunium["valElectrons"])
					print("Type of Element: ", Neptunium["Type"])
					print("Element Symbol: ", Neptunium["elementSymbol"])
					print("Density: ", Neptunium["density"], "g/cm3")
					print("Melting Point: ", Neptunium["meltingPoint"])
					print("Boiling Point: ", Neptunium["boilingPoint"])
					print("______________________________")
				if Start == "plutonium":
					print("")
					print("Plutonium:")
					print("______________________________")
					print("Atomic Number: ", Plutonium["atomicNO"])
					print("Atomic Weight: ", Plutonium["atomicWeight"])
					print("Electron Configuration: ", Plutonium["electronConfig"])
					print("Valence Electrons: ", Plutonium["valElectrons"])
					print("Type of Element: ", Plutonium["Type"])
					print("Element Symbol: ", Plutonium["elementSymbol"])
					print("Density: ", Plutonium["density"], "g/cm3")
					print("Melting Point: ", Plutonium["meltingPoint"])
					print("Boiling Point: ", Plutonium["boilingPoint"])
					print("______________________________")
				if Start == "americium":
					print("")
					print("Americium:")
					print("______________________________")
					print("Atomic Number: ", Americium["atomicNO"])
					print("Atomic Weight: ", Americium["atomicWeight"])
					print("Electron Configuration: ", Americium["electronConfig"])
					print("Valence Electrons: ", Americium["valElectrons"])
					print("Type of Element: ", Americium["Type"])
					print("Element Symbol: ", Americium["elementSymbol"])
					print("Density: ", Americium["density"], "g/cm3")
					print("Melting Point: ", Americium["meltingPoint"])
					print("Boiling Point: ", Americium["boilingPoint"])
					print("______________________________")
				if Start == "curium":
					print("")
					print("Curium:")
					print("______________________________")
					print("Atomic Number: ", Curium["atomicNO"])
					print("Atomic Weight: ", Curium["atomicWeight"])
					print("Electron Configuration: ", Curium["electronConfig"])
					print("Valence Electrons: ", Curium["valElectrons"])
					print("Type of Element: ", Curium["Type"])
					print("Element Symbol: ", Curium["elementSymbol"])
					print("Density: ", Curium["density"], "g/cm3")
					print("Melting Point: ", Curium["meltingPoint"])
					print("Boiling Point: ", Curium["boilingPoint"])
					print("______________________________")
				if Start == "berkelium":
					print("")
					print("Berkelium:")
					print("______________________________")
					print("Atomic Number: ", Berkelium["atomicNO"])
					print("Atomic Weight: ", Berkelium["atomicWeight"])
					print("Electron Configuration: ", Berkelium["electronConfig"])
					print("Valence Electrons: ", Berkelium["valElectrons"])
					print("Type of Element: ", Berkelium["Type"])
					print("Element Symbol: ", Berkelium["elementSymbol"])
					print("Density: ", Berkelium["density"], "g/cm3")
					print("Melting Point: ", Berkelium["meltingPoint"])
					print("Boiling Point: ", Berkelium["boilingPoint"])
					print("______________________________")
				if Start == "californium":
					print("")
					print("Californium:")
					print("______________________________")
					print("Atomic Number: ", Californium["atomicNO"])
					print("Atomic Weight: ", Californium["atomicWeight"])
					print("Electron Configuration: ", Californium["electronConfig"])
					print("Valence Electrons: ", Californium["valElectrons"])
					print("Type of Element: ", Californium["Type"])
					print("Element Symbol: ", Californium["elementSymbol"])
					print("Density: ", Californium["density"], "g/cm3")
					print("Melting Point: ", Californium["meltingPoint"])
					print("Boiling Point: ", Californium["boilingPoint"])
					print("______________________________")
				if Start == "einsteinium":
					print("")
					print("Einsteinium:")
					print("______________________________")
					print("Atomic Number: ", Einsteinium["atomicNO"])
					print("Atomic Weight: ", Einsteinium["atomicWeight"])
					print("Electron Configuration: ", Einsteinium["electronConfig"])
					print("Valence Electrons: ", Einsteinium["valElectrons"])
					print("Type of Element: ", Einsteinium["Type"])
					print("Element Symbol: ", Einsteinium["elementSymbol"])
					print("Density: ", Einsteinium["density"], "g/cm3")
					print("Melting Point: ", Einsteinium["meltingPoint"])
					print("Boiling Point: ", Einsteinium["boilingPoint"])
					print("______________________________")
				if Start == "fermium":
					print("")
					print("Fermium:")
					print("______________________________")
					print("Atomic Number: ", Fermium["atomicNO"])
					print("Atomic Weight: ", Fermium["atomicWeight"])
					print("Electron Configuration: ", Fermium["electronConfig"])
					print("Valence Electrons: ", Fermium["valElectrons"])
					print("Type of Element: ", Fermium["Type"])
					print("Element Symbol: ", Fermium["elementSymbol"])
					print("Density: ", Fermium["density"], "g/cm3")
					print("Melting Point: ", Fermium["meltingPoint"])
					print("Boiling Point: ", Fermium["boilingPoint"])
					print("______________________________")
				if Start == "mendelevium":
					print("")
					print("Mendelevium:")
					print("______________________________")
					print("Atomic Number: ", Mendelevium["atomicNO"])
					print("Atomic Weight: ", Mendelevium["atomicWeight"])
					print("Electron Configuration: ", Mendelevium["electronConfig"])
					print("Valence Electrons: ", Mendelevium["valElectrons"])
					print("Type of Element: ", Mendelevium["Type"])
					print("Element Symbol: ", Mendelevium["elementSymbol"])
					print("Density: ", Mendelevium["density"], "g/cm3")
					print("Melting Point: ", Mendelevium["meltingPoint"])
					print("Boiling Point: ", Mendelevium["boilingPoint"])
					print("______________________________")
				if Start == "nobelium":
					print("")
					print("Nobelium:")
					print("______________________________")
					print("Atomic Number: ", Nobelium["atomicNO"])
					print("Atomic Weight: ", Nobelium["atomicWeight"])
					print("Electron Configuration: ", Nobelium["electronConfig"])
					print("Valence Electrons: ", Nobelium["valElectrons"])
					print("Type of Element: ", Nobelium["Type"])
					print("Element Symbol: ", Nobelium["elementSymbol"])
					print("Density: ", Nobelium["density"], "g/cm3")
					print("Melting Point: ", Nobelium["meltingPoint"])
					print("Boiling Point: ", Nobelium["boilingPoint"])
					print("______________________________")
				if Start == "lawrencium":
					print("")
					print("Lawrencium:")
					print("______________________________")
					print("Atomic Number: ", Lawrencium["atomicNO"])
					print("Atomic Weight: ", Lawrencium["atomicWeight"])
					print("Electron Configuration: ", Lawrencium["electronConfig"])
					print("Valence Electrons: ", Lawrencium["valElectrons"])
					print("Type of Element: ", Lawrencium["Type"])
					print("Element Symbol: ", Lawrencium["elementSymbol"])
					print("Density: ", Lawrencium["density"], "g/cm3")
					print("Melting Point: ", Lawrencium["meltingPoint"])
					print("Boiling Point: ", Lawrencium["boilingPoint"])
					print("______________________________")
				if Start == "rutherfordium":
					print("")
					print("Rutherfordium:")
					print("______________________________")
					print("Atomic Number: ", Rutherfordium["atomicNO"])
					print("Atomic Weight: ", Rutherfordium["atomicWeight"])
					print("Electron Configuration: ", Rutherfordium["electronConfig"])
					print("Valence Electrons: ", Rutherfordium["valElectrons"])
					print("Type of Element: ", Rutherfordium["Type"])
					print("Element Symbol: ", Rutherfordium["elementSymbol"])
					print("Density: ", Rutherfordium["density"], "g/cm3")
					print("Melting Point: ", Rutherfordium["meltingPoint"])
					print("Boiling Point: ", Rutherfordium["boilingPoint"])
					print("______________________________")
				if Start == "dubnium":
					print("")
					print("Dubnium:")
					print("______________________________")
					print("Atomic Number: ", Dubnium["atomicNO"])
					print("Atomic Weight: ", Dubnium["atomicWeight"])
					print("Electron Configuration: ", Dubnium["electronConfig"])
					print("Valence Electrons: ", Dubnium["valElectrons"])
					print("Type of Element: ", Dubnium["Type"])
					print("Element Symbol: ", Dubnium["elementSymbol"])
					print("Density: ", Dubnium["density"], "g/cm3")
					print("Melting Point: ", Dubnium["meltingPoint"])
					print("Boiling Point: ", Dubnium["boilingPoint"])
					print("______________________________")
				if Start == "seaborgium":
					print("")
					print("Seaborgium:")
					print("______________________________")
					print("Atomic Number: ", Seaborgium["atomicNO"])
					print("Atomic Weight: ", Seaborgium["atomicWeight"])
					print("Electron Configuration: ", Seaborgium["electronConfig"])
					print("Valence Electrons: ", Seaborgium["valElectrons"])
					print("Type of Element: ", Seaborgium["Type"])
					print("Element Symbol: ", Seaborgium["elementSymbol"])
					print("Density: ", Seaborgium["density"], "g/cm3")
					print("Melting Point: ", Seaborgium["meltingPoint"])
					print("Boiling Point: ", Seaborgium["boilingPoint"])
					print("______________________________")
				if Start == "bohrium":
					print("")
					print("Bohrium:")
					print("______________________________")
					print("Atomic Number: ", Bohrium["atomicNO"])
					print("Atomic Weight: ", Bohrium["atomicWeight"])
					print("Electron Configuration: ", Bohrium["electronConfig"])
					print("Valence Electrons: ", Bohrium["valElectrons"])
					print("Type of Element: ", Bohrium["Type"])
					print("Element Symbol: ", Bohrium["elementSymbol"])
					print("Density: ", Bohrium["density"], "g/cm3")
					print("Melting Point: ", Bohrium["meltingPoint"])
					print("Boiling Point: ", Bohrium["boilingPoint"])
					print("______________________________")
				if Start == "hassium":
					print("")
					print("Hassium:")
					print("______________________________")
					print("Atomic Number: ", Hassium["atomicNO"])
					print("Atomic Weight: ", Hassium["atomicWeight"])
					print("Electron Configuration: ", Hassium["electronConfig"])
					print("Valence Electrons: ", Hassium["valElectrons"])
					print("Type of Element: ", Hassium["Type"])
					print("Element Symbol: ", Hassium["elementSymbol"])
					print("Density: ", Hassium["density"], "g/cm3")
					print("Melting Point: ", Hassium["meltingPoint"])
					print("Boiling Point: ", Hassium["boilingPoint"])
					print("______________________________")
				if Start == "meitnerium":
					print("")
					print("Meitnerium:")
					print("______________________________")
					print("Atomic Number: ", Meitnerium["atomicNO"])
					print("Atomic Weight: ", Meitnerium["atomicWeight"])
					print("Electron Configuration: ", Meitnerium["electronConfig"])
					print("Valence Electrons: ", Meitnerium["valElectrons"])
					print("Type of Element: ", Meitnerium["Type"])
					print("Element Symbol: ", Meitnerium["elementSymbol"])
					print("Density: ", Meitnerium["density"], "g/cm3")
					print("Melting Point: ", Meitnerium["meltingPoint"])
					print("Boiling Point: ", Meitnerium["boilingPoint"])
					print("______________________________")
				if Start == "darmstadtium":
					print("")
					print("Darmstadtium:")
					print("______________________________")
					print("Atomic Number: ", Darmstadtium["atomicNO"])
					print("Atomic Weight: ", Darmstadtium["atomicWeight"])
					print("Electron Configuration: ", Darmstadtium["electronConfig"])
					print("Valence Electrons: ", Darmstadtium["valElectrons"])
					print("Type of Element: ", Darmstadtium["Type"])
					print("Element Symbol: ", Darmstadtium["elementSymbol"])
					print("Density: ", Darmstadtium["density"], "g/cm3")
					print("Melting Point: ", Darmstadtium["meltingPoint"])
					print("Boiling Point: ", Darmstadtium["boilingPoint"])
					print("______________________________")
				if Start == "roentgenium":
					print("")
					print("Roentgenium:")
					print("______________________________")
					print("Atomic Number: ", Roentgenium["atomicNO"])
					print("Atomic Weight: ", Roentgenium["atomicWeight"])
					print("Electron Configuration: ", Roentgenium["electronConfig"])
					print("Valence Electrons: ", Roentgenium["valElectrons"])
					print("Type of Element: ", Roentgenium["Type"])
					print("Element Symbol: ", Roentgenium["elementSymbol"])
					print("Density: ", Roentgenium["density"], "g/cm3")
					print("Melting Point: ", Roentgenium["meltingPoint"])
					print("Boiling Point: ", Roentgenium["boilingPoint"])
					print("______________________________")
				if Start == "copernicium":
					print("")
					print("Copernicium:")
					print("______________________________")
					print("Atomic Number: ", Copernicium["atomicNO"])
					print("Atomic Weight: ", Copernicium["atomicWeight"])
					print("Electron Configuration: ", Copernicium["electronConfig"])
					print("Valence Electrons: ", Copernicium["valElectrons"])
					print("Type of Element: ", Copernicium["Type"])
					print("Element Symbol: ", Copernicium["elementSymbol"])
					print("Density: ", Copernicium["density"], "g/cm3")
					print("Melting Point: ", Copernicium["meltingPoint"])
					print("Boiling Point: ", Copernicium["boilingPoint"])
					print("______________________________")
				if Start == "nihonium":
					print("")
					print("Nihonium:")
					print("______________________________")
					print("Atomic Number: ", Nihonium["atomicNO"])
					print("Atomic Weight: ", Nihonium["atomicWeight"])
					print("Electron Configuration: ", Nihonium["electronConfig"])
					print("Valence Electrons: ", Nihonium["valElectrons"])
					print("Type of Element: ", Nihonium["Type"])
					print("Element Symbol: ", Nihonium["elementSymbol"])
					print("Density: ", Nihonium["density"], "g/cm3")
					print("Melting Point: ", Nihonium["meltingPoint"])
					print("Boiling Point: ", Nihonium["boilingPoint"])
					print("______________________________")
				if Start == "flerovium":
					print("")
					print("Flerovium:")
					print("______________________________")
					print("Atomic Number: ", Flerovium["atomicNO"])
					print("Atomic Weight: ", Flerovium["atomicWeight"])
					print("Electron Configuration: ", Flerovium["electronConfig"])
					print("Valence Electrons: ", Flerovium["valElectrons"])
					print("Type of Element: ", Flerovium["Type"])
					print("Element Symbol: ", Flerovium["elementSymbol"])
					print("Density: ", Flerovium["density"], "g/cm3")
					print("Melting Point: ", Flerovium["meltingPoint"])
					print("Boiling Point: ", Flerovium["boilingPoint"])
					print("______________________________")
				if Start == "moscovium":
					print("")
					print("Moscovium:")
					print("______________________________")
					print("Atomic Number: ", Moscovium["atomicNO"])
					print("Atomic Weight: ", Moscovium["atomicWeight"])
					print("Electron Configuration: ", Moscovium["electronConfig"])
					print("Valence Electrons: ", Moscovium["valElectrons"])
					print("Type of Element: ", Moscovium["Type"])
					print("Element Symbol: ", Moscovium["elementSymbol"])
					print("Density: ", Moscovium["density"], "g/cm3")
					print("Melting Point: ", Moscovium["meltingPoint"])
					print("Boiling Point: ", Moscovium["boilingPoint"])
					print("______________________________")
				if Start == "livermorium":
					print("")
					print("Livermorium:")
					print("______________________________")
					print("Atomic Number: ", Livermorium["atomicNO"])
					print("Atomic Weight: ", Livermorium["atomicWeight"])
					print("Electron Configuration: ", Livermorium["electronConfig"])
					print("Valence Electrons: ", Livermorium["valElectrons"])
					print("Type of Element: ", Livermorium["Type"])
					print("Element Symbol: ", Livermorium["elementSymbol"])
					print("Density: ", Livermorium["density"], "g/cm3")
					print("Melting Point: ", Livermorium["meltingPoint"])
					print("Boiling Point: ", Livermorium["boilingPoint"])
					print("______________________________")
					print("")
				if Start == "tennessine":
					print("")
					print("Tennessine:")
					print("______________________________")
					print("Atomic Number: ", Tennessine["atomicNO"])
					print("Atomic Weight: ", Tennessine["atomicWeight"])
					print("Electron Configuration: ", Tennessine["electronConfig"])
					print("Valence Electrons: ", Tennessine["valElectrons"])
					print("Type of Element: ", Tennessine["Type"])
					print("Element Symbol: ", Tennessine["elementSymbol"])
					print("Density: ", Tennessine["density"], "g/cm3")
					print("Melting Point: ", Tennessine["meltingPoint"])
					print("Boiling Point: ", Tennessine["boilingPoint"])
					print("______________________________")
				if Start == "oganesson":
					print("")
					print("Oganesson:")
					print("______________________________")
					print("Atomic Number: ", Oganesson["atomicNO"])
					print("Atomic Weight: ", Oganesson["atomicWeight"])
					print("Electron Configuration: ", Oganesson["electronConfig"])
					print("Valence Electrons: ", Oganesson["valElectrons"])
					print("Type of Element: ", Oganesson["Type"])
					print("Element Symbol: ", Oganesson["elementSymbol"])
					print("Density: ", Oganesson["density"], "g/cm3")
					print("Melting Point: ", Oganesson["meltingPoint"])
					print("Boiling Point: ", Oganesson["boilingPoint"])
					print("______________________________")
			print("")
			Exit=input("Again? Y or N: ").lower()
			if Exit == "y":
				chem=True
				print("")
				print("")
			if Exit == "n":
				chem=False
				sys.exit()
	if calculator_machine =="g":
		geo=True
		while geo is True:
			print("")
			print("________________________________________________________________________________________________________")
			print("Pythagorean Theorem:")
			print("")
			geometrypythag = input("What side do you need to find? (A)  (B)  (HY): ").lower()
			if geometrypythag == "a":
				fsideb = float(input("Enter the number for b: "))
				fsidehy = float(input("Enter the hypotenuse: "))
				print("")
				Faesideb = fsideb*fsideb
				Faesidehy = fsidehy*fsidehy
				Output = Faesidehy-Faesideb
				ROutput= Output** 0.5
				print("A = ", str(ROutput))
			if geometrypythag == "b":
				fsidea = float(input("Enter the number for a: "))
				fsidehy = float(input("Enter the hypotenuse: "))
				print("")
				Faesidea = fsidea*fsidea
				Faesidehy = fsidehy*fsidehy
				Output = Faesidehy-Faesidea
				ROutput= Output** 0.5
				print("B = ", str(ROutput))
			if geometrypythag == "hy":
				fsideb = float(input("Enter the number for b: "))
				fsidea = float(input("Enter the number for a: "))
				print("")
				Faesideb = fsideb*fsideb
				Faesidea = fsidea*fsidea
				Output = Faesidea+Faesideb
				ROutput = Output** 0.5
				print("Hypotenuse = ", str(ROutput))
				print("")
			pythag=input("Again? Y or N: ").lower()
			if pythag == "y":
				geo=True
			if pythag == "n":
				geo=False
				sys.exit()
	if calculator_machine =="ma":
		a = True
		while a is True:
			Hehe=[]
			Haha=[]
			print("________________________________________________________________________________________________________")
			moreMatrix_Action = input("Do you want to multiply a Matrix by a given number x(M1)? Y or N: ").lower()
			if moreMatrix_Action == "y":
				print("")
				maSize = input("What dimentions do you want the Matrix to be? Max:4x4: ").lower()
				print("")
				maNum = input("What number do you want to multiply by: ")
				print("")
				if maSize == "1x1":
					print(onexone)
				if maSize == "1x2":
					print(onextwo)
				if maSize == "1x3":
					print(onexthree)
				if maSize == "2x3":
					print(twoxthree)
				if maSize == "2x2":
					print(twoxtwo)
				if maSize == "2x1":
					print(twoxone)
				if maSize == "3x2":
					print(threextwo)
				if maSize == "3x1":
					print(threexone)
				if maSize == "3x3":
					print(threexthree)	
				if maSize == "4x1":
					print(fourxone)
				if maSize == "4x2":
					print(fourxtwo)
				if maSize == "4x3":
					print(fourxthree)
				if maSize == "4x4":
					print(fourxfour)	
				if maSize == "1x4":
					print(onexfour)
				if maSize == "2x4":
					print(twoxfour)
				if maSize == "3x4":
					print(threexfour)
				print("")	
				if maSize == "1x1":
					R1onexoneC1 = input("What number is R1: C1: ")
				if maSize == "1x2":
					R1onextwoC1 = input("What number is R1: C1: ")
					R1onextwoC2 = input("What number is R1: C2: ")
				if maSize == "2x1":
					R1twoxoneC1 = input("What number is R1: C1: ")
					R2twoxoneC1 = input("What number is R2: C1: ")
				if maSize == "1x3":
					R1onexthreeC1 = input("What number is R1: C1: ")
					R1onexthreeC2 = input("What number is R1: C2: ")
					R1onexthreeC3 = input("What number is R1: C3: ")
				if maSize == "3x1":
					R1threexoneC1 = input("What number is R1: C1: ")
					R2threexoneC1 = input("What number is R2: C1: ")
					R3threexoneC1 = input("What number is R3: C1: ")
				if maSize == "2x2":
					R1twoxtwoC1 = input("What number is R1: C1: ")
					R1twoxtwoC2 = input("What number is R1: C2: ")
					R2twoxtwoC1 = input("What number is R2: C1: ")
					R2twoxtwoC2 = input("What number is R2: C2: ")
				if maSize == "2x3":
					R1twoxthreeC1 = input("What number is R1: C1: ")
					R1twoxthreeC2 = input("What number is R1: C2: ")
					R1twoxthreeC3 = input("What number is R1: C3: ")
					R2twoxthreeC1 = input("What number is R2: C1: ")
					R2twoxthreeC2 = input("What number is R2: C2: ")
					R2twoxthreeC3 = input("What number is R2: C3: ")
				if maSize == "3x2":
					R1threextwoC1 = input("What number is R1: C1: ")
					R1threextwoC2 = input("What number is R1: C2: ")
					R2threextwoC1 = input("What number is R2: C1: ")
					R2threextwoC2 = input("What number is R2: C2: ")
					R3threextwoC1 = input("What number is R2: C1: ")
					R3threextwoC2 = input("What number is R2: C2: ")
				if maSize == "3x3":
					R1threexthreeC1 = input("What number is R1: C1: ")
					R1threexthreeC2 = input("What number is R1: C2: ")
					R1threexthreeC3 = input("What number is R1: C3: ")
					R2threexthreeC1 = input("What number is R2: C1: ")
					R2threexthreeC2 = input("What number is R2: C2: ")
					R2threexthreeC3 = input("What number is R2: C3: ")
					R3threexthreeC1 = input("What number is R3: C1: ")
					R3threexthreeC2 = input("What number is R3: C2: ")
					R3threexthreeC3 = input("What number is R3: C3: ")
				if maSize == "4x1":
					R1fourxoneC1 = input("What number is R1: C1: ")
					R2fourxoneC1 = input("What number is R2: C1: ")
					R3fourxoneC1 = input("What number is R3: C1: ")
					R4fourxoneC1 = input("What number is R4: C1: ")
				if maSize == "4x2":
					R1fourxtwoC1 = input("What number is R1: C1: ")
					R1fourxtwoC2 = input("What number is R1: C2: ")
					R2fourxtwoC1 = input("What number is R2: C1: ")
					R2fourxtwoC2 = input("What number is R2: C2: ")
					R3fourxtwoC1 = input("What number is R3: C1: ")
					R3fourxtwoC2 = input("What number is R3: C2: ")
					R4fourxtwoC1 = input("What number is R4: C1: ")
					R4fourxtwoC2 = input("What number is R4: C2: ")
				if maSize == "4x3":
					R1fourxthreeC1 = input("What number is R1: C1: ")
					R1fourxthreeC2 = input("What number is R1: C2: ")
					R1fourxthreeC3 = input("What number is R1: C3: ")
					R2fourxthreeC1 = input("What number is R2: C1: ")
					R2fourxthreeC2 = input("What number is R2: C2: ")
					R2fourxthreeC3 = input("What number is R2: C3: ")
					R3fourxthreeC1 = input("What number is R3: C1: ")
					R3fourxthreeC2 = input("What number is R3: C2: ")
					R3fourxthreeC3 = input("What number is R3: C3: ")
					R4fourxthreeC1 = input("What number is R4: C1: ")
					R4fourxthreeC2 = input("What number is R4: C2: ")
					R4fourxthreeC3 = input("What number is R4: C3: ")
				if maSize == "4x4":
					R1fourxfourC1 = input("What number is R1: C1: ")
					R1fourxfourC2 = input("What number is R1: C2: ")
					R1fourxfourC3 = input("What number is R1: C3: ")
					R1fourxfourC4 = input("What number is R1: C4: ")
					R2fourxfourC1 = input("What number is R2: C1: ")
					R2fourxfourC2 = input("What number is R2: C2: ")
					R2fourxfourC3 = input("What number is R2: C3: ")
					R2fourxfourC4 = input("What number is R2: C4: ")
					R3fourxfourC1 = input("What number is R3: C1: ")
					R3fourxfourC2 = input("What number is R3: C2: ")
					R3fourxfourC3 = input("What number is R3: C3: ")
					R3fourxfourC4 = input("What number is R3: C4: ")
					R4fourxfourC1 = input("What number is R4: C1: ")
					R4fourxfourC2 = input("What number is R4: C2: ")
					R4fourxfourC3 = input("What number is R4: C3: ")
					R4fourxfourC4 = input("What number is R4: C4: ")
				if maSize == "1x4":
					R1onexfourC1 = input("What number is R1: C1: ")
					R1onexfourC2 = input("What number is R1: C2: ")
					R1onexfourC3 = input("What number is R1: C3: ")
					R1onexfourC4 = input("What number is R1: C4: ")	
				if maSize == "2x4":
					R1twoxfourC1 = input("What number is R1: C1: ")
					R1twoxfourC2 = input("What number is R1: C2: ")
					R1twoxfourC3 = input("What number is R1: C3: ")
					R1twoxfourC4 = input("What number is R1: C4: ")
					R2twoxfourC1 = input("What number is R2: C1: ")
					R2twoxfourC2 = input("What number is R2: C2: ")
					R2twoxfourC3 = input("What number is R2: C3: ")
					R2twoxfourC4 = input("What number is R2: C4: ")
				if maSize == "3x4":
					R1threexfourC1 = input("What number is R1: C1: ")
					R1threexfourC2 = input("What number is R1: C2: ")
					R1threexfourC3 = input("What number is R1: C3: ")
					R1threexfourC4 = input("What number is R1: C4: ")
					R2threexfourC1 = input("What number is R2: C1: ")
					R2threexfourC2 = input("What number is R2: C2: ")
					R2threexfourC3 = input("What number is R2: C3: ")
					R2threexfourC4 = input("What number is R2: C4: ")								
					R3threexfourC1 = input("What number is R3: C1: ")
					R3threexfourC2 = input("What number is R3: C2: ")
					R3threexfourC3 = input("What number is R3: C3: ")
					R3threexfourC4 = input("What number is R3: C4: ")
				print("")
				print("")
				question = input("Start calculation, press (enter) to continue")
				print("")
				print("")
				if maSize == "4x1":
					faNum37 = int(R1fourxoneC1)*int(maNum)
					faNum38 = int(R2fourxoneC1)*int(maNum)
					faNum39 = int(R3fourxoneC1)*int(maNum)
					faNum40 = int(R4fourxoneC1)*int(maNum)
					print("["+str(faNum37)+"]")
					print("["+str(faNum38)+"]")
					print("["+str(faNum39)+"]")
					print("["+str(faNum40)+"]")
				if maSize == "4x2":
					faNum41 = int(R1fourxtwoC1)*int(maNum)
					faNum42 = int(R1fourxtwoC2)*int(maNum)
					faNum43 = int(R2fourxtwoC1)*int(maNum)
					faNum44 = int(R2fourxtwoC2)*int(maNum)
					faNum45 = int(R3fourxtwoC1)*int(maNum)
					faNum46 = int(R3fourxtwoC2)*int(maNum)
					faNum47 = int(R4fourxtwoC1)*int(maNum)
					faNum48 = int(R4fourxtwoC2)*int(maNum)
					print("["+str(faNum41)+" "+str(faNum42)+"]")
					print("["+str(faNum43)+" "+str(faNum44)+"]")
					print("["+str(faNum45)+" "+str(faNum46)+"]")
					print("["+str(faNum47)+" "+str(faNum48)+"]")
				if maSize == "4x3":
					faNum49 = int(R1fourxthreeC1)*int(maNum)
					faNum50 = int(R1fourxthreeC2)*int(maNum)
					faNum51 = int(R1fourxthreeC3)*int(maNum)
					faNum52 = int(R2fourxthreeC1)*int(maNum)
					faNum53 = int(R2fourxthreeC2)*int(maNum)
					faNum54 = int(R2fourxthreeC3)*int(maNum)
					faNum55 = int(R3fourxthreeC1)*int(maNum)
					faNum56 = int(R3fourxthreeC2)*int(maNum)
					faNum57 = int(R3fourxthreeC3)*int(maNum)
					faNum58 = int(R4fourxthreeC1)*int(maNum)
					faNum59 = int(R4fourxthreeC2)*int(maNum)
					faNum60 = int(R4fourxthreeC3)*int(maNum)
					print("["+str(faNum49)+" "+str(faNum50)+" "+str(faNum51)+"]")
					print("["+str(faNum52)+" "+str(faNum53)+" "+str(faNum54)+"]")
					print("["+str(faNum55)+" "+str(faNum56)+" "+str(faNum57)+"]")
					print("["+str(faNum58)+" "+str(faNum59)+" "+str(faNum60)+"]")
				if maSize == "1x4":
					faNum61 = int(R1onexfourC1)*int(maNum)
					faNum62 = int(R1onexfourC2)*int(maNum)
					faNum63 = int(R1onexfourC3)*int(maNum)
					faNum64 = int(R1onexfourC4)*int(maNum)
					print("["+str(faNum61)+" "+str(faNum62)+" "+str(faNum63)+" "+str(faNum64)+"]")
				if maSize == "2x4":
					faNum65 = int(R1twoxfourC1)*int(maNum)
					faNum66 = int(R1twoxfourC2)*int(maNum)
					faNum67 = int(R1twoxfourC3)*int(maNum)
					faNum68 = int(R1twoxfourC4)*int(maNum)
					faNum69 = int(R2twoxfourC1)*int(maNum)
					faNum70 = int(R2twoxfourC2)*int(maNum)
					faNum71 = int(R2twoxfourC3)*int(maNum)
					faNum72 = int(R2twoxfourC4)*int(maNum)
					print("["+str(faNum65)+" "+str(faNum66)+" "+str(faNum67)+" "+str(faNum68)+"]")
					print("["+str(faNum69)+" "+str(faNum70)+" "+str(faNum71)+" "+str(faNum72)+"]")
				if maSize == "3x4":	
					faNum73 = int(R1threexfourC1)*int(maNum)
					faNum74 = int(R1threexfourC2)*int(maNum)
					faNum75 = int(R1threexfourC3)*int(maNum)
					faNum76 = int(R1threexfourC4)*int(maNum)
					faNum77 = int(R2threexfourC1)*int(maNum)
					faNum78 = int(R2threexfourC2)*int(maNum)
					faNum79 = int(R2threexfourC3)*int(maNum)
					faNum80 = int(R2threexfourC4)*int(maNum)
					faNum81 = int(R3threexfourC1)*int(maNum)
					faNum82 = int(R3threexfourC2)*int(maNum)
					faNum83 = int(R3threexfourC3)*int(maNum)
					faNum84 = int(R3threexfourC4)*int(maNum)
					print("["+str(faNum73)+" "+str(faNum74)+" "+str(faNum75)+" "+str(faNum76)+"]")
					print("["+str(faNum77)+" "+str(faNum78)+" "+str(faNum79)+" "+str(faNum80)+"]")
					print("["+str(faNum81)+" "+str(faNum82)+" "+str(faNum83)+" "+str(faNum84)+"]")
				if maSize == "4x4":
					faNum84 = int(R1fourxfourC1)*int(maNum)
					faNum85 = int(R1fourxfourC2)*int(maNum)
					faNum86 = int(R1fourxfourC3)*int(maNum)
					faNum87 = int(R1fourxfourC4)*int(maNum)
					faNum88 = int(R2fourxfourC1)*int(maNum)
					faNum89 = int(R2fourxfourC2)*int(maNum)
					faNum90 = int(R2fourxfourC3)*int(maNum)
					faNum91 = int(R2fourxfourC4)*int(maNum)
					faNum92 = int(R3fourxfourC1)*int(maNum)
					faNum93 = int(R3fourxfourC2)*int(maNum)
					faNum94 = int(R3fourxfourC3)*int(maNum)
					faNum95 = int(R3fourxfourC4)*int(maNum)
					faNum96 = int(R4fourxfourC1)*int(maNum)
					faNum97 = int(R4fourxfourC2)*int(maNum)
					faNum98 = int(R4fourxfourC3)*int(maNum)
					faNum99 = int(R4fourxfourC4)*int(maNum)
					faNum100 = "YAY WE REACHED 100!"
					print("["+str(faNum84)+" "+str(faNum85)+" "+str(faNum86)+" "+str(faNum87)+"]")
					print("["+str(faNum88)+" "+str(faNum89)+" "+str(faNum90)+" "+str(faNum91)+"]")
					print("["+str(faNum92)+" "+str(faNum93)+" "+str(faNum94)+" "+str(faNum95)+"]")
					print("["+str(faNum96)+" "+str(faNum97)+" "+str(faNum98)+" "+str(faNum99)+"]")
				if maSize == "1x1":
					faNum1 = int(R1onexoneC1)*int(maNum)
					print("["+str(faNum1)+"]")
				if maSize == "1x2":
					faNum2 = int(R1onextwoC1)*int(maNum)
					faNum3 = int(R1onextwoC2)*int(maNum)
					print("["+str(faNum2)+" "+str(faNum3)+"]")
				if maSize == "1x3":
					faNum4 = int(R1onexthreeC1)*int(maNum)
					faNum5 = int(R1onexthreeC2)*int(maNum)
					faNum6 = int(R1onexthreeC3)*int(maNum)
					print("["+str(faNum4)+" "+str(faNum5)+" "+str(faNum6)+"]")
				if maSize == "2x3":
					faNum7 = int(R1twoxthreeC1)*int(maNum)
					faNum8 = int(R1twoxthreeC2)*int(maNum)
					faNum9 = int(R1twoxthreeC3)*int(maNum)
					faNum10 = int(R2twoxthreeC1)*int(maNum)
					faNum11 = int(R2twoxthreeC2)*int(maNum)
					faNum12 = int(R2twoxthreeC3)*int(maNum)
					print("["+str(faNum7)+" "+str(faNum8)+" "+str(faNum9)+"]")
					print("["+str(faNum10)+" "+str(faNum11)+" "+str(faNum12)+"]")
				if maSize == "2x2":
					faNum13 = int(R1twoxtwoC1)*int(maNum)
					faNum14 = int(R1twoxtwoC2)*int(maNum)
					faNum15 = int(R2twoxtwoC1)*int(maNum)
					faNum16 = int(R2twoxtwoC2)*int(maNum)
					print("["+str(faNum13)+" "+str(faNum14)+"]")
					print("["+str(faNum15)+" "+str(faNum16)+"]")
				if maSize == "2x1":
					faNum17 = int(R1twoxoneC1)*int(maNum)
					faNum18 = int(R2twoxoneC1)*int(maNum)
					print("["+str(faNum17)+"]")
					print("["+str(faNum18)+"]")
				if maSize == "3x2":
					faNum19 = int(R1threextwoC1)*int(maNum)
					faNum20 = int(R1threextwoC2)*int(maNum)
					faNum21 = int(R2threextwoC1)*int(maNum)
					faNum22 = int(R2threextwoC2)*int(maNum)
					faNum23 = int(R3threextwoC1)*int(maNum)
					faNum24 = int(R3threextwoC2)*int(maNum)
					print("["+str(faNum19)+" "+str(faNum20)+"]")
					print("["+str(faNum21)+" "+str(faNum22)+"]")
					print("["+str(faNum23)+" "+str(faNum24)+"]")
				if maSize == "3x1":
					faNum25 = int(R1threexoneC1)*int(maNum)
					faNum26 = int(R2threexoneC1)*int(maNum)
					faNum27 = int(R3threexoneC1)*int(maNum)
					print("["+str(faNum25)+"]")
					print("["+str(faNum26)+"]")
					print("["+str(faNum27)+"]")
				if maSize == "3x3":
					faNum28 = int(R1threexthreeC1)*int(maNum)
					faNum29 = int(R1threexthreeC2)*int(maNum)
					faNum30 = int(R1threexthreeC3)*int(maNum)
					faNum31 = int(R2threexthreeC1)*int(maNum)
					faNum32 = int(R2threexthreeC2)*int(maNum)
					faNum33 = int(R2threexthreeC3)*int(maNum)
					faNum34 = int(R3threexthreeC1)*int(maNum)
					faNum35 = int(R3threexthreeC2)*int(maNum)
					faNum36 = int(R3threexthreeC3)*int(maNum)
					print("["+str(faNum28)+" "+str(faNum29)+" "+str(faNum30)+"]")
					print("["+str(faNum31)+" "+str(faNum32)+" "+str(faNum33)+"]")
					print("["+str(faNum34)+" "+str(faNum35)+" "+str(faNum36)+"]")
					print("")
					print("")
				print("")
				print("")
				maAgain = input("Again? Y or N: ").lower()
				if maAgain == "y":
					print("")
					print("")
					print("")
					a = True
				if maAgain == "n":
					a = False
					sys.exit()
			if moreMatrix_Action == "n":		
				print("")	
				Matrix1_size = input("what dimentions do you want to matrix 1 to be? Max:3x3: ").lower()
				time.sleep(.25)
				Matrix2_size = input("what dimentions do you want to matrix 2 to be? Max:3x3: ").lower()
				time.sleep(.25)
				def split(Matrix1_size):
					return [char for char in Matrix1_size]  
				Matrix_Check1 = Matrix1_size
				#print(split(Matrix_Check1))
				def split(Matrix2_size):
					return [char for char in Matrix2_size]  
				Matrix_Check2 = Matrix2_size
				#print(split(Matrix_Check2))
				if Matrix_Check1[2] != Matrix_Check2[0]:
					print("")
					print("")
					print("")
					matrixAgain = input("--The dimensions given are a dimension mismatch, press (enter) to continue--")
					print("")
					print("")
					print("")
					Haha.append("hrrrrm")
					print("________________________________________________________________________________________________________")
				elif len(Haha) != 0: #Change "elif" to "if" to only allow multiplications
					a=True
					sys.exit()
				else:
					a=False
					print("")
					print("")
					print("")
					question = input("--Your dimentions work, press (enter) to continue--")
					print("")
					print("")
					print("")
				if Matrix1_size == "1x1":
					print("M1= "+onexone)
				if Matrix1_size == "1x2":
					print("M1= "+onextwo)
				if Matrix1_size == "1x3":
					print("M1= "+onexthree)
				if Matrix1_size == "2x3":
					print("M1= "+twoxthree)
				if Matrix1_size == "2x2":
					print("M1= "+twoxtwo)
				if Matrix1_size == "2x1":
					print("M1= "+twoxone)
				if Matrix1_size == "3x2":
					print("M1= "+threextwo)
				if Matrix1_size == "3x1":
					print("M1= "+threexone)
				if Matrix1_size == "3x3":
					print("M1= "+threexthree)
				if Matrix1_size == "4x1":
					print("M1= "+fourxone)
				if Matrix1_size == "4x2":
					print("M1= "+fourxtwo)
				if Matrix1_size == "4x3":
					print("M1= "+fourxthree)
				if Matrix1_size == "1x4":
					print("M1= "+onexfour)
				if Matrix1_size == "2x4":
					print("M1= "+twoxfour)
				if Matrix1_size == "3x4":
					print("M1= "+threexfour)
				if Matrix1_size == "4x4":
					print("M1= "+fourxfour)				
				else: 
					print("")
					print("")
					print("")
					a = True
				if Matrix2_size == "1x1":
					print("M2= "+onexone)
				if Matrix2_size == "1x2":
					print("M2= "+onextwo)
				if Matrix2_size == "1x3":
					print("M2= "+onexthree)
				if Matrix2_size == "2x3":
					print("M2= "+twoxthree)
				if Matrix2_size == "2x2":
					print("M2= "+twoxtwo)
				if Matrix2_size == "2x1":
					print("M2= "+twoxone)
				if Matrix2_size == "3x2":
					print("M2= "+threextwo)
				if Matrix2_size == "3x1":
					print("M2= "+threexone)
				if Matrix2_size == "3x3":
					print("M2= "+threexthree)
				if Matrix2_size == "4x1":
					print("M2= "+fourxone)
				if Matrix2_size == "4x2":
					print("M2= "+fourxtwo)
				if Matrix2_size == "4x3":
					print("M2= "+fourxthree)
				if Matrix2_size == "1x4":
					print("M2= "+onexfour)
				if Matrix2_size == "2x4":
					print("M2= "+twoxfour)
				if Matrix2_size == "3x4":
					print("M2= "+threexfour)
				if Matrix2_size == "4x4":
					print("M2= "+fourxfour)	
				else:
					print("")
					Hehe.append("OOOOOFFF")
					print("")
					print("")				
					a = True
				if len(Hehe) != 0:
					a = False
				a = False
				print("Start Putting in Values for M1")
				print("")
				if Matrix1_size == "1x1":
					M1R1onexoneC1 = input("What number is M1R1: C1: ")
				if Matrix1_size == "1x2":
					M1R1onextwoC1 = input("What number is M1R1: C1: ")
					M1R1onextwoC2 = input("What number is M1R1: C2: ")
				if Matrix1_size == "2x1":
					M1R1twoxoneC1 = input("What number is M1R1: C1: ")
					M1R2twoxoneC1 = input("What number is M1R2: C1: ")
				if Matrix1_size == "1x3":
					M1R1onexthreeC1 = input("What number is M1R1: C1: ")
					M1R1onexthreeC2 = input("What number is M1R1: C2: ")
					M1R1onexthreeC3 = input("What number is M1R1: C3: ")
				if Matrix1_size == "3x1":
					M1R1threexoneC1 = input("What number is M1R1: C1: ")
					M1R2threexoneC1 = input("What number is M1R2: C1: ")
					M1R3threexoneC1 = input("What number is M1R3: C1: ")
				if Matrix1_size == "2x2":
					M1R1twoxtwoC1 = input("What number is M1R1: C1: ")
					M1R1twoxtwoC2 = input("What number is M1R1: C2: ")
					M1R2twoxtwoC1 = input("What number is M1R2: C1: ")
					M1R2twoxtwoC2 = input("What number is M1R2: C2: ")
				if Matrix1_size == "2x3":
					M1R1twoxthreeC1 = input("What number is M1R1: C1: ")
					M1R1twoxthreeC2 = input("What number is M1R1: C2: ")
					M1R1twoxthreeC3 = input("What number is M1R1: C3: ")
					M1R2twoxthreeC1 = input("What number is M1R2: C1: ")
					M1R2twoxthreeC2 = input("What number is M1R2: C2: ")
					M1R2twoxthreeC3 = input("What number is M1R2: C3: ")
				if Matrix1_size == "3x2":
					M1R1threextwoC1 = input("What number is M1R1: C1: ")
					M1R1threextwoC2 = input("What number is M1R1: C2: ")
					M1R2threextwoC1 = input("What number is M1R2: C1: ")
					M1R2threextwoC2 = input("What number is M1R2: C2: ")
					M1R3threextwoC1 = input("What number is M1R2: C1: ")
					M1R3threextwoC2 = input("What number is M1R2: C2: ")
				if Matrix1_size == "3x3":
					M1R1threexthreeC1 = input("What number is M1R1: C1: ")
					M1R1threexthreeC2 = input("What number is M1R1: C2: ")
					M1R1threexthreeC3 = input("What number is M1R1: C3: ")
					M1R2threexthreeC1 = input("What number is M1R2: C1: ")
					M1R2threexthreeC2 = input("What number is M1R2: C2: ")
					M1R2threexthreeC3 = input("What number is M1R2: C3: ")
					M1R3threexthreeC1 = input("What number is M1R3: C1: ")
					M1R3threexthreeC2 = input("What number is M1R3: C2: ")
					M1R3threexthreeC3 = input("What number is M1R3: C3: ")
				if Matrix1_size == "4x1":
					M1R1fourxoneC1 = input("What number is M1R1: C1: ")
					M1R2fourxoneC1 = input("What number is M1R2: C1: ")
					M1R3fourxoneC1 = input("What number is M1R3: C1: ")
					M1R4fourxoneC1 = input("What number is M1R4: C1: ")
				if Matrix1_size == "4x2":
					M1R1fourxtwoC1 = input("What number is M1R1: C1: ")
					M1R1fourxtwoC2 = input("What number is M1R1: C2: ")
					M1R2fourxtwoC1 = input("What number is M1R2: C1: ")
					M1R2fourxtwoC2 = input("What number is M1R2: C2: ")
					M1R3fourxtwoC1 = input("What number is M1R3: C1: ")
					M1R3fourxtwoC2 = input("What number is M1R3: C2: ")
					M1R4fourxtwoC1 = input("What number is M1R4: C1: ")
					M1R4fourxtwoC2 = input("What number is M1R4: C2: ")
				if Matrix1_size == "4x3":
					M1R1fourxthreeC1 = input("What number is M1R1: C1: ")
					M1R1fourxthreeC2 = input("What number is M1R1: C2: ")
					M1R1fourxthreeC3 = input("What number is M1R1: C3: ")
					M1R2fourxthreeC1 = input("What number is M1R2: C1: ")
					M1R2fourxthreeC2 = input("What number is M1R2: C2: ")
					M1R2fourxthreeC3 = input("What number is M1R2: C3: ")
					M1R3fourxthreeC1 = input("What number is M1R3: C1: ")
					M1R3fourxthreeC2 = input("What number is M1R3: C2: ")
					M1R3fourxthreeC3 = input("What number is M1R3: C3: ")
					M1R4fourxthreeC1 = input("What number is M1R4: C1: ")
					M1R4fourxthreeC2 = input("What number is M1R4: C2: ")
					M1R4fourxthreeC3 = input("What number is M1R4: C3: ")
				if Matrix1_size == "4x4":
					M1R1fourxfourC1 = input("What number is M1R1: C1: ")
					M1R1fourxfourC2 = input("What number is M1R1: C2: ")
					M1R1fourxfourC3 = input("What number is M1R1: C3: ")
					M1R1fourxfourC4 = input("What number is M1R1: C4: ")
					M1R2fourxfourC1 = input("What number is M1R2: C1: ")
					M1R2fourxfourC2 = input("What number is M1R2: C2: ")
					M1R2fourxfourC3 = input("What number is M1R2: C3: ")
					M1R2fourxfourC4 = input("What number is M1R2: C4: ")
					M1R3fourxfourC1 = input("What number is M1R3: C1: ")
					M1R3fourxfourC2 = input("What number is M1R3: C2: ")
					M1R3fourxfourC3 = input("What number is M1R3: C3: ")
					M1R3fourxfourC4 = input("What number is M1R3: C4: ")
					M1R4fourxfourC1 = input("What number is M1R4: C1: ")
					M1R4fourxfourC2 = input("What number is M1R4: C2: ")
					M1R4fourxfourC3 = input("What number is M1R4: C3: ")
					M1R4fourxfourC4 = input("What number is M1R4: C4: ")
				if Matrix1_size == "1x4":
					M1R1onexfourC1 = input("What number is M1R1: C1: ")
					M1R1onexfourC2 = input("What number is M1R1: C2: ")
					M1R1onexfourC3 = input("What number is M1R1: C3: ")
					M1R1onexfourC4 = input("What number is M1R1: C4: ")	
				if Matrix1_size == "2x4":
					M1R1twoxfourC1 = input("What number is M1R1: C1: ")
					M1R1twoxfourC2 = input("What number is M1R1: C2: ")
					M1R1twoxfourC3 = input("What number is M1R1: C3: ")
					M1R1twoxfourC4 = input("What number is M1R1: C4: ")
					M1R2twoxfourC1 = input("What number is M1R2: C1: ")
					M1R2twoxfourC2 = input("What number is M1R2: C2: ")
					M1R2twoxfourC3 = input("What number is M1R2: C3: ")
					M1R2twoxfourC4 = input("What number is M1R2: C4: ")
				if Matrix1_size == "3x4":
					M1R1threexfourC1 = input("What number is M1R1: C1: ")
					M1R1threexfourC2 = input("What number is M1R1: C2: ")
					M1R1threexfourC3 = input("What number is M1R1: C3: ")
					M1R1threexfourC4 = input("What number is M1R1: C4: ")
					M1R2threexfourC1 = input("What number is M1R2: C1: ")
					M1R2threexfourC2 = input("What number is M1R2: C2: ")
					M1R2threexfourC3 = input("What number is M1R2: C3: ")
					M1R2threexfourC4 = input("What number is M1R2: C4: ")
					M1R3threexfourC1 = input("What number is M1R3: C1: ")
					M1R3threexfourC2 = input("What number is M1R3: C2: ")
					M1R3threexfourC3 = input("What number is M1R3: C3: ")
					M1R3threexfourC4 = input("What number is M1R3: C4: ")
				print("")
				print("Start Putting in Values for M2")
				print("")
				if Matrix2_size == "1x1":
					M2R1onexoneC1 = input("What number is M2R1: C1: ")
				if Matrix2_size == "1x2":
					M2R1onextwoC1 = input("What number is M2R1: C1: ")
					M2R1onextwoC2 = input("What number is M2R1: C2: ")
				if Matrix2_size == "2x1":
					M2R1twoxoneC1 = input("What number is M2R1: C1: ")
					M2R2twoxoneC1 = input("What number is M2R2: C1: ")
				if Matrix2_size == "1x3":
					M2R1onexthreeC1 = input("What number is M2R1: C1: ")
					M2R1onexthreeC2 = input("What number is M2R1: C2: ")
					M2R1onexthreeC3 = input("What number is M2R1: C3: ")
				if Matrix2_size == "3x1":
					M2R1threexoneC1 = input("What number is M2R1: C1: ")
					M2R2threexoneC1 = input("What number is M2R2: C1: ")
					M2R3threexoneC1 = input("What number is M2R3: C1: ")
				if Matrix2_size == "2x2":
					M2R1twoxtwoC1 = input("What number is M2R1: C1: ")
					M2R1twoxtwoC2 = input("What number is M2R1: C2: ")
					M2R2twoxtwoC1 = input("What number is M2R2: C1: ")
					M2R2twoxtwoC2 = input("What number is M2R2: C2: ")
				if Matrix2_size == "2x3":
					M2R1twoxthreeC1 = input("What number is M2R1: C1: ")
					M2R1twoxthreeC2 = input("What number is M2R1: C2: ")
					M2R1twoxthreeC3 = input("What number is M2R1: C3: ")
					M2R2twoxthreeC1 = input("What number is M2R2: C1: ")
					M2R2twoxthreeC2 = input("What number is M2R2: C2: ")
					M2R2twoxthreeC3 = input("What number is M2R2: C3: ")
				if Matrix2_size == "3x2":
					M2R1threextwoC1 = input("What number is M2R1: C1: ")
					M2R1threextwoC2 = input("What number is M2R1: C2: ")
					M2R2threextwoC1 = input("What number is M2R2: C1: ")
					M2R2threextwoC2 = input("What number is M2R2: C2: ")
					M2R3threextwoC1 = input("What number is M2R2: C1: ")
					M2R3threextwoC2 = input("What number is M2R2: C2: ")
				if Matrix2_size == "3x3":
					M2R1threexthreeC1 = input("What number is M2R1: C1: ")
					M2R1threexthreeC2 = input("What number is M2R1: C2: ")
					M2R1threexthreeC3 = input("What number is M2R1: C3: ")
					M2R2threexthreeC1 = input("What number is M2R2: C1: ")
					M2R2threexthreeC2 = input("What number is M2R2: C2: ")
					M2R2threexthreeC3 = input("What number is M2R2: C3: ")
					M2R3threexthreeC1 = input("What number is M2R3: C1: ")
					M2R3threexthreeC2 = input("What number is M2R3: C2: ")
					M2R3threexthreeC3 = input("What number is M2R3: C3: ")
				if Matrix2_size == "4x1":
					M2R1fourxoneC1 = input("What number is M2R1: C1: ")
					M2R2fourxoneC1 = input("What number is M2R2: C1: ")
					M2R3fourxoneC1 = input("What number is M2R3: C1: ")
					M2R4fourxoneC1 = input("What number is M2R4: C1: ")
				if Matrix2_size == "4x2":
					M2R1fourxtwoC1 = input("What number is M2R1: C1: ")
					M2R1fourxtwoC2 = input("What number is M2R1: C2: ")
					M2R2fourxtwoC1 = input("What number is M2R2: C1: ")
					M2R2fourxtwoC2 = input("What number is M2R2: C2: ")
					M2R3fourxtwoC1 = input("What number is M2R3: C1: ")
					M2R3fourxtwoC2 = input("What number is M2R3: C2: ")
					M2R4fourxtwoC1 = input("What number is M2R4: C1: ")
					M2R4fourxtwoC2 = input("What number is M2R4: C2: ")
				if Matrix2_size == "4x3":
					M2R1fourxthreeC1 = input("What number is M2R1: C1: ")
					M2R1fourxthreeC2 = input("What number is M2R1: C2: ")
					M2R1fourxthreeC3 = input("What number is M2R1: C3: ")
					M2R2fourxthreeC1 = input("What number is M2R2: C1: ")
					M2R2fourxthreeC2 = input("What number is M2R2: C2: ")
					M2R2fourxthreeC3 = input("What number is M2R2: C3: ")
					M2R3fourxthreeC1 = input("What number is M2R3: C1: ")
					M2R3fourxthreeC2 = input("What number is M2R3: C2: ")
					M2R3fourxthreeC3 = input("What number is M2R3: C3: ")
					M2R4fourxthreeC1 = input("What number is M2R4: C1: ")
					M2R4fourxthreeC2 = input("What number is M2R4: C2: ")
					M2R4fourxthreeC3 = input("What number is M2R4: C3: ")
				if Matrix2_size == "4x4":
					M2R1fourxfourC1 = input("What number is M2R1: C1: ")
					M2R1fourxfourC2 = input("What number is M2R1: C2: ")
					M2R1fourxfourC3 = input("What number is M2R1: C3: ")
					M2R1fourxfourC4 = input("What number is M2R1: C4: ")
					M2R2fourxfourC1 = input("What number is M2R2: C1: ")
					M2R2fourxfourC2 = input("What number is M2R2: C2: ")
					M2R2fourxfourC3 = input("What number is M2R2: C3: ")
					M2R2fourxfourC4 = input("What number is M2R2: C4: ")
					M2R3fourxfourC1 = input("What number is M2R3: C1: ")
					M2R3fourxfourC2 = input("What number is M2R3: C2: ")
					M2R3fourxfourC3 = input("What number is M2R3: C3: ")
					M2R3fourxfourC4 = input("What number is M2R3: C4: ")
					M2R4fourxfourC1 = input("What number is M2R4: C1: ")
					M2R4fourxfourC2 = input("What number is M2R4: C2: ")
					M2R4fourxfourC3 = input("What number is M2R4: C3: ")
					M2R4fourxfourC4 = input("What number is M2R4: C4: ")
				if Matrix2_size == "1x4":
					M2R1onexfourC1 = input("What number is M2R1: C1: ")
					M2R1onexfourC2 = input("What number is M2R1: C2: ")
					M2R1onexfourC3 = input("What number is M2R1: C3: ")
					M2R1onexfourC4 = input("What number is M2R1: C4: ")	
				if Matrix2_size == "2x4":
					M2R1twoxfourC1 = input("What number is M2R1: C1: ")
					M2R1twoxfourC2 = input("What number is M2R1: C2: ")
					M2R1twoxfourC3 = input("What number is M2R1: C3: ")
					M2R1twoxfourC4 = input("What number is M2R1: C4: ")
					M2R2twoxfourC1 = input("What number is M2R2: C1: ")
					M2R2twoxfourC2 = input("What number is M2R2: C2: ")
					M2R2twoxfourC3 = input("What number is M2R2: C3: ")
					M2R2twoxfourC4 = input("What number is M2R2: C4: ")
				if Matrix2_size == "3x4":
					M2R1threexfourC1 = input("What number is M2R1: C1: ")
					M2R1threexfourC2 = input("What number is M2R1: C2: ")
					M2R1threexfourC3 = input("What number is M2R1: C3: ")
					M2R1threexfourC4 = input("What number is M2R1: C4: ")
					M2R2threexfourC1 = input("What number is M2R2: C1: ")
					M2R2threexfourC2 = input("What number is M2R2: C2: ")
					M2R2threexfourC3 = input("What number is M2R2: C3: ")
					M2R2threexfourC4 = input("What number is M2R2: C4: ")								
					M2R3threexfourC1 = input("What number is M2R3: C1: ")
					M2R3threexfourC2 = input("What number is M2R3: C2: ")
					M2R3threexfourC3 = input("What number is M2R3: C3: ")
					M2R3threexfourC4 = input("What number is M2R3: C4: ")
				matrix_Action = input("Do you want to Add M1+M2(A), Subtract M1-M2(S), or Multiply M1*M2(M): ").lower()
				print("")
				if matrix_Action == "a":
	#Addition
					continuem = input("Adding Selected, press (enter) to continue.")
					if Matrix1_size == "1x1":
						if Matrix2_size == "1x1":
							FA = int(M1R1onexoneC1)+int(M2R1onexoneC1)
							print("")
							print("["+str(FA)+"]")
						else:
							print("")
							print("")
							print("Matrices have to be the same size to add")
					if Matrix1_size == "2x1":
						if Matrix2_size == "2x1":
							FAR1 = int(M1R1twoxoneC1)+int(M2R1twoxoneC1)
							FAR2 = int(M1R2twoxoneC1)+int(M2R2twoxoneC1)
							print("")
							print("["+str(FAR1)+"]")
							print("["+str(FAR2)+"]")
						else:
							print("")
							print("")
							print("Matrices have to be the same size to add")						
					if Matrix1_size == "3x1":
						if Matrix2_size == "3x1":
							FAR1 = int(M1R1threexoneC1)+int(M2R1threexoneC1)
							FAR2 = int(M1R2threexoneC1)+int(M2R2threexoneC1)
							FAR3 = int(M1R3threexoneC1)+int(M2R3threexoneC1)
							print("")
							print("["+str(FAR1)+"]")
							print("["+str(FAR2)+"]")		
							print("["+str(FAR3)+"]")
					if Matrix1_size == "1x2":
						if Matrix2_size == "1x2":
							FAR1C1 = int(M1R1onextwoC1)+int(M2R1onextwoC1)
							FAR1C2 = int(M1R1onextwoC2)+int(M1R1onextwoC2)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+"]")
					if Matrix1_size == "2x2":
						if Matrix2_size == "2x2":
							FARC1 = int(M1R1twoxtwoC1)+int(M2R1twoxtwoC1)
							FARC2 = int(M1R1twoxtwoC2)+int(M2R1twoxtwoC2)
							FAR2C1 = int(M1R2twoxtwoC1)+int(M2R2twoxtwoC1)
							FAR2C2 = int(M1R2twoxtwoC2)+int(M2R2twoxtwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+"]")
					if Matrix1_size == "3x2":
						if Matrix2_size == "3x2":
							FARC1 = int(M1R1threextwoC1)+int(M2R1threextwoC1)
							FARC2 = int(M1R1threextwoC2)+int(M2R1threextwoC2)
							FAR2C1 = int(M1R2threextwoC1)+int(M2R2threextwoC1)
							FAR2C2 = int(M1R2threextwoC2)+int(M2R2threextwoC2)
							FAR3C1 = int(M1R3threextwoC1)+int(M2R3threextwoC1)
							FAR3C2 = int(M1R3threextwoC2)+int(M2R3threextwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+"]")
					if Matrix1_size == "1x3":
						if Matrix2_size == "1x3":
							FARC1 = int(M1R1onexthreeC1)+int(M2R1onexthreeC1)
							FARC2 = int(M1R1onexthreeC2)+int(M2R1onexthreeC2)
							FARC3 = int(M1R1onexthreeC3)+int(M2R1onexthreeC3)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
					if Matrix1_size == "2x3":
						if Matrix2_size == "2x3":
							FARC1 = int(M1R1twoxthreeC1)+int(M2R1twoxthreeC1)
							FARC2 = int(M1R1twoxthreeC2)+int(M2R1twoxthreeC2)
							FARC3 = int(M1R1twoxthreeC3)+int(M2R1twoxthreeC3)
							FAR2C1 = int(M1R2twoxthreeC1)+int(M2R2twoxthreeC1)
							FAR2C2 = int(M1R2twoxthreeC2)+int(M2R2twoxthreeC2)
							FAR2C3 = int(M1R2twoxthreeC3)+int(M2R2twoxthreeC3)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+"]")					
					if Matrix1_size == "3x3":
						if Matrix2_size == "3x3":
							FARC1 = int(M1R1threexthreeC1)+int(M2R1threexthreeC1)
							FARC2 = int(M1R1threexthreeC2)+int(M2R1threexthreeC2)
							FARC3 = int(M1R1threexthreeC3)+int(M2R1threexthreeC3)
							FAR2C1 = int(M1R2threexthreeC1)+int(M2R2threexthreeC1)
							FAR2C2 = int(M1R2threexthreeC2)+int(M2R2threexthreeC2)
							FAR2C3 = int(M1R2threexthreeC3)+int(M2R2threexthreeC3)
							FAR3C1 = int(M1R3threexthreeC1)+int(M2R3threexthreeC1)
							FAR3C2 = int(M1R3threexthreeC2)+int(M2R3threexthreeC2)
							FAR3C3 = int(M1R3threexthreeC3)+int(M2R3threexthreeC3)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+"]")	
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+"]")
					if Matrix1_size == "4x1":
						if Matrix2_size == "4x1":
							FARC1 = int(M1R1fourxoneC1)+int(M2R1fourxoneC1)
							FARC2 = int(M1R2fourxoneC1)+int(M2R2fourxoneC1)
							FARC3 = int(M1R3fourxoneC1)+int(M2R3fourxoneC1)
							FARC4 = int(M1R4fourxoneC1)+int(M2R4fourxoneC1)
							print("")
							print("["+str(FARC1)+"]")
							print("["+str(FARC2)+"]")
							print("["+str(FARC3)+"]")
							print("["+str(FARC4)+"]")
					if Matrix1_size == "4x2":
						if Matrix2_size == "4x2":
							FARC1 = int(M1R1fourxtwoC1)+int(M2R1fourxtwoC1)
							FARC2 = int(M1R2fourxtwoC1)+int(M2R2fourxtwoC1)
							FARC3 = int(M1R3fourxtwoC1)+int(M2R3fourxtwoC1)
							FARC4 = int(M1R4fourxtwoC1)+int(M2R4fourxtwoC1)
							FARC5 = int(M1R1fourxtwoC2)+int(M2R1fourxtwoC2)
							FARC6 = int(M1R2fourxtwoC2)+int(M2R2fourxtwoC2)
							FARC7 = int(M1R3fourxtwoC2)+int(M2R3fourxtwoC2)
							FARC8 = int(M1R4fourxtwoC2)+int(M2R4fourxtwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC5)+"]")
							print("["+str(FARC2)+" "+str(FARC6)+"]")
							print("["+str(FARC3)+" "+str(FARC7)+"]")
							print("["+str(FARC4)+" "+str(FARC8)+"]")
					if Matrix1_size == "4x3":
						if Matrix2_size == "4x3":
							FAR1C1 = int(M1R1fourxthreeC1)+int(M2R1fourxthreeC1)
							FAR1C2 = int(M1R1fourxthreeC2)+int(M2R1fourxthreeC2)
							FAR1C3 = int(M1R1fourxthreeC3)+int(M2R1fourxthreeC3)
							FAR2C4 = int(M1R2fourxthreeC1)+int(M2R2fourxthreeC1)
							FAR2C5 = int(M1R2fourxthreeC2)+int(M2R2fourxthreeC2)
							FAR2C6 = int(M1R2fourxthreeC3)+int(M2R2fourxthreeC3)
							FAR3C7 = int(M1R3fourxthreeC1)+int(M2R3fourxthreeC1)
							FAR3C8 = int(M1R3fourxthreeC2)+int(M2R3fourxthreeC2)
							FAR3C9 = int(M1R3fourxthreeC3)+int(M2R3fourxthreeC3)
							FAR4C1 = int(M1R4fourxthreeC1)+int(M2R4fourxthreeC1)
							FAR4C2 = int(M1R4fourxthreeC2)+int(M2R4fourxthreeC2)
							FAR4C3 = int(M1R4fourxthreeC3)+int(M2R4fourxthreeC3)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+"]")
							print("["+str(FAR2C4)+" "+str(FAR2C5)+" "+str(FAR2C6)+"]")
							print("["+str(FAR3C7)+" "+str(FAR3C8)+" "+str(FAR3C9)+"]")
							print("["+str(FAR4C1)+" "+str(FAR4C2)+" "+str(FAR4C3)+"]")							
					if Matrix1_size == "1x4":
						if Matrix2_size == "1x4":
							FAR1C1 = int(M1R1onexfourC1)+int(M2R1onexfourC1)
							FAR1C2 = int(M1R1onexfourC2)+int(M2R1onexfourC2)
							FAR1C3 = int(M1R1onexfourC3)+int(M2R1onexfourC3)
							FAR1C4 = int(M1R1onexfourC4)+int(M2R1onexfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
					if Matrix1_size == "2x4":
						if Matrix2_size == "2x4":
							FAR1C1 = int(M1R1twoxfourC1)+int(M2R1twoxfourC1)
							FAR1C2 = int(M1R1twoxfourC2)+int(M2R1twoxfourC2)
							FAR1C3 = int(M1R1twoxfourC3)+int(M2R1twoxfourC3)
							FAR1C4 = int(M1R1twoxfourC4)+int(M2R1twoxfourC4)
							FAR2C1 = int(M1R2twoxfourC1)+int(M2R2twoxfourC1)
							FAR2C2 = int(M1R2twoxfourC2)+int(M2R2twoxfourC2)
							FAR2C3 = int(M1R2twoxfourC3)+int(M2R2twoxfourC3)
							FAR2C4 = int(M1R2twoxfourC4)+int(M2R2twoxfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2C4)+"]")
					if Matrix1_size == "3x4":
						if Matrix2_size == "3x4":
							FAR1C1 = int(M1R1threexfourC1)+int(M2R1threexfourC1)
							FAR1C2 = int(M1R1threexfourC2)+int(M2R1threexfourC2)
							FAR1C3 = int(M1R1threexfourC3)+int(M2R1threexfourC3)
							FAR1C4 = int(M1R1threexfourC4)+int(M2R1threexfourC4)
							FAR2C1 = int(M1R2threexfourC1)+int(M2R2threexfourC1)
							FAR2C2 = int(M1R2threexfourC2)+int(M2R2threexfourC2)
							FAR2C3 = int(M1R2threexfourC3)+int(M2R2threexfourC3)
							FAR2C4 = int(M1R2threexfourC4)+int(M2R2threexfourC4)
							FAR3C1 = int(M1R3threexfourC1)+int(M2R3threexfourC1)
							FAR3C2 = int(M1R3threexfourC2)+int(M2R3threexfourC2)
							FAR3C3 = int(M1R3threexfourC3)+int(M2R3threexfourC3)
							FAR3C4 = int(M1R3threexfourC4)+int(M2R3threexfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2C4)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+" "+str(FAR3C4)+"]")
					if Matrix1_size == "4x4":
						if Matrix2_size == "4x4":
							FAR1C1 = int(M1R1fourxfourC1)+int(M2R1fourxfourC1)
							FAR1C2 = int(M1R1fourxfourC2)+int(M2R1fourxfourC2)
							FAR1C3 = int(M1R1fourxfourC3)+int(M2R1fourxfourC3)
							FAR1C4 = int(M1R1fourxfourC4)+int(M2R1fourxfourC4)
							FAR2C1 = int(M1R2fourxfourC1)+int(M2R2fourxfourC1)
							FAR2C2 = int(M1R2fourxfourC2)+int(M2R2fourxfourC2)
							FAR2C3 = int(M1R2fourxfourC3)+int(M2R2fourxfourC3)
							FAR2C4 = int(M1R2fourxfourC4)+int(M2R2fourxfourC4)
							FAR3C1 = int(M1R3fourxfourC1)+int(M2R3fourxfourC1)
							FAR3C2 = int(M1R3fourxfourC2)+int(M2R3fourxfourC2)
							FAR3C3 = int(M1R3fourxfourC3)+int(M2R3fourxfourC3)
							FAR3C4 = int(M1R3fourxfourC4)+int(M2R3fourxfourC4)
							FAR4C1 = int(M1R4fourxfourC1)+int(M2R4fourxfourC1)
							FAR4C2 = int(M1R4fourxfourC2)+int(M2R4fourxfourC2)
							FAR4C3 = int(M1R4fourxfourC3)+int(M2R4fourxfourC3)
							FAR4C4 = int(M1R4fourxfourC4)+int(M2R4fourxfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2C4)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+" "+str(FAR3C4)+"]")
							print("["+str(FAR4C1)+" "+str(FAR4C2)+" "+str(FAR4C3)+" "+str(FAR4C4)+"]")
					print("")
					print("")
					maAgain = input("Again? Y or N: ").lower()
					if maAgain == "y":
						print("")
						print("")
						print("")
						a = True
					if maAgain == "n":
						a = False
						sys.exit()
	#Subtraction													
				if matrix_Action == "s":
					continuem = input("Subtract Selected, press (enter) to continue.")
					if Matrix1_size == "1x1":
						if Matrix2_size == "1x1":
							FA = int(M1R1onexoneC1)-int(M2R1onexoneC1)
							print("")
							print("["+str(FA)+"]")
						else:
							print("")
							print("")
							print("Matrices have to be the same size to add")
					if Matrix1_size == "2x1":
						if Matrix2_size == "2x1":
							FAR1 = int(M1R1twoxoneC1)-int(M2R1twoxoneC1)
							FAR2 = int(M1R2twoxoneC1)-int(M2R2twoxoneC1)
							print("")
							print("["+str(FAR1)+"]")
							print("["+str(FAR2)+"]")
						else:
							print("")
							print("")
							print("Matrices have to be the same size to add")						
					if Matrix1_size == "3x1":
						if Matrix2_size == "3x1":
							FAR1 = int(M1R1threexoneC1)-int(M2R1threexoneC1)
							FAR2 = int(M1R2threexoneC1)-int(M2R2threexoneC1)
							FAR3 = int(M1R3threexoneC1)-int(M2R3threexoneC1)
							print("")
							print("["+str(FAR1)+"]")
							print("["+str(FAR2)+"]")		
							print("["+str(FAR3)+"]")
					if Matrix1_size == "1x2":
						if Matrix2_size == "1x2":
							FAR1C1 = int(M1R1onextwoC1)-int(M2R1onextwoC1)
							FAR1C2 = int(M1R1onextwoC2)-int(M2R1onextwoC2)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+"]")
					if Matrix1_size == "2x2":
						if Matrix2_size == "2x2":
							FARC1 = int(M1R1twoxtwoC1)-int(M2R1twoxtwoC1)
							FARC2 = int(M1R1twoxtwoC2)-int(M2R1twoxtwoC2)
							FAR2C1 = int(M1R2twoxtwoC1)-int(M2R2twoxtwoC1)
							FAR2C2 = int(M1R2twoxtwoC2)-int(M2R2twoxtwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+"]")
					if Matrix1_size == "3x2":
						if Matrix2_size == "3x2":
							FARC1 = int(M1R1threextwoC1)-int(M2R1threextwoC1)
							FARC2 = int(M1R1threextwoC2)-int(M2R1threextwoC2)
							FAR2C1 = int(M1R2threextwoC1)-int(M2R2threextwoC1)
							FAR2C2 = int(M1R2threextwoC2)-int(M2R2threextwoC2)
							FAR3C1 = int(M1R3threextwoC1)-int(M2R3threextwoC1)
							FAR3C2 = int(M1R3threextwoC2)-int(M2R3threextwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+"]")
					if Matrix1_size == "1x3":
						if Matrix2_size == "1x3":
							FARC1 = int(M1R1onexthreeC1)-int(M2R1onexthreeC1)
							FARC2 = int(M1R1onexthreeC2)-int(M2R1onexthreeC2)
							FARC3 = int(M1R1onexthreeC3)-int(M2R1onexthreeC3)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
					if Matrix1_size == "2x3":
						if Matrix2_size == "2x3":
							FARC1 = int(M1R1twoxthreeC1)-int(M2R1twoxthreeC1)
							FARC2 = int(M1R1twoxthreeC2)-int(M2R1twoxthreeC2)
							FARC3 = int(M1R1twoxthreeC3)-int(M2R1twoxthreeC3)
							FAR2C1 = int(M1R2twoxthreeC1)-int(M2R2twoxthreeC1)
							FAR2C2 = int(M1R2twoxthreeC2)-int(M2R2twoxthreeC2)
							FAR2C3 = int(M1R2twoxthreeC3)-int(M2R2twoxthreeC3)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+"]")					
					if Matrix1_size == "3x3":
						if Matrix2_size == "3x3":
							FARC1 = int(M1R1threexthreeC1)-int(M2R1threexthreeC1)
							FARC2 = int(M1R1threexthreeC2)-int(M2R1threexthreeC2)
							FARC3 = int(M1R1threexthreeC3)-int(M2R1threexthreeC3)
							FAR2C1 = int(M1R2threexthreeC1)-int(M2R2threexthreeC1)
							FAR2C2 = int(M1R2threexthreeC2)-int(M2R2threexthreeC2)
							FAR2C3 = int(M1R2threexthreeC3)-int(M2R2threexthreeC3)
							FAR3C1 = int(M1R3threexthreeC1)-int(M2R3threexthreeC1)
							FAR3C2 = int(M1R3threexthreeC2)-int(M2R3x2threexthreeC2)
							FAR3C3 = int(M1R3threexthreeC3)-int(M2R3threexthreeC3)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+"]")	
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+"]")	
							
							
					if Matrix1_size == "4x1":
						if Matrix2_size == "4x1":
							FARC1 = int(M1R1fourxoneC1)-int(M2R1fourxoneC1)
							FARC2 = int(M1R2fourxoneC1)-int(M2R2fourxoneC1)
							FARC3 = int(M1R3fourxoneC1)-int(M2R3fourxoneC1)
							FARC4 = int(M1R4fourxoneC1)-int(M2R4fourxoneC1)
							print("")
							print("["+str(FARC1)+"]")
							print("["+str(FARC2)+"]")
							print("["+str(FARC3)+"]")
							print("["+str(FARC4)+"]")
					if Matrix1_size == "4x2":
						if Matrix2_size == "4x2":
							FARC1 = int(M1R1fourxtwoC1)-int(M2R1fourxtwoC1)
							FARC2 = int(M1R2fourxtwoC1)-int(M2R2fourxtwoC1)
							FARC3 = int(M1R3fourxtwoC1)-int(M2R3fourxtwoC1)
							FARC4 = int(M1R4fourxtwoC1)-int(M2R4fourxtwoC1)
							FARC5 = int(M1R1fourxtwoC2)-int(M2R1fourxtwoC2)
							FARC6 = int(M1R2fourxtwoC2)-int(M2R2fourxtwoC2)
							FARC7 = int(M1R3fourxtwoC2)-int(M2R3fourxtwoC2)
							FARC8 = int(M1R4fourxtwoC2)-int(M2R4fourxtwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC5)+"]")
							print("["+str(FARC2)+" "+str(FARC6)+"]")
							print("["+str(FARC3)+" "+str(FARC7)+"]")
							print("["+str(FARC4)+" "+str(FARC8)+"]")
					if Matrix1_size == "4x3":
						if Matrix2_size == "4x3":
							FAR1C1 = int(M1R1fourxthreeC1)-int(M2R1fourxthreeC1)
							FAR1C2 = int(M1R1fourxthreeC2)-int(M2R1fourxthreeC2)
							FAR1C3 = int(M1R1fourxthreeC3)-int(M2R1fourxthreeC3)
							FAR2C4 = int(M1R2fourxthreeC1)-int(M2R2fourxthreeC1)
							FAR2C5 = int(M1R2fourxthreeC2)-int(M2R2fourxthreeC2)
							FAR2C6 = int(M1R2fourxthreeC3)-int(M2R2fourxthreeC3)
							FAR3C7 = int(M1R3fourxthreeC1)-int(M2R3fourxthreeC1)
							FAR3C8 = int(M1R3fourxthreeC2)-int(M2R3fourxthreeC2)
							FAR3C9 = int(M1R3fourxthreeC3)-int(M2R3fourxthreeC3)
							FAR4C1 = int(M1R4fourxthreeC1)-int(M2R4fourxthreeC1)
							FAR4C2 = int(M1R4fourxthreeC2)-int(M2R4fourxthreeC2)
							FAR4C3 = int(M1R4fourxthreeC3)-int(M2R4fourxthreeC3)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+"]")
							print("["+str(FAR2C4)+" "+str(FAR2C5)+" "+str(FAR2C6)+"]")
							print("["+str(FAR3C7)+" "+str(FAR3C8)+" "+str(FAR3C9)+"]")
							print("["+str(FAR4C1)+" "+str(FAR4C2)+" "+str(FAR4C3)+"]")							
					if Matrix1_size == "1x4":
						if Matrix2_size == "1x4":
							FAR1C1 = int(M1R1onexfourC1)-int(M2R1onexfourC1)
							FAR1C2 = int(M1R1onexfourC2)-int(M2R1onexfourC2)
							FAR1C3 = int(M1R1onexfourC3)-int(M2R1onexfourC3)
							FAR1C4 = int(M1R1onexfourC4)-int(M2R1onexfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
					if Matrix1_size == "2x4":
						if Matrix2_size == "2x4":
							FAR1C1 = int(M1R1twoxfourC1)-int(M2R1twoxfourC1)
							FAR1C2 = int(M1R1twoxfourC2)-int(M2R1twoxfourC2)
							FAR1C3 = int(M1R1twoxfourC3)-int(M2R1twoxfourC3)
							FAR1C4 = int(M1R1twoxfourC4)-int(M2R1twoxfourC4)
							FAR2C1 = int(M1R2twoxfourC1)-int(M2R2twoxfourC1)
							FAR2C2 = int(M1R2twoxfourC2)-int(M2R2twoxfourC2)
							FAR2C3 = int(M1R2twoxfourC3)-int(M2R2twoxfourC3)
							FAR2C4 = int(M1R2twoxfourC4)-int(M2R2twoxfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2C4)+"]")
					if Matrix1_size == "3x4":
						if Matrix2_size == "3x4":
							FAR1C1 = int(M1R1threexfourC1)-int(M2R1threexfourC1)
							FAR1C2 = int(M1R1threexfourC2)-int(M2R1threexfourC2)
							FAR1C3 = int(M1R1threexfourC3)-int(M2R1threexfourC3)
							FAR1C4 = int(M1R1threexfourC4)-int(M2R1threexfourC4)
							FAR2C1 = int(M1R2threexfourC1)-int(M2R2threexfourC1)
							FAR2C2 = int(M1R2threexfourC2)-int(M2R2threexfourC2)
							FAR2C3 = int(M1R2threexfourC3)-int(M2R2threexfourC3)
							FAR2C4 = int(M1R2threexfourC4)-int(M2R2threexfourC4)
							FAR3C1 = int(M1R3threexfourC1)-int(M2R3threexfourC1)
							FAR3C2 = int(M1R3threexfourC2)-int(M2R3threexfourC2)
							FAR3C3 = int(M1R3threexfourC3)-int(M2R3threexfourC3)
							FAR3C4 = int(M1R3threexfourC4)-int(M2R3threexfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2C4)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+" "+str(FAR3C4)+"]")
					if Matrix1_size == "4x4":
						if Matrix2_size == "4x4":
							FAR1C1 = int(M1R1fourxfourC1)-int(M2R1fourxfourC1)
							FAR1C2 = int(M1R1fourxfourC2)-int(M2R1fourxfourC2)
							FAR1C3 = int(M1R1fourxfourC3)-int(M2R1fourxfourC3)
							FAR1C4 = int(M1R1fourxfourC4)-int(M2R1fourxfourC4)
							FAR2C1 = int(M1R2fourxfourC1)-int(M2R2fourxfourC1)
							FAR2C2 = int(M1R2fourxfourC2)-int(M2R2fourxfourC2)
							FAR2C3 = int(M1R2fourxfourC3)-int(M2R2fourxfourC3)
							FAR2C4 = int(M1R2fourxfourC4)-int(M2R2fourxfourC4)
							FAR3C1 = int(M1R3fourxfourC1)-int(M2R3fourxfourC1)
							FAR3C2 = int(M1R3fourxfourC2)-int(M2R3fourxfourC2)
							FAR3C3 = int(M1R3fourxfourC3)-int(M2R3fourxfourC3)
							FAR3C4 = int(M1R3fourxfourC4)-int(M2R3fourxfourC4)
							FAR4C1 = int(M1R4fourxfourC1)-int(M2R4fourxfourC1)
							FAR4C2 = int(M1R4fourxfourC2)-int(M2R4fourxfourC2)
							FAR4C3 = int(M1R4fourxfourC3)-int(M2R4fourxfourC3)
							FAR4C4 = int(M1R4fourxfourC4)-int(M2R4fourxfourC4)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+" "+str(FAR1C3)+" "+str(FAR1C4)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2C4)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+" "+str(FAR3C4)+"]")
							print("["+str(FAR4C1)+" "+str(FAR4C2)+" "+str(FAR4C3)+" "+str(FAR4C4)+"]")							
					print("")
					print("")
					maAgain = input("Again? Y or N: ").lower()
					if maAgain == "y":
						print("")
						print("")
						print("")
						a = True
					if maAgain == "n":
						a = False
						sys.exit()
#Multiplication			
				if matrix_Action == "m":
					continuem = input("Multiplication Selected, press (enter) to continue.")
					if Matrix1_size == "1x1":
						if Matrix2_size == "1x1":
							FARC = int(M1R1onexoneC1)*int(M2R1onexoneC1)
							print("")
							print("["+str(FARC)+"]")
						if Matrix2_size == "1x2":
							FARCE1 = int(M1R1onexoneC1)*int(M2R1onextwoC1)
							FARC2E1 = int(M1R1onexoneC1)*int(M2R1onextwoC2)
							print("")
							print("["+str(FARCE1)+" "+str(FARC2E1)+"]")
						if Matrix2_size == "1x3":
							FARCE1 = int(M1R1onexoneC1)*int(M2R1onexthreeC1)
							FARC2E1 = int(M1R1onexoneC1)*int(M2R1onexthreeC2)
							FARC3E2 = int(M1R1onexoneC1)*int(M2R1onexthreeC3)
							print("")
							print("["+str(FARCE1)+" "+str(FARC2E1)+" "+str(FARC3E2)+"]")
						if Matrix2_size == "1x4":
							FARC1 = int(M1R1onexoneC1)*int(M2R1onexfourC1)
							FARC2 = int(M1R1onexoneC1)*int(M2R1onexfourC2)
							FARC3 = int(M1R1onexoneC1)*int(M2R1onexfourC3)
							FARC4 = int(M1R1onexoneC1)*int(M2R1onexfourC4)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+" "+str(FARC4)+"]")
					if Matrix1_size == "1x2":
						if Matrix2_size == "2x1":
							FAE1 = int(M1R1onextwoC1)*int(M2R1twoxoneC1)
							FAE2 = int(M1R1onextwoC2)*int(M2R2twoxoneC1)
							FET = int(FAE1)+int(FAE2)
							print("")
							print("["+str(FET)+"]")
						if Matrix2_size == "2x2":
							FARC1 = int(M1R1onextwoC1)*int(M2R1twoxtwoC1)
							FARC2 = int(M1R1onextwoC2)*int(M2R2twoxtwoC1)
							FAR2C1 = int(M1R1onextwoC1)*int(M2R1twoxtwoC2)
							FAR2C2 = int(M1R1onextwoC2)*int(M2R2twoxtwoC2)
							FAR1C1 = int(FARC1)+int(FARC2)
							FAR1C2 = int(FAR2C1)+int(FAR2C2)
							print("")
							print("["+str(FAR1C1)+" "+str(FAR1C2)+"]")
						if Matrix2_size == "2x3":
							FARC1 = int(M1R1onextwoC1)*int(M2R1twoxthreeC1)
							FARC2 = int(M1R1onextwoC2)*int(M2R2twoxthreeC1)
							FAR2C2 = int(M1R1onextwoC1)*int(M2R1twoxthreeC2)
							FAR2C3 = int(M1R1onextwoC2)*int(M2R2twoxthreeC2)
							FAR3C3 = int(M1R1onextwoC1)*int(M2R1twoxthreeC3)
							FAR3C4 = int(M1R1onextwoC2)*int(M2R2twoxthreeC3)
							FAE1C1 = int(FARC1) + int(FARC2)
							FAE2C2 = int(FAR2C2) + int(FAR2C3)
							FAE3C3 = int(FAR3C3) + int(FAR3C4)
							print("")
							print("["+str(FAE1C1) +" "+ str(FAE2C2) +" "+ str(FAE3C3)+"]")
						if Matrix2_size == "2x4":
							FARC1 = int(M1R1onextwoC1)*int(M2R1twoxfourC1)
							FARC2 = int(M1R1onextwoC2)*int(M2R2twoxfourC1)
							FAR2C2 = int(M1R1onextwoC1)*int(M2R1twoxfourC2)
							FAR2C3 = int(M1R1onextwoC2)*int(M2R2twoxfourC2)
							FAR3C3 = int(M1R1onextwoC1)*int(M2R1twoxfourC3)
							FAR3C4 = int(M1R1onextwoC2)*int(M2R2twoxfourC3)
							FAR4C3 = int(M1R1onextwoC1)*int(M2R1twoxfourC4)
							FAR4C4 = int(M1R1onextwoC2)*int(M2R2twoxfourC4)
							FAE1C1 = int(FARC1) + int(FARC2)
							FAE2C2 = int(FAR2C2) + int(FAR2C3)
							FAE3C3 = int(FAR3C3) + int(FAR3C4)
							FAE4C4 = int(FAR4C3) + int(FAR4C4)
							print("")
							print("["+str(FAE1C1)+" "+str(FAE2C2)+" "+str(FAE3C3)+" "+str(FAE4C4)+"]")
					if Matrix1_size == "1x3":
						if Matrix2_size == "3x1":
							FARC1 = int(M1R1onexthreeC1)*int(M2R1threexoneC1)
							FAR2C1 = int(M1R1onexthreeC2)*int(M2R2threexoneC1)
							FAR3C1 = int(M1R1onexthreeC3)*int(M2R3threexoneC1)
							FAE = int(FARC1)+int(FAR2C1)+int(FAR3C1)
							print("")
							print("["+str(FAE)+"]")
						if Matrix2_size == "3x2":
							FARC1 = int(M1R1onexthreeC1)*int(M2R1threextwoC1)
							FARC2 = int(M1R1onexthreeC2)*int(M2R2threextwoC1)
							FARC3 = int(M1R1onexthreeC3)*int(M2R3threextwoC1)
							FAR2C1 = int(M1R1onexthreeC1)*int(M2R1threextwoC2)
							FAR2C2 = int(M1R1onexthreeC2)*int(M2R2threextwoC2)
							FAR2C3 = int(M1R1onexthreeC3)*int(M2R3threextwoC2)
							FAE1 = int(FARC1)+int(FARC2)+int(FARC3)
							FAE2 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)
							print("")
							print("["+str(FAE1)+" "+str(FAE2)+"]")
						if Matrix2_size == "3x3":
							FARC1 = int(M1R1onexthreeC1)*int(M2R1threexthreeC1)
							FARC2 = int(M1R1onexthreeC2)*int(M2R2threexthreeC1)
							FARC3 = int(M1R1onexthreeC3)*int(M2R3threexthreeC1)
							FAR2C1 = int(M1R1onexthreeC1)*int(M2R1threexthreeC2)
							FAR2C2 = int(M1R1onexthreeC2)*int(M2R2threexthreeC2)
							FAR2C3 = int(M1R1onexthreeC3)*int(M2R3threexthreeC2)
							FAR3C1 = int(M1R1onexthreeC1)*int(M2R1threexthreeC3)
							FAR3C2 = int(M1R1onexthreeC2)*int(M2R2threexthreeC3)
							FAR3C3 = int(M1R1onexthreeC3)*int(M2R3threexthreeC3)
							FAE1 = int(FARC1)+int(FARC2)+int(FARC3)
							FAE2 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)
							FAE3 = int(FAR3C1)+int(FAR3C2)+int(FAR3C3)
							print("")
							print("["+str(FAE1)+" "+str(FAE2)+" "+str(FAE3)+"]")
						
						if Matrix2_size == "3x4":
							FARC1 = int(M1R1onexthreeC1)*int(M2R1threexfourC1)
							FARC2 = int(M1R1onexthreeC2)*int(M2R2threexfourC1)
							FARC3 = int(M1R1onexthreeC3)*int(M2R3threexfourC1)
							FAR2C1 = int(M1R1onexthreeC1)*int(M2R1threexfourC2)
							FAR2C2 = int(M1R1onexthreeC2)*int(M2R2threexfourC2)
							FAR2C3 = int(M1R1onexthreeC3)*int(M2R3threexfourC2)
							FAR3C1 = int(M1R1onexthreeC1)*int(M2R1threexfourC3)
							FAR3C2 = int(M1R1onexthreeC2)*int(M2R2threexfourC3)
							FAR3C3 = int(M1R1onexthreeC3)*int(M2R3threexfourC3)
							FAR4C1 = int(M1R1onexthreeC1)*int(M2R1threexfourC4)
							FAR4C2 = int(M1R1onexthreeC2)*int(M2R2threexfourC4)
							FAR4C3 = int(M1R1onexthreeC3)*int(M2R3threexfourC4)
							FAE1 = int(FARC1)+int(FARC2)+int(FARC3)
							FAE2 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)
							FAE3 = int(FAR3C1)+int(FAR3C2)+int(FAR3C3)
							FAE4 = int(FAR4C1)+int(FAR4C2)+int(FAR4C3)
							print("")
							print("["+str(FAE1)+" "+str(FAE2)+" "+str(FAE3)+" "+str(FAE4)+"]")
					if Matrix1_size == "2x3":
						if Matrix2_size == "3x1":
							FARC1 = int(M1R1twoxthreeC1)*int(M2R1threexoneC1)
							FARC2 = int(M1R1twoxthreeC2)*int(M2R2threexoneC1)
							FARC3 = int(M1R1twoxthreeC3)*int(M2R3threexoneC1)
							FAR2C1 = int(M1R2twoxthreeC1)*int(M2R1threexoneC1)
							FAR2C2 = int(M1R2twoxthreeC2)*int(M2R2threexoneC1)
							FAR2C3 = int(M1R2twoxthreeC3)*int(M2R3threexoneC1)
							FAE1R1 = int(FARC1)+int(FARC2)+int(FARC3)
							FAE1R2 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)
							print("")
							print("["+str(FAE1R1)+"]")
							print("["+str(FAE1R2)+"]")							
						if Matrix2_size == "3x2":
							FARC1 = int(M1R1twoxthreeC1)*int(M2R1threextwoC1)
							FARC2 = int(M1R1twoxthreeC2)*int(M2R2threextwoC1)
							FARC3 = int(M1R1twoxthreeC3)*int(M2R3threextwoC1)
							FAR2C1 = int(M1R1twoxthreeC1)*int(M2R1threextwoC2)
							FAR2C2 = int(M1R1twoxthreeC2)*int(M2R2threextwoC2)
							FAR2C3 = int(M1R1twoxthreeC3)*int(M2R3threextwoC2)
							FAR3C1 = int(M1R2twoxthreeC1)*int(M2R1threextwoC1)
							FAR3C2 = int(M1R2twoxthreeC2)*int(M2R2threextwoC1)
							FAR3C3 = int(M1R2twoxthreeC3)*int(M2R3threextwoC1)
							FAR4C1 = int(M1R2twoxthreeC1)*int(M2R1threextwoC2)
							FAR4C2 = int(M1R2twoxthreeC2)*int(M2R2threextwoC2)
							FAR4C3 = int(M1R2twoxthreeC3)*int(M2R3threextwoC2)				
							FAE1R1 = int(FARC1)+int(FARC2)+int(FARC3)
							FAE2R1 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)				
							FAE1R2 = int(FAR3C1)+int(FAR3C2)+int(FAR3C3)				
							FAE2R2 = int(FAR4C1)+int(FAR4C2)+int(FAR4C3)
							print("")
							print("["+str(FAE1R1)+" "+str(FAE2R1)+"]")
							print("["+str(FAE1R2)+" "+str(FAE2R2)+"]")
							#2x3
						if Matrix2_size == "3x3":
							FARC1 = int(M1R1twoxthreeC1)*int(M2R1threexthreeC1)
							FARC2 = int(M1R1twoxthreeC2)*int(M2R2threexthreeC1)
							FARC3 = int(M1R1twoxthreeC3)*int(M2R3threexthreeC1)					
							FAR2C1 = int(M1R1twoxthreeC1)*int(M2R1threexthreeC2)
							FAR2C2 = int(M1R1twoxthreeC2)*int(M2R2threexthreeC2)
							FAR2C3 = int(M1R1twoxthreeC3)*int(M2R3threexthreeC2)					
							FAR3C1 = int(M1R1twoxthreeC1)*int(M2R1threexthreeC3)
							FAR3C2 = int(M1R1twoxthreeC2)*int(M2R2threexthreeC3)
							FAR3C3 = int(M1R1twoxthreeC3)*int(M2R3threexthreeC3)																		
							FAR4C1 = int(M1R2twoxthreeC1)*int(M2R1threexthreeC1)
							FAR4C2 = int(M1R2twoxthreeC2)*int(M2R2threexthreeC1)
							FAR4C3 = int(M1R2twoxthreeC3)*int(M2R3threexthreeC1)						
							FAR5C1 = int(M1R2twoxthreeC1)*int(M2R1threexthreeC2)
							FAR5C2 = int(M1R2twoxthreeC2)*int(M2R2threexthreeC2)
							FAR5C3 = int(M1R2twoxthreeC3)*int(M2R3threexthreeC2)					
							FAR6C1 = int(M1R2twoxthreeC1)*int(M2R1threexthreeC3)
							FAR6C2 = int(M1R2twoxthreeC2)*int(M2R2threexthreeC3)
							FAR6C3 = int(M1R2twoxthreeC3)*int(M2R3threexthreeC3)						
							FARE1 = int(FARC1)+int(FARC2)+int(FARC3)						
							FARE2 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)						
							FARE3 = int(FAR3C1)+int(FAR3C2)+int(FAR3C3)												
							FAR2E1 = int(FAR4C1)+int(FAR4C2)+int(FAR4C3)						
							FAR2E2 = int(FAR5C1)+int(FAR5C2)+int(FAR5C3)
							FAR2E3 = int(FAR6C1)+int(FAR6C2)+int(FAR6C3)
							print("")
							print("["+str(FARE1)+" "+str(FARE2)+" "+str(FARE3)+"]")
							print("["+str(FAR2E1)+" "+str(FAR2E2)+" "+str(FAR2E3)+"]")
						if Matrix2_size == "3x4":
							FARC1 = int(M1R1twoxthreeC1)*int(M2R1threexfourC1)
							FARC2 = int(M1R1twoxthreeC2)*int(M2R2threexfourC1)
							FARC3 = int(M1R1twoxthreeC3)*int(M2R3threexfourC1)
							FAR2C1 = int(M1R1twoxthreeC1)*int(M2R1threexfourC2)
							FAR2C2 = int(M1R1twoxthreeC2)*int(M2R2threexfourC2)
							FAR2C3 = int(M1R1twoxthreeC3)*int(M2R3threexfourC2)
							FAR3C1 = int(M1R1twoxthreeC1)*int(M2R1threexfourC3)
							FAR3C2 = int(M1R1twoxthreeC2)*int(M2R2threexfourC3)
							FAR3C3 = int(M1R1twoxthreeC3)*int(M2R3threexfourC3)
							FAR4aC1 = int(M1R1twoxthreeC1)*int(M2R1threexfourC4)
							FAR4aC2 = int(M1R1twoxthreeC2)*int(M2R2threexfourC4)
							FAR4aC3 = int(M1R1twoxthreeC3)*int(M2R3threexfourC4)
							FAR4C1 = int(M1R2twoxthreeC1)*int(M2R1threexfourC1)
							FAR4C2 = int(M1R2twoxthreeC2)*int(M2R2threexfourC1)
							FAR4C3 = int(M1R2twoxthreeC3)*int(M2R3threexfourC1)				
							FAR5C1 = int(M1R2twoxthreeC1)*int(M2R1threexfourC2)
							FAR5C2 = int(M1R2twoxthreeC2)*int(M2R2threexfourC2)
							FAR5C3 = int(M1R2twoxthreeC3)*int(M2R3threexfourC2)		
							FAR6C1 = int(M1R2twoxthreeC1)*int(M2R1threexfourC3)
							FAR6C2 = int(M1R2twoxthreeC2)*int(M2R2threexfourC3)
							FAR6C3 = int(M1R2twoxthreeC3)*int(M2R3threexfourC3)
							FAR7C1 = int(M1R2twoxthreeC1)*int(M2R1threexfourC4)
							FAR7C2 = int(M1R2twoxthreeC2)*int(M2R2threexfourC4)
							FAR7C3 = int(M1R2twoxthreeC3)*int(M2R3threexfourC4)
							FARE1 = int(FARC1)+int(FARC2)+int(FARC3)						
							FARE2 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)						
							FARE3 = int(FAR3C1)+int(FAR3C2)+int(FAR3C3)
							FARE4 = int(FAR4aC1)+int(FAR4aC2)+int(FAR4aC3)
							FAR2E1 = int(FAR4C1)+int(FAR4C2)+int(FAR4C3)						
							FAR2E2 = int(FAR5C1)+int(FAR5C2)+int(FAR5C3)
							FAR2E3 = int(FAR6C1)+int(FAR6C2)+int(FAR6C3)
							FAR2E4 = int(FAR7C1)+int(FAR7C2)+int(FAR7C3)
							print("")
							print("["+str(FARE1)+" "+str(FARE2)+" "+str(FARE3)+" "+str(FARE4)+"]")
							print("["+str(FAR2E1)+" "+str(FAR2E2)+" "+str(FAR2E3)+" "+str(FAR2E4)+"]")
					if Matrix1_size == "2x2":
						if Matrix2_size == "2x1":
							FARC1 = int(M1R1twoxtwoC1)*int(M2R1twoxoneC1)
							FARC2 = int(M1R1twoxtwoC2)*int(M2R2twoxoneC1)
							FAR2C1 = int(M1R2twoxtwoC1)*int(M2R1twoxoneC1)
							FAR2C2 = int(M1R2twoxtwoC2)*int(M2R2twoxoneC1)
							FAER1 = int(FARC1)+int(FARC2)
							FAER2 = int(FAR2C1)+int(FAR2C2)
							print("")
							print("["+str(FAER1)+"]")
							print("["+str(FAER2)+"]")
						if Matrix2_size == "2x2":
							FARC1 = int(M1R1twoxtwoC1)*int(M2R1twoxtwoC1)
							FARC2 = int(M1R1twoxtwoC2)*int(M2R2twoxtwoC1)
							FAR2C1 = int(M1R1twoxtwoC1)*int(M2R1twoxtwoC2)
							FAR2C2 = int(M1R1twoxtwoC2)*int(M2R2twoxtwoC2)
							FAR3C1 = int(M1R2twoxtwoC1)*int(M2R1twoxtwoC1)
							FAR3C2 = int(M1R2twoxtwoC2)*int(M2R2twoxtwoC1)
							FAR4C1 = int(M1R2twoxtwoC1)*int(M2R1twoxtwoC2)
							FAR4C2 = int(M1R2twoxtwoC2)*int(M2R2twoxtwoC2)	
							FAE1R1 = int(FARC1)+int(FARC2)
							FAE1R2 = int(FAR2C1)+int(FAR2C2)
							FAE2R3 = int(FAR3C1)+int(FAR3C2)
							FAE3R4 = int(FAR4C1)+int(FAR4C2)
							print("")
							print("["+str(FAE1R1)+" "+str(FAE1R2)+"]")
							print("["+str(FAE2R3)+" "+str(FAE3R4)+"]")
						if Matrix2_size == "2x3": 
							FAR1C1 = int(M1R1twoxtwoC1)*int(M2R1twoxthreeC1)
							FAR2C1 = int(M1R1twoxtwoC2)*int(M2R2twoxthreeC1)
							FAR3C2 = int(M1R1twoxtwoC1)*int(M2R1twoxthreeC2)
							FAR4C2 = int(M1R1twoxtwoC2)*int(M2R2twoxthreeC2)
							FAR5C3 = int(M1R1twoxtwoC1)*int(M2R1twoxthreeC3)
							FAR6C3 = int(M1R1twoxtwoC2)*int(M2R2twoxthreeC3)
							FAR1C4 = int(M1R2twoxtwoC1)*int(M2R1twoxthreeC1)
							FAR2C4 = int(M1R2twoxtwoC2)*int(M2R2twoxthreeC1)
							FAR3C5 = int(M1R2twoxtwoC1)*int(M2R1twoxthreeC2)
							FAR4C5 = int(M1R2twoxtwoC2)*int(M2R2twoxthreeC2)
							FAR5C6 = int(M1R2twoxtwoC1)*int(M2R1twoxthreeC3)
							FAR6C6 = int(M1R2twoxtwoC2)*int(M2R2twoxthreeC3)
							FAE1R1 = int(FAR1C1)+int(FAR2C1)
							FAE2R1 = int(FAR3C2)+int(FAR4C2)
							FAE3R1 = int(FAR5C3)+int(FAR6C3)
							FAE4R2 = int(FAR1C4)+int(FAR2C4)
							FAE5R2 = int(FAR3C5)+int(FAR4C5)
							FAE6R2 = int(FAR5C6)+int(FAR6C6)
							print("")
							print("["+str(FAE1R1)+" "+str(FAE2R1)+" "+str(FAE3R1)+"]")
							print("["+str(FAE4R2)+" "+str(FAE5R2)+" "+str(FAE6R2)+"]")
						if Matrix2_size == "2x4":
							FAR1C1 = int(M1R1twoxtwoC1)*int(M2R1twoxfourC1)
							FAR2C1 = int(M1R1twoxtwoC2)*int(M2R2twoxfourC1)
							FAR3C2 = int(M1R1twoxtwoC1)*int(M2R1twoxfourC2)
							FAR4C2 = int(M1R1twoxtwoC2)*int(M2R2twoxfourC2)
							FAR5C3 = int(M1R1twoxtwoC1)*int(M2R1twoxfourC3)
							FAR6C3 = int(M1R1twoxtwoC2)*int(M2R2twoxfourC3)
							FAR5aC3 = int(M1R1twoxtwoC1)*int(M2R1twoxfourC4)
							FAR6aC3 = int(M1R1twoxtwoC2)*int(M2R2twoxfourC4)
							FAR1C4 = int(M1R2twoxtwoC1)*int(M2R1twoxfourC1)
							FAR2C4 = int(M1R2twoxtwoC2)*int(M2R2twoxfourC1)
							FAR3C5 = int(M1R2twoxtwoC1)*int(M2R1twoxfourC2)
							FAR4C5 = int(M1R2twoxtwoC2)*int(M2R2twoxfourC2)
							FAR5C6 = int(M1R2twoxtwoC1)*int(M2R1twoxfourC3)
							FAR6C6 = int(M1R2twoxtwoC2)*int(M2R2twoxfourC3)
							FAR5bC6 = int(M1R2twoxtwoC1)*int(M2R1twoxfourC4)
							FAR6bC6 = int(M1R2twoxtwoC2)*int(M2R2twoxfourC4)
							FAE1R1 = int(FAR1C1)+int(FAR2C1)
							FAE2R1 = int(FAR3C2)+int(FAR4C2)
							FAE3R1 = int(FAR5C3)+int(FAR6C3)
							FAE4R1 = int(FAR5aC3)+int(FAR6aC3)
							FAE4R2 = int(FAR1C4)+int(FAR2C4)
							FAE5R2 = int(FAR3C5)+int(FAR4C5)
							FAE6R2 = int(FAR5C6)+int(FAR6C6)
							FAE7R2 = int(FAR5bC6)+int(FAR6bC6)
							print("")
							print("["+str(FAE1R1)+" "+str(FAE2R1)+" "+str(FAE3R1)+" "+str(FAE4R1)+"]")
							print("["+str(FAE4R2)+" "+str(FAE5R2)+" "+str(FAE6R2)+" "+str(FAE7R2)+"]")
					if Matrix1_size == "2x1":
						if Matrix2_size == "1x1":
							FARC1 = int(M1R1twoxoneC1)*int(M2R1onexoneC1)
							FARC2 = int(M1R2twoxoneC1)*int(M2R1onexoneC1)
							print("")
							print("["+str(FARC1)+"]")
							print("["+str(FARC2)+"]")
						if Matrix2_size == "1x2":
							FARC1 = int(M1R1twoxoneC1)*int(M2R1onextwoC1)
							FARC2 = int(M1R1twoxoneC1)*int(M2R1onextwoC2)
							FAR2C1 = int(M1R2twoxoneC1)*int(M2R1onextwoC1)
							FAR2C2 = int(M1R2twoxoneC1)*int(M2R1onextwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+"]")
						if Matrix2_size == "1x3":
							FARC1 = int(M1R1twoxoneC1)*int(M2R1onexthreeC1)
							FARC2 = int(M1R1twoxoneC1)*int(M2R1onexthreeC2)
							FARC3 = int(M1R1twoxoneC1)*int(M2R1onexthreeC3)
							FAR2C1 = int(M1R2twoxoneC1)*int(M2R1onexthreeC1)
							FAR2C2 = int(M1R2twoxoneC1)*int(M2R1onexthreeC2)
							FAR2C3 = int(M1R2twoxoneC1)*int(M2R1onexthreeC3)
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+"]")
						if Matrix2_size == "1x4":
							FARC1 = int(M1R1twoxoneC1)*int(M2R1onexfourC1)
							FARC2 = int(M1R1twoxoneC1)*int(M2R1onexfourC2)
							FARC3 = int(M1R1twoxoneC1)*int(M2R1onexfourC3)
							FARaC3 = int(M1R1twoxoneC1)*int(M2R1onexfourC4)
							FAR2C1 = int(M1R2twoxoneC1)*int(M2R1onexfourC1)
							FAR2C2 = int(M1R2twoxoneC1)*int(M2R1onexfourC2)
							FAR2C3 = int(M1R2twoxoneC1)*int(M2R1onexfourC3)
							FAR2bC3 = int(M1R2twoxoneC1)*int(M2R1onexfourC4)
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+" "+str(FARaC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2bC3)+"]")
					if Matrix1_size == "3x1":
						if Matrix2_size == "1x1":
							FAR1C1 = int(M1R1threexoneC1)*int(M2R1onexoneC1)
							FAR2C1 = int(M1R2threexoneC1)*int(M2R1onexoneC1)
							FAR3C1 = int(M1R3threexoneC1)*int(M2R1onexoneC1)
							print("["+str(FAR1C1)+"]")				
							print("["+str(FAR2C1)+"]")	
							print("["+str(FAR3C1)+"]")	
						if Matrix2_size == "1x2":
							FARC1 = int(M1R1threexoneC1)*int(M2R1onextwoC1)
							FARC2 = int(M1R1threexoneC1)*int(M2R1onextwoC2)
							FAR2C1 = int(M1R2threexoneC1)*int(M2R1onextwoC1)
							FAR2C2 = int(M1R2threexoneC1)*int(M2R1onextwoC2)
							FAR3C1 = int(M1R3threexoneC1)*int(M2R1onextwoC1)
							FAR3C2 = int(M1R3threexoneC1)*int(M2R1onextwoC2)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+"]")		
						if Matrix2_size == "1x3":
							FARC1 = int(M1R1threexoneC1)*int(M2R1onexthreeC1)
							FARC2 = int(M1R1threexoneC1)*int(M2R1onexthreeC2)
							FARC3 = int(M1R1threexoneC1)*int(M2R1onexthreeC3)
							FAR2C1 = int(M1R2threexoneC1)*int(M2R1onexthreeC1)
							FAR2C2 = int(M1R2threexoneC1)*int(M2R1onexthreeC2)
							FAR2C3 = int(M1R2threexoneC1)*int(M2R1onexthreeC3)
							FAR3C1 = int(M1R3threexoneC1)*int(M2R1onexthreeC1)
							FAR3C2 = int(M1R3threexoneC1)*int(M2R1onexthreeC2)
							FAR3C3 = int(M1R3threexoneC1)*int(M2R1onexthreeC3)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+"]")
						if Matrix2_size == "1x4":
							FARC1 = int(M1R1threexoneC1)*int(M2R1onexfourC1)
							FARC2 = int(M1R1threexoneC1)*int(M2R1onexfourC2)
							FARC3 = int(M1R1threexoneC1)*int(M2R1onexfourC3)
							FARaC3 = int(M1R1threexoneC1)*int(M2R1onexfourC4)
							FAR2C1 = int(M1R2threexoneC1)*int(M2R1onexfourC1)
							FAR2C2 = int(M1R2threexoneC1)*int(M2R1onexfourC2)
							FAR2C3 = int(M1R2threexoneC1)*int(M2R1onexfourC3)
							FAR2bC3 = int(M1R2threexoneC1)*int(M2R1onexfourC4)
							FAR3C1 = int(M1R3threexoneC1)*int(M2R1onexfourC1)
							FAR3C2 = int(M1R3threexoneC1)*int(M2R1onexfourC2)
							FAR3C3 = int(M1R3threexoneC1)*int(M2R1onexfourC3)
							FAR3cC3 = int(M1R3threexoneC1)*int(M2R1onexfourC4)
							print("")
							print("["+str(FARC1)+" "+str(FARC2)+" "+str(FARC3)+" "+str(FARaC3)+"]")
							print("["+str(FAR2C1)+" "+str(FAR2C2)+" "+str(FAR2C3)+" "+str(FAR2bC3)+"]")
							print("["+str(FAR3C1)+" "+str(FAR3C2)+" "+str(FAR3C3)+" "+str(FAR3cC3)+"]")
					if Matrix1_size == "3x2":
						if Matrix2_size == "2x1":
							FARC1 = int(M1R1threextwoC1)*int(M2R1twoxoneC1)
							FARC2 = int(M1R1threextwoC2)*int(M2R2twoxoneC1)
							FAR2C1 = int(M1R2threextwoC1)*int(M2R1twoxoneC1)
							FAR2C2 = int(M1R2threextwoC2)*int(M2R2twoxoneC1)
							FAR3C1 = int(M1R3threextwoC1)*int(M2R1twoxoneC1)
							FAR3C2 = int(M1R3threextwoC2)*int(M2R2twoxoneC1)
							FAR1 = int(FARC1)+int(FARC2)
							FAR2 = int(FAR2C1)+int(FAR2C2)
							FAR3 = int(FAR3C1)+int(FAR3C2)
							print("")
							print("["+str(FAR1)+"]")
							print("["+str(FAR2)+"]")
							print("["+str(FAR3)+"]")
						if Matrix2_size == "2x2":
							FARC1 = int(M1R1threextwoC1)*int(M2R1twoxtwoC1)
							FARC2 = int(M1R1threextwoC2)*int(M2R2twoxtwoC1)
							FAR2C1 = int(M1R1threextwoC1)*int(M2R1twoxtwoC2)
							FAR2C2 = int(M1R1threextwoC2)*int(M2R2twoxtwoC2)
							FAR3C1 = int(M1R2threextwoC1)*int(M2R1twoxtwoC1)
							FAR3C2 = int(M1R2threextwoC2)*int(M2R2twoxtwoC1)
							FAR4C1 = int(M1R2threextwoC1)*int(M2R1twoxtwoC2)
							FAR4C2 = int(M1R2threextwoC2)*int(M2R2twoxtwoC2)
							FAR5C1 = int(M1R3threextwoC1)*int(M2R1twoxtwoC1)
							FAR5C2 = int(M1R3threextwoC2)*int(M2R2twoxtwoC1)
							FAR6C1 = int(M1R3threextwoC1)*int(M2R1twoxtwoC2)
							FAR6C2 = int(M1R3threextwoC2)*int(M2R2twoxtwoC2)
							FAR1E1 = int(FARC1)+int(FARC2)
							FAR1E2 = int(FAR2C1)+int(FAR2C2)
							FAR2E1 = int(FAR3C1)+int(FAR3C2)
							FAR2E2 = int(FAR4C1)+int(FAR4C2)
							FAR3E1 = int(FAR5C1)+int(FAR5C2)
							FAR3E2 = int(FAR6C1)+int(FAR6C2)
							print("")
							print("["+str(FAR1E1)+" "+str(FAR1E2)+"]")
							print("["+str(FAR2E1)+" "+str(FAR2E2)+"]")
							print("["+str(FAR3E1)+" "+str(FAR3E2)+"]")
						if Matrix2_size == "2x3":
							FAR1C1 = int(M1R1threextwoC1)*int(M2R1twoxthreeC1)
							FAR2C1 = int(M1R1threextwoC2)*int(M2R2twoxthreeC1)
							FAR3C1 = int(M1R1threextwoC1)*int(M2R1twoxthreeC2)
							FAR4C1 = int(M1R1threextwoC2)*int(M2R2twoxthreeC2)
							FAR5C1 = int(M1R1threextwoC1)*int(M2R1twoxthreeC3)
							FAR6C1 = int(M1R1threextwoC2)*int(M2R2twoxthreeC3)
							FAR7C1 = int(M1R2threextwoC1)*int(M2R1twoxthreeC1)
							FAR8C1 = int(M1R2threextwoC2)*int(M2R2twoxthreeC1)
							FAR9C1 = int(M1R2threextwoC1)*int(M2R1twoxthreeC2)
							FAR10C1 = int(M1R2threextwoC2)*int(M2R2twoxthreeC2)
							FAR11C1 = int(M1R2threextwoC1)*int(M2R1twoxthreeC3)
							FAR12C1 = int(M1R2threextwoC2)*int(M2R2twoxthreeC3)
							FAR13C1 = int(M1R3threextwoC1)*int(M2R1twoxthreeC1)
							FAR14C1 = int(M1R3threextwoC2)*int(M2R2twoxthreeC1)
							FAR15C1 = int(M1R3threextwoC1)*int(M2R1twoxthreeC2)
							FAR16C1 = int(M1R3threextwoC2)*int(M2R2twoxthreeC2)
							FAR17C1 = int(M1R3threextwoC1)*int(M2R1twoxthreeC3)
							FAR18C1 = int(M1R3threextwoC2)*int(M2R2twoxthreeC3)
							FAR1E1 = int(FAR1C1)+int(FAR2C1)
							FAR1E2 = int(FAR3C1)+int(FAR4C1)
							FAR1E3 = int(FAR5C1)+int(FAR6C1)
							FAR2E1 = int(FAR7C1)+int(FAR8C1)
							FAR2E2 = int(FAR9C1)+int(FAR10C1)
							FAR2E3 = int(FAR11C1)+int(FAR12C1)
							FAR3E1 = int(FAR13C1)+int(FAR14C1)
							FAR3E2 = int(FAR15C1)+int(FAR16C1)
							FAR3E3 = int(FAR17C1)+int(FAR18C1)
							print("")
							print("["+str(FAR1E1)+" "+str(FAR1E2)+" "+str(FAR1E3)+"]")
							print("["+str(FAR2E1)+" "+str(FAR2E2)+" "+str(FAR2E3)+"]")
							print("["+str(FAR3E1)+" "+str(FAR3E2)+" "+str(FAR3E3)+"]")
						if Matrix2_size == "2x4":
							FAR1C1 = int(M1R1threextwoC1)*int(M2R1twoxfourC1)
							FAR2C1 = int(M1R1threextwoC2)*int(M2R2twoxfourC1)
							FAR3C1 = int(M1R1threextwoC1)*int(M2R1twoxfourC2)
							FAR4C1 = int(M1R1threextwoC2)*int(M2R2twoxfourC2)
							FAR5C1 = int(M1R1threextwoC1)*int(M2R1twoxfourC3)
							FAR6C1 = int(M1R1threextwoC2)*int(M2R2twoxfourC3)	
							FAR5aC1 = int(M1R1threextwoC1)*int(M2R1twoxfourC4)
							FAR6aC1 = int(M1R1threextwoC2)*int(M2R2twoxfourC4)
							FAR7C1 = int(M1R2threextwoC1)*int(M2R1twoxfourC1)
							FAR8C1 = int(M1R2threextwoC2)*int(M2R2twoxfourC1)
							FAR9C1 = int(M1R2threextwoC1)*int(M2R1twoxfourC2)
							FAR10C1 = int(M1R2threextwoC2)*int(M2R2twoxfourC2)	
							FAR11C1 = int(M1R2threextwoC1)*int(M2R1twoxfourC3)
							FAR12C1 = int(M1R2threextwoC2)*int(M2R2twoxfourC3)
							FAR11bC1 = int(M1R2threextwoC1)*int(M2R1twoxfourC4)
							FAR12bC1 = int(M1R2threextwoC2)*int(M2R2twoxfourC4)	
							FAR13C1 = int(M1R3threextwoC1)*int(M2R1twoxfourC1)
							FAR14C1 = int(M1R3threextwoC2)*int(M2R2twoxfourC1)
							FAR15C1 = int(M1R3threextwoC1)*int(M2R1twoxfourC2)
							FAR16C1 = int(M1R3threextwoC2)*int(M2R2twoxfourC2)
							FAR17C1 = int(M1R3threextwoC1)*int(M2R1twoxfourC3)
							FAR18C1 = int(M1R3threextwoC2)*int(M2R2twoxfourC3)
							FAR17cC1 = int(M1R3threextwoC1)*int(M2R1twoxfourC4)
							FAR18cC1 = int(M1R3threextwoC2)*int(M2R2twoxfourC4)
							FAR1E1 = int(FAR1C1)+int(FAR2C1)
							FAR1E2 = int(FAR3C1)+int(FAR4C1)
							FAR1E3 = int(FAR5C1)+int(FAR6C1)
							FAR1E4 = int(FAR5aC1)+int(FAR6aC1)
							FAR2E1 = int(FAR7C1)+int(FAR8C1)
							FAR2E2 = int(FAR9C1)+int(FAR10C1)
							FAR2E3 = int(FAR11C1)+int(FAR12C1)
							FAR2E4 = int(FAR11bC1)+int(FAR12bC1)
							FAR3E1 = int(FAR13C1)+int(FAR14C1)
							FAR3E2 = int(FAR15C1)+int(FAR16C1)
							FAR3E3 = int(FAR17C1)+int(FAR18C1)
							FAR3E4 = int(FAR17cC1)+int(FAR18cC1)
							print("")
							print("["+str(FAR1E1)+" "+str(FAR1E2)+" "+str(FAR1E3)+" "+str(FAR1E4)+"]")
							print("["+str(FAR2E1)+" "+str(FAR2E2)+" "+str(FAR2E3)+" "+str(FAR2E4)+"]")
							print("["+str(FAR3E1)+" "+str(FAR3E2)+" "+str(FAR3E3)+" "+str(FAR3E4)+"]")
					if Matrix1_size == "3x3":
						if Matrix2_size == "3x1":
							FAC1R1 = int(M1R1threexthreeC1)*int(M2R1threexoneC1)
							FAC2R1 = int(M1R1threexthreeC2)*int(M2R2threexoneC1)
							FAC3R1 = int(M1R1threexthreeC3)*int(M2R3threexoneC1)
							FAC1R2 = int(M1R2threexthreeC1)*int(M2R1threexoneC1)
							FAC2R2 = int(M1R2threexthreeC2)*int(M2R2threexoneC1)
							FAC3R2 = int(M1R2threexthreeC3)*int(M2R3threexoneC1)
							FAC1R3 = int(M1R3threexthreeC1)*int(M2R1threexoneC1)
							FAC2R3 = int(M1R3threexthreeC2)*int(M2R2threexoneC1)
							FAC3R3 = int(M1R3threexthreeC3)*int(M2R3threexoneC1)						
							FAE1R1 = int(FAC1R1)+int(FAC2R1)+int(FAC3R1)
							FAE2R2 = int(FAC1R2)+int(FAC2R2)+int(FAC3R2)
							FAE3R3 = int(FAC1R3)+int(FAC2R3)+int(FAC3R3)
							print("")
							print("["+str(FAE1R1)+"]")
							print("["+str(FAE2R2)+"]")
							print("["+str(FAE3R3)+"]")					
						if Matrix2_size == "3x2":
							FAC1R1 = int(M1R1threexthreeC1)*int(M2R1threextwoC1)
							FAC2R1 = int(M1R1threexthreeC2)*int(M2R2threextwoC1)
							FAC3R1 = int(M1R1threexthreeC3)*int(M2R3threextwoC1)
							FAC4c2R1 = int(M1R1threexthreeC1)*int(M2R1threextwoC2)
							FAC5c2R1 = int(M1R1threexthreeC2)*int(M2R2threextwoC2)
							FAC6c2R1 = int(M1R1threexthreeC3)*int(M2R3threextwoC2)
							FAC7R2 = int(M1R2threexthreeC1)*int(M2R1threextwoC1)
							FAC8R2 = int(M1R2threexthreeC2)*int(M2R2threextwoC1)
							FAC9R2 = int(M1R2threexthreeC3)*int(M2R3threextwoC1)
							FAC10c2R2 = int(M1R2threexthreeC1)*int(M2R1threextwoC2)
							FAC11c2R2 = int(M1R2threexthreeC2)*int(M2R2threextwoC2)
							FAC12c2R2 = int(M1R2threexthreeC3)*int(M2R3threextwoC2)
							FAC13R3 = int(M1R3threexthreeC1)*int(M2R1threextwoC1)
							FAC14R3 = int(M1R3threexthreeC2)*int(M2R2threextwoC1)
							FAC15R3 = int(M1R3threexthreeC3)*int(M2R3threextwoC1)
							FAC16c2R3 = int(M1R3threexthreeC1)*int(M2R1threextwoC2)
							FAC17c2R3 = int(M1R3threexthreeC2)*int(M2R2threextwoC2)
							FAC18c2R3 = int(M1R3threexthreeC3)*int(M2R3threextwoC2)	
							FAE1C1 = int(FAC1R1)+int(FAC2R1)+int(FAC3R1)
							FAE2C1 = int(FAC4c2R1)+int(FAC5c2R1)+int(FAC6c2R1)
							FAE3C2 = int(FAC7R2)+int(FAC8R2)+int(FAC9R2)
							FAE4C2 = int(FAC10c2R2)+int(FAC11c2R2)+int(FAC12c2R2)
							FAE5C3 = int(FAC13R3)+int(FAC14R3)+int(FAC15R3)
							FAE6C3 = int(FAC16c2R3)+int(FAC17c2R3)+int(FAC18c2R3)
							print("")
							print("["+str(FAE1C1)+" "+str(FAE2C1)+"]")
							print("["+str(FAE3C2)+" "+str(FAE4C2)+"]")
							print("["+str(FAE5C3)+" "+str(FAE6C3)+"]")
						if Matrix2_size == "3x3":
							FAC1R1 = int(M1R1threexthreeC1)*int(M2R1threexthreeC1)
							FAC2R1 = int(M1R1threexthreeC2)*int(M2R2threexthreeC1)
							FAC3R1 = int(M1R1threexthreeC3)*int(M2R3threexthreeC1)
							FAC4c2R1 = int(M1R1threexthreeC1)*int(M2R1threexthreeC2)
							FAC5c2R1 = int(M1R1threexthreeC2)*int(M2R2threexthreeC2)
							FAC6c2R1 = int(M1R1threexthreeC3)*int(M2R3threexthreeC2)
							FAC1c3R1 = int(M1R1threexthreeC1)*int(M2R1threexthreeC3)
							FAC2c3R1 = int(M1R1threexthreeC2)*int(M2R2threexthreeC3)
							FAC3c3R1 = int(M1R1threexthreeC3)*int(M2R3threexthreeC3)
							FAC7R2 = int(M1R2threexthreeC1)*int(M2R1threexthreeC1)
							FAC8R2 = int(M1R2threexthreeC2)*int(M2R2threexthreeC1)
							FAC9R2 = int(M1R2threexthreeC3)*int(M2R3threexthreeC1)
							FAC10c2R2 = int(M1R2threexthreeC1)*int(M2R1threexthreeC2)
							FAC11c2R2 = int(M1R2threexthreeC2)*int(M2R2threexthreeC2)
							FAC12c2R2 = int(M1R2threexthreeC3)*int(M2R3threexthreeC2)
							FAC4c3R2 = int(M1R2threexthreeC1)*int(M2R1threexthreeC3)
							FAC5c3R2 = int(M1R2threexthreeC2)*int(M2R2threexthreeC3)
							FAC6c3R2 = int(M1R2threexthreeC3)*int(M2R3threexthreeC3)
							FAC13R3 = int(M1R3threexthreeC1)*int(M2R1threexthreeC1)
							FAC14R3 = int(M1R3threexthreeC2)*int(M2R2threexthreeC1)
							FAC15R3 = int(M1R3threexthreeC3)*int(M2R3threexthreeC1)
							FAC16c2R3 = int(M1R3threexthreeC1)*int(M2R1threexthreeC2)
							FAC17c2R3 = int(M1R3threexthreeC2)*int(M2R2threexthreeC2)
							FAC18c2R3 = int(M1R3threexthreeC3)*int(M2R3threexthreeC2)
							FAC7c3R3 = int(M1R3threexthreeC1)*int(M2R1threexthreeC3)
							FAC8c3R3 = int(M1R3threexthreeC2)*int(M2R2threexthreeC3)
							FAC9c3R3 = int(M1R3threexthreeC3)*int(M2R3threexthreeC3)
							FAE1R1 = int(FAC1R1)+int(FAC2R1)+int(FAC3R1)
							FAE2R1 = int(FAC4c2R1)+int(FAC5c2R1)+int(FAC6c2R1)
							FAE3R1 = int(FAC1c3R1)+int(FAC2c3R1)+int(FAC3c3R1)
							FAE4R2 = int(FAC7R2)+int(FAC8R2)+int(FAC9R2)
							FAE5R2 = int(FAC10c2R2)+int(FAC11c2R2)+int(FAC12c2R2)
							FAE6R2 = int(FAC4c3R2)+int(FAC5c3R2)+int(FAC6c3R2)
							FAE7R3 = int(FAC13R3)+int(FAC14R3)+int(FAC15R3)
							FAE8R3 = int(FAC16c2R3)+int(FAC17c2R3)+int(FAC18c2R3)
							FAE9R3 = int(FAC7c3R3)+int(FAC8c3R3)+int(FAC9c3R3)
							print("")
							print("["+str(FAE1R1)+" "+str(FAE2R1)+" "+str(FAE3R1)+"]")
							print("["+str(FAE4R2)+" "+str(FAE5R2)+" "+str(FAE6R2)+"]")
							print("["+str(FAE7R3)+" "+str(FAE8R3)+" "+str(FAE9R3)+"]")
						if Matrix2_size == "3x4":
							FAC1R1 = int(M1R1threexthreeC1)*int(M2R1threexfourC1)
							FAC2R1 = int(M1R1threexthreeC2)*int(M2R2threexfourC1)
							FAC3R1 = int(M1R1threexthreeC3)*int(M2R3threexfourC1)
							FAC4c2R1 = int(M1R1threexthreeC1)*int(M2R1threexfourC2)
							FAC5c2R1 = int(M1R1threexthreeC2)*int(M2R2threexfourC2)
							FAC6c2R1 = int(M1R1threexthreeC3)*int(M2R3threexfourC2)
							FAC1c3R1 = int(M1R1threexthreeC1)*int(M2R1threexfourC3)
							FAC2c3R1 = int(M1R1threexthreeC2)*int(M2R2threexfourC3)
							FAC3c3R1 = int(M1R1threexthreeC3)*int(M2R3threexfourC3)
							FAC1c4R1 = int(M1R1threexthreeC1)*int(M2R1threexfourC4)
							FAC2c4R1 = int(M1R1threexthreeC2)*int(M2R2threexfourC4)
							FAC3c4R1 = int(M1R1threexthreeC3)*int(M2R3threexfourC4)
							FAC7R2 = int(M1R2threexthreeC1)*int(M2R1threexfourC1)
							FAC8R2 = int(M1R2threexthreeC2)*int(M2R2threexfourC1)
							FAC9R2 = int(M1R2threexthreeC3)*int(M2R3threexfourC1)
							FAC10c2R2 = int(M1R2threexthreeC1)*int(M2R1threexfourC2)
							FAC11c2R2 = int(M1R2threexthreeC2)*int(M2R2threexfourC2)
							FAC12c2R2 = int(M1R2threexthreeC3)*int(M2R3threexfourC2)
							FAC4c3R2 = int(M1R2threexthreeC1)*int(M2R1threexfourC3)
							FAC5c3R2 = int(M1R2threexthreeC2)*int(M2R2threexfourC3)
							FAC6c3R2 = int(M1R2threexthreeC3)*int(M2R3threexfourC3)
							FAC4c4R2 = int(M1R2threexthreeC1)*int(M2R1threexfourC4)
							FAC5c4R2 = int(M1R2threexthreeC2)*int(M2R2threexfourC4)
							FAC6c4R2 = int(M1R2threexthreeC3)*int(M2R3threexfourC4)			
							FAC13R3 = int(M1R3threexthreeC1)*int(M2R1threexfourC1)
							FAC14R3 = int(M1R3threexthreeC2)*int(M2R2threexfourC1)
							FAC15R3 = int(M1R3threexthreeC3)*int(M2R3threexfourC1)
							FAC16c2R3 = int(M1R3threexthreeC1)*int(M2R1threexfourC2)
							FAC17c2R3 = int(M1R3threexthreeC2)*int(M2R2threexfourC2)
							FAC18c2R3 = int(M1R3threexthreeC3)*int(M2R3threexfourC2)		
							FAC7c3R3 = int(M1R3threexthreeC1)*int(M2R1threexfourC3)
							FAC8c3R3 = int(M1R3threexthreeC2)*int(M2R2threexfourC3)
							FAC9c3R3 = int(M1R3threexthreeC3)*int(M2R3threexfourC3)
							FAC7c4R3 = int(M1R3threexthreeC1)*int(M2R1threexfourC4)
							FAC8c4R3 = int(M1R3threexthreeC2)*int(M2R2threexfourC4)
							FAC9c4R3 = int(M1R3threexthreeC3)*int(M2R3threexfourC4)			
							FAE1R1 = int(FAC1R1)+int(FAC2R1)+int(FAC3R1)
							FAE2R1 = int(FAC4c2R1)+int(FAC5c2R1)+int(FAC6c2R1)
							FAE3R1 = int(FAC1c3R1)+int(FAC2c3R1)+int(FAC3c3R1)
							FAE4R1 = int(FAC1c4R1)+int(FAC2c4R1)+int(FAC3c4R1)
							FAE4R2 = int(FAC7R2)+int(FAC8R2)+int(FAC9R2)
							FAE5R2 = int(FAC10c2R2)+int(FAC11c2R2)+int(FAC12c2R2)
							FAE6R2 = int(FAC4c3R2)+int(FAC5c3R2)+int(FAC6c3R2)
							FAE7R2 = int(FAC4c4R2)+int(FAC5c4R2)+int(FAC6c4R2)	
							FAE7R3 = int(FAC13R3)+int(FAC14R3)+int(FAC15R3)
							FAE8R3 = int(FAC16c2R3)+int(FAC17c2R3)+int(FAC18c2R3)
							FAE9R3 = int(FAC7c3R3)+int(FAC8c3R3)+int(FAC9c3R3)
							FAE10R3 = int(FAC7c4R3)+int(FAC8c4R3)+int(FAC9c4R3)
							print("")
							print("["+str(FAE1R1)+" "+str(FAE2R1)+" "+str(FAE3R1)+" "+str(FAE4R1)+"]")
							print("["+str(FAE4R2)+" "+str(FAE5R2)+" "+str(FAE6R2)+" "+str(FAE7R2)+"]")
							print("["+str(FAE7R3)+" "+str(FAE8R3)+" "+str(FAE9R3)+" "+str(FAE10R3)+"]")
					if Matrix1_size == "4x1":
						if Matrix2_size == "1x1":
							FAR1 = int(M1R1fourxoneC1)*int(M2R1onexoneC1)
							FAR2 = int(M1R2fourxoneC1)*int(M2R1onexoneC1)
							FAR3 = int(M1R3fourxoneC1)*int(M2R1onexoneC1)
							FAR4 = int(M1R4fourxoneC1)*int(M2R1onexoneC1)
							print("")
							print("["+str(FAR1)+"]")
							print("["+str(FAR2)+"]")
							print("["+str(FAR3)+"]")
							print("["+str(FAR4)+"]")
						if Matrix2_size == "1x2":
							FARC1R1 = int(M1R1fourxoneC1)*int(M2R1onextwoC1)
							FARC2R1 = int(M1R1fourxoneC1)*int(M2R1onextwoC2)
							FARC1R2 = int(M1R2fourxoneC1)*int(M2R1onextwoC1)
							FARC2R2 = int(M1R2fourxoneC1)*int(M2R1onextwoC2)
							FARC1R3 = int(M1R3fourxoneC1)*int(M2R1onextwoC1)
							FARC2R3 = int(M1R3fourxoneC1)*int(M2R1onextwoC2)
							FARC1R4 = int(M1R4fourxoneC1)*int(M2R1onextwoC1)
							FARC2R4 = int(M1R4fourxoneC1)*int(M2R1onextwoC2)
							print("")
							print("["+str(FARC1R1)+" "+str(FARC2R1)+"]")
							print("["+str(FARC1R2)+" "+str(FARC2R2)+"]")
							print("["+str(FARC1R3)+" "+str(FARC2R3)+"]")
							print("["+str(FARC1R4)+" "+str(FARC2R4)+"]")
						if Matrix2_size == "1x3":
							FARC1R1 = int(M1R1fourxoneC1)*int(M2R1onexthreeC1)
							FARC2R1 = int(M1R1fourxoneC1)*int(M2R1onexthreeC2)
							FARC3R1 = int(M1R1fourxoneC1)*int(M2R1onexthreeC3)
							FARC1R2 = int(M1R2fourxoneC1)*int(M2R1onexthreeC1)
							FARC2R2 = int(M1R2fourxoneC1)*int(M2R1onexthreeC2)
							FARC3R2 = int(M1R2fourxoneC1)*int(M2R1onexthreeC3)
							FARC1R3 = int(M1R3fourxoneC1)*int(M2R1onexthreeC1)
							FARC2R3 = int(M1R3fourxoneC1)*int(M2R1onexthreeC2)
							FARC3R3 = int(M1R3fourxoneC1)*int(M2R1onexthreeC3)
							FARC1R4 = int(M1R4fourxoneC1)*int(M2R1onexthreeC1)
							FARC2R4 = int(M1R4fourxoneC1)*int(M2R1onexthreeC2)
							FARC3R4 = int(M1R4fourxoneC1)*int(M2R1onexthreeC3)
							print("")
							print("["+str(FARC1R1)+" "+str(FARC2R1)+" "+str(FARC3R1)+"]")
							print("["+str(FARC1R2)+" "+str(FARC2R2)+" "+str(FARC3R2)+"]")
							print("["+str(FARC1R3)+" "+str(FARC2R3)+" "+str(FARC3R3)+"]")
							print("["+str(FARC1R4)+" "+str(FARC2R4)+" "+str(FARC3R4)+"]")
						if Matrix2_size == "1x4":
							FARC1R1 = int(M1R1fourxoneC1)*int(M2R1onexfourC1)
							FARC2R1 = int(M1R1fourxoneC1)*int(M2R1onexfourC2)
							FARC3R1 = int(M1R1fourxoneC1)*int(M2R1onexfourC3)
							FARC4R1 = int(M1R1fourxoneC1)*int(M2R1onexfourC4)
							FARC1R2 = int(M1R2fourxoneC1)*int(M2R1onexfourC1)
							FARC2R2 = int(M1R2fourxoneC1)*int(M2R1onexfourC2)
							FARC3R2 = int(M1R2fourxoneC1)*int(M2R1onexfourC3)
							FARC4R2 = int(M1R2fourxoneC1)*int(M2R1onexfourC4)
							FARC1R3 = int(M1R3fourxoneC1)*int(M2R1onexfourC1)
							FARC2R3 = int(M1R3fourxoneC1)*int(M2R1onexfourC2)
							FARC3R3 = int(M1R3fourxoneC1)*int(M2R1onexfourC3)
							FARC4R3 = int(M1R3fourxoneC1)*int(M2R1onexfourC4)
							FARC1R4 = int(M1R4fourxoneC1)*int(M2R1onexfourC1)
							FARC2R4 = int(M1R4fourxoneC1)*int(M2R1onexfourC2)
							FARC3R4 = int(M1R4fourxoneC1)*int(M2R1onexfourC3)
							FARC4R4 = int(M1R4fourxoneC1)*int(M2R1onexfourC4)
							print("")
							print("["+str(FARC1R1)+" "+str(FARC2R1)+" "+str(FARC3R1)+" "+str(FARC4R1)+"]")
							print("["+str(FARC1R2)+" "+str(FARC2R2)+" "+str(FARC3R2)+" "+str(FARC4R2)+"]")
							print("["+str(FARC1R3)+" "+str(FARC2R3)+" "+str(FARC3R3)+" "+str(FARC4R3)+"]")
							print("["+str(FARC1R4)+" "+str(FARC2R4)+" "+str(FARC3R4)+" "+str(FARC4R4)+"]")
							print("")
					if Matrix1_size == "4x2":
						if Matrix2_size == "2x1":
							FAR1C1 = int(M1R1fourxtwoC1)*int(M2R1twoxoneC1)
							FAR1C2 = int(M1R1fourxtwoC2)*int(M2R2twoxoneC1)
							FAR2C1 = int(M1R2fourxtwoC1)*int(M2R1twoxoneC1)
							FAR2C2 = int(M1R2fourxtwoC2)*int(M2R2twoxoneC1)
							FAR3C1 = int(M1R3fourxtwoC1)*int(M2R1twoxoneC1)
							FAR3C2 = int(M1R3fourxtwoC2)*int(M2R2twoxoneC1)
							FAR4C1 = int(M1R4fourxtwoC1)*int(M2R1twoxoneC1)
							FAR4C2 = int(M1R4fourxtwoC2)*int(M2R2twoxoneC1)
							FAE1 = int(FAR1C1)+int(FAR1C2)
							FAE2 = int(FAR2C1)+int(FAR2C2)
							FAE3 = int(FAR3C1)+int(FAR3C2)
							FAE4 = int(FAR4C1)+int(FAR4C2)
							print("")
							print("["+str(FAE1)+"]")
							print("["+str(FAE2)+"]")
							print("["+str(FAE3)+"]")
							print("["+str(FAE4)+"]")
						if Matrix2_size == "2x2":
							FAR1C1 = int(M1R1fourxtwoC1)*int(M2R1twoxtwoC1)
							FAR1C2 = int(M1R1fourxtwoC2)*int(M2R2twoxtwoC1)
							FAR1aC1 = int(M1R1fourxtwoC1)*int(M2R1twoxtwoC2)
							FAR1aC2 = int(M1R1fourxtwoC2)*int(M2R2twoxtwoC2)
							FAR2C1 = int(M1R2fourxtwoC1)*int(M2R1twoxtwoC1)
							FAR2C2 = int(M1R2fourxtwoC2)*int(M2R2twoxtwoC1)
							FAR2bC1 = int(M1R2fourxtwoC1)*int(M2R1twoxtwoC2)
							FAR2bC2 = int(M1R2fourxtwoC2)*int(M2R2twoxtwoC2)
							FAR3C1 = int(M1R3fourxtwoC1)*int(M2R1twoxtwoC1)
							FAR3C2 = int(M1R3fourxtwoC2)*int(M2R2twoxtwoC1)
							FAR3cC1 = int(M1R3fourxtwoC1)*int(M2R1twoxtwoC2)
							FAR3cC2 = int(M1R3fourxtwoC2)*int(M2R2twoxtwoC2)
							FAR4C1 = int(M1R4fourxtwoC1)*int(M2R1twoxtwoC1)
							FAR4C2 = int(M1R4fourxtwoC2)*int(M2R2twoxtwoC1)
							FAR4dC1 = int(M1R4fourxtwoC1)*int(M2R1twoxtwoC2)
							FAR4dC2 = int(M1R4fourxtwoC2)*int(M2R2twoxtwoC2)
							FAE1 = int(FAR1C1)+int(FAR1C2)
							FAEa1 = int(FAR1aC1)+int(FAR1aC2)
							FAE2 = int(FAR2C1)+int(FAR2C2)
							FAEb2 = int(FAR2bC1)+int(FAR2bC2)
							FAE3 = int(FAR3C1)+int(FAR3C2)
							FAEc3 = int(FAR3cC1)+int(FAR3cC2)
							FAE4 = int(FAR4C1)+int(FAR4C2)
							FAEd4 = int(FAR4dC1)+int(FAR4dC2)
							print("")
							print("["+str(FAE1)+" "+str(FAEa1)+"]")
							print("["+str(FAE2)+" "+str(FAEb2)+"]")
							print("["+str(FAE3)+" "+str(FAEc3)+"]")
							print("["+str(FAE4)+" "+str(FAEd4)+"]")
						if Matrix2_size == "2x3":
							FAR1C1 = int(M1R1fourxtwoC1)*int(M2R1twoxthreeC1)
							FAR1C2 = int(M1R1fourxtwoC2)*int(M2R2twoxthreeC1)
							FAR1aC1 = int(M1R1fourxtwoC1)*int(M2R1twoxthreeC2)
							FAR1aC2 = int(M1R1fourxtwoC2)*int(M2R2twoxthreeC2)
							FAR1aAC1 = int(M1R1fourxtwoC1)*int(M2R1twoxthreeC3)
							FAR1aAC2 = int(M1R1fourxtwoC2)*int(M2R2twoxthreeC3)
							FAR2C1 = int(M1R2fourxtwoC1)*int(M2R1twoxthreeC1)
							FAR2C2 = int(M1R2fourxtwoC2)*int(M2R2twoxthreeC1)
							FAR2bC1 = int(M1R2fourxtwoC1)*int(M2R1twoxthreeC2)
							FAR2bC2 = int(M1R2fourxtwoC2)*int(M2R2twoxthreeC2)
							FAR2bBC1 = int(M1R2fourxtwoC1)*int(M2R1twoxthreeC3)
							FAR2bBC2 = int(M1R2fourxtwoC2)*int(M2R2twoxthreeC3)
							FAR3C1 = int(M1R3fourxtwoC1)*int(M2R1twoxthreeC1)
							FAR3C2 = int(M1R3fourxtwoC2)*int(M2R2twoxthreeC1)
							FAR3cC1 = int(M1R3fourxtwoC1)*int(M2R1twoxthreeC2)
							FAR3cC2 = int(M1R3fourxtwoC2)*int(M2R2twoxthreeC2)
							FAR3cCC1 = int(M1R3fourxtwoC1)*int(M2R1twoxthreeC3)
							FAR3cCC2 = int(M1R3fourxtwoC2)*int(M2R2twoxthreeC3)
							FAR4C1 = int(M1R4fourxtwoC1)*int(M2R1twoxthreeC1)
							FAR4C2 = int(M1R4fourxtwoC2)*int(M2R2twoxthreeC1)
							FAR4dC1 = int(M1R4fourxtwoC1)*int(M2R1twoxthreeC2)
							FAR4dC2 = int(M1R4fourxtwoC2)*int(M2R2twoxthreeC2)
							FAR4dDC1 = int(M1R4fourxtwoC1)*int(M2R1twoxthreeC3)
							FAR4dDC2 = int(M1R4fourxtwoC2)*int(M2R2twoxthreeC3)
							FAE1 = int(FAR1C1)+int(FAR1C2)
							FAEa1 = int(FAR1aC1)+int(FAR1aC2)
							FAEaA1 = int(FAR1aAC1)+int(FAR1aAC2)
							FAE2 = int(FAR2C1)+int(FAR2C2)
							FAEb2 = int(FAR2bC1)+int(FAR2bC2)
							FAEbB2 = int(FAR2bBC1)+int(FAR2bBC2)
							FAE3 = int(FAR3C1)+int(FAR3C2)
							FAEc3 = int(FAR3cC1)+int(FAR3cC2)
							FAEcC3 = int(FAR3cCC1)+int(FAR3cCC2)
							FAE4 = int(FAR4C1)+int(FAR4C2)
							FAEd4 = int(FAR4dC1)+int(FAR4dC2)
							FAEdD4 = int(FAR4dDC1)+int(FAR4dDC2)
							print("")
							print("["+str(FAE1)+" "+str(FAEa1)+" "+str(FAEaA1)+"]")
							print("["+str(FAE2)+" "+str(FAEb2)+" "+str(FAEbB2)+"]")
							print("["+str(FAE3)+" "+str(FAEc3)+" "+str(FAEcC3)+"]")
							print("["+str(FAE4)+" "+str(FAEd4)+" "+str(FAEdD4)+"]")
						if Matrix2_size == "2x4":
							FAR1C1 = int(M1R1fourxtwoC1)*int(M2R1twoxfourC1)
							FAR1C2 = int(M1R1fourxtwoC2)*int(M2R2twoxfourC1)
							FAR1aC1 = int(M1R1fourxtwoC1)*int(M2R1twoxfourC2)
							FAR1aC2 = int(M1R1fourxtwoC2)*int(M2R2twoxfourC2)
							FAR1aAC1 = int(M1R1fourxtwoC1)*int(M2R1twoxfourC3)
							FAR1aAC2 = int(M1R1fourxtwoC2)*int(M2R2twoxfourC3)
							FAR1aAAC1 = int(M1R1fourxtwoC1)*int(M2R1twoxfourC4)
							FAR1aAAC2 = int(M1R1fourxtwoC2)*int(M2R2twoxfourC4)
							FAR2C1 = int(M1R2fourxtwoC1)*int(M2R1twoxfourC1)
							FAR2C2 = int(M1R2fourxtwoC2)*int(M2R2twoxfourC1)
							FAR2bC1 = int(M1R2fourxtwoC1)*int(M2R1twoxfourC2)
							FAR2bC2 = int(M1R2fourxtwoC2)*int(M2R2twoxfourC2)
							FAR2bBC1 = int(M1R2fourxtwoC1)*int(M2R1twoxfourC3)
							FAR2bBC2 = int(M1R2fourxtwoC2)*int(M2R2twoxfourC3)
							FAR2bBBC1 = int(M1R2fourxtwoC1)*int(M2R1twoxfourC4)
							FAR2bBBC2 = int(M1R2fourxtwoC2)*int(M2R2twoxfourC4)
							FAR3C1 = int(M1R3fourxtwoC1)*int(M2R1twoxfourC1)
							FAR3C2 = int(M1R3fourxtwoC2)*int(M2R2twoxfourC1)
							FAR3cC1 = int(M1R3fourxtwoC1)*int(M2R1twoxfourC2)
							FAR3cC2 = int(M1R3fourxtwoC2)*int(M2R2twoxfourC2)
							FAR3cCC1 = int(M1R3fourxtwoC1)*int(M2R1twoxfourC3)
							FAR3cCC2 = int(M1R3fourxtwoC2)*int(M2R2twoxfourC3)
							FAR3cCCC1 = int(M1R3fourxtwoC1)*int(M2R1twoxfourC4)
							FAR3cCCC2 = int(M1R3fourxtwoC2)*int(M2R2twoxfourC4)
							FAR4C1 = int(M1R4fourxtwoC1)*int(M2R1twoxfourC1)
							FAR4C2 = int(M1R4fourxtwoC2)*int(M2R2twoxfourC1)
							FAR4dC1 = int(M1R4fourxtwoC1)*int(M2R1twoxfourC2)
							FAR4dC2 = int(M1R4fourxtwoC2)*int(M2R2twoxfourC2)
							FAR4dDC1 = int(M1R4fourxtwoC1)*int(M2R1twoxfourC3)
							FAR4dDC2 = int(M1R4fourxtwoC2)*int(M2R2twoxfourC3)
							FAR4dDDC1 = int(M1R4fourxtwoC1)*int(M2R1twoxfourC4)
							FAR4dDDC2 = int(M1R4fourxtwoC2)*int(M2R2twoxfourC4)
							FAE1 = int(FAR1C1)+int(FAR1C2)
							FAEa1 = int(FAR1aC1)+int(FAR1aC2)
							FAEaA1 = int(FAR1aAC1)+int(FAR1aAC2)
							FAEaAA1 = int(FAR1aAAC1)+int(FAR1aAAC2)
							FAE2 = int(FAR2C1)+int(FAR2C2)
							FAEb2 = int(FAR2bC1)+int(FAR2bC2)
							FAEbB2 = int(FAR2bBC1)+int(FAR2bBC2)
							FAEbBB2 = int(FAR2bBBC1)+int(FAR2bBBC2)
							FAE3 = int(FAR3C1)+int(FAR3C2)
							FAEc3 = int(FAR3cC1)+int(FAR3cC2)
							FAEcC3 = int(FAR3cCC1)+int(FAR3cCC2)
							FAEcCC3 = int(FAR3cCCC1)+int(FAR3cCCC2)
							FAE4 = int(FAR4C1)+int(FAR4C2)
							FAEd4 = int(FAR4dC1)+int(FAR4dC2)
							FAEdD4 = int(FAR4dDC1)+int(FAR4dDC2)
							FAEdDD4 = int(FAR4dDDC1)+int(FAR4dDDC2)
							print("")
							print("["+str(FAE1)+" "+str(FAEa1)+" "+str(FAEaA1)+" "+str(FAEaAA1)+"]")
							print("["+str(FAE2)+" "+str(FAEb2)+" "+str(FAEbB2)+" "+str(FAEbBB2)+"]")
							print("["+str(FAE3)+" "+str(FAEc3)+" "+str(FAEcC3)+" "+str(FAEcCC3)+"]")
							print("["+str(FAE4)+" "+str(FAEd4)+" "+str(FAEdD4)+" "+str(FAEdDD4)+"]")	
					if Matrix1_size == "4x3":
						if Matrix2_size == "3x1":
							if Matrix2_size == "3x2":
								if Matrix2_size == "3x3":
									if Matrix2_size == "3x4":
										print("")
					if Matrix1_size == "1x4":
						if Matrix2_size == "4x1":
							if Matrix2_size == "4x2":
								if Matrix2_size == "4x3":
									if Matrix2_size == "4x4":
										print("")
					if Matrix1_size == "2x4":
						if Matrix2_size == "4x1":
							if Matrix2_size == "4x2":
								if Matrix2_size == "4x3":
									if Matrix2_size == "4x4":
										print("")
					if Matrix1_size == "3x4":
						if Matrix2_size == "4x1":
							if Matrix2_size == "4x2":
								if Matrix2_size == "4x3":
									if Matrix2_size == "4x4":
										print("")					
					if Matrix1_size == "4x4":
						if Matrix2_size == "4x1":
							FAR1C1 = int(M1R1fourxfourC1)*int(M2R1fourxoneC1)
							FAR1C2 = int(M1R1fourxfourC2)*int(M2R2fourxoneC1)
							FAR1C3 = int(M1R1fourxfourC3)*int(M2R3fourxoneC1)
							FAR1C4 = int(M1R1fourxfourC4)*int(M2R4fourxoneC1)
							FAR2C1 = int(M1R2fourxfourC1)*int(M2R1fourxoneC1)
							FAR2C2 = int(M1R2fourxfourC2)*int(M2R2fourxoneC1)
							FAR2C3 = int(M1R2fourxfourC3)*int(M2R3fourxoneC1)
							FAR2C4 = int(M1R2fourxfourC4)*int(M2R4fourxoneC1)
							FAR3C1 = int(M1R3fourxfourC1)*int(M2R1fourxoneC1)
							FAR3C2 = int(M1R3fourxfourC2)*int(M2R2fourxoneC1)
							FAR3C3 = int(M1R3fourxfourC3)*int(M2R3fourxoneC1)
							FAR3C4 = int(M1R3fourxfourC4)*int(M2R4fourxoneC1)
							FAR4C1 = int(M1R4fourxfourC1)*int(M2R1fourxoneC1)
							FAR4C2 = int(M1R4fourxfourC2)*int(M2R2fourxoneC1)
							FAR4C3 = int(M1R4fourxfourC3)*int(M2R3fourxoneC1)
							FAR4C4 = int(M1R4fourxfourC4)*int(M2R4fourxoneC1)
							FAER1 = int(FAR1C1)+int(FAR1C2)+int(FAR1C3)+int(FAR1C4)
							FAER2 = int(FAR2C1)+int(FAR2C2)+int(FAR2C3)+int(FAR2C4)
							FAER3 = int(FAR3C1)+int(FAR3C2)+int(FAR3C3)+int(FAR3C4)
							FAER4 = int(FAR4C1)+int(FAR4C2)+int(FAR4C3)+int(FAR4C4)
							print("")
							print("["+str(FAER1)+"]")
							print("["+str(FAER2)+"]")
							print("["+str(FAER3)+"]")
							print("["+str(FAER4)+"]")
							if Matrix2_size == "4x2":
								if Matrix2_size == "4x3":
									if Matrix2_size == "4x4":
										print("")
					print("")
					print("")
					maAgain = input("Again? Y or N: ").lower()
					if maAgain == "y":
						print("")
						print("")
						print("")
						a = True
					if maAgain == "n":
						a = False
						sys.exit()
	print("")												
	n1=float(input("Enter the first number: "))
	time.sleep(.45)
	if n1 == "":
		sys.exit()
	print("")
	n2=float(input("Enter the second number: "))
	time.sleep(.45)
	print("")
	if n2 == "":
		sys.exit()
	elif calculator_machine =="a":
		output=n1+n2
	elif calculator_machine =="s":
		output=n1-n2
	elif calculator_machine =="m":
		output=n1*n2
	elif calculator_machine =="d":
		output=n1/n2
	print("")
	print("")
	print("")
	print("Calculator Output: "+str(output))
	print("")
	print("________________________________________________________________________________________________________")
	print("")
	again_Time()
