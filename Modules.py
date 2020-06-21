import Converter_For_Modules  # modules can be imported only when they dont lie in same package ----- syntax1
from Converter_For_Modules import lbs_kg  # ctrl+space to know the list of functions in converters ---- syntax2
import Utils  # syntax3

print(Converter_For_Modules.kg_lbs(30))
print("...............................")

# syntax 2

print(lbs_kg(120))
print("...............................")

# exercise from mosh


a = list(map(int, input().split()))
print(Utils.find_max(a))
# remove list1 from utils before executing Modules
# as it will be executed twice for list1 and a
