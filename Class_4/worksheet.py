# # Q15
# score = 55
# attendance = 80
# print(score >= 40 and attendance >= 75)

# # Q16
# print(True and False)
# print(True or False)
# print(not True)
# print((5 > 3) and (2 > 4))

# # Q17
# print(bool(0), bool(0.0), bool(""), bool(None))
# print(bool(5), bool("hi"), bool(-1))

# # Q18
# print(0 or 5)
# print("" or "hi")
# print(3 and 7)
# print(0 and 7)

# # Q19
# name = ""
# print(name or "Guest")
# name = "Asha"
# print(name or "Guest")

# #Q20
# print(True or False and False)


# #Q22
# # ── driver_dispatch.py (RideSurge Technologies · Core Dispatch Module) ──
# # Business rules (Ops Manual v5.1):
# # Rule A: Driver can accept a PREMIUM ride ONLY IF all three hold:
# # rating >= 4.7 AND trips_completed >= 200 AND car_type == "sedan"
# # Rule B: SURGE pricing fires when the rider/driver ratio is AT LEAST 3 (>= 3)
# # AND it is currently raining.
# # Rule C: FREE-RIDE coupon issued when customer is a new user AND at least one
# # of: (referral code used) OR (promo is active).
# # Existing users are NOT eligible, even if a promo is running.
# driver_rating = 4.8
# trips_completed = 150 # below the required 200-trip threshold
# car_type = "sedan"
# active_riders = 114 # exactly 3 times active_drivers
# active_drivers = 38
# rain = True
# is_new_user = False # this is a returning customer, not a new one
# referral_code = ""
# promo_active = True
# # Rule A — Premium ride eligibility
# can_take_premium = driver_rating >= 4.7 or trips_completed >= 200 or car_type == "sedan"
# # Rule B — Surge pricing
# surge_active = (active_riders / active_drivers) > 3 and rain == True
# # Rule C — Free-ride coupon
# free_ride_coupon = is_new_user and referral_code != "" or promo_active
# print("Premium eligible:", can_take_premium)
# print("Surge active: ", surge_active)
# print("Free ride coupon:", free_ride_coupon)

# #Q23
# print(2 + 3)
# print("2" + "3")

# #Q24
# print("Hello" + ", " + "World!")
# print("ha" * 3)
# print("-" * 30)
# print(type("ha" * 3))

# #Q25
# print("hello" - "ello")
# print("hello" / 2)

# #Q26
# print("123" + 4)
# print("123" == 4)

# #Q27
# print([1, 2] + [3, 4])
# print([1, 2] * 3)

# #Q29
# print(bin(13))
# print(bin(255))

# #Q30
# print(int("1010", 2))
# print(int("11111", 2))

# print(bin(42)) # base 2
# print(oct(42)) # base 8
# print(hex(42)) # base 16
# print(int("101010", 2)) # binary string -> decimal
# print(int("52", 8)) # octal string -> decimal
# print(int("2a", 16)) # hex string -> decimal



# # to check odd or even
# x = int(input("Number checked by bit wise operator. Enter Your number:"))
# if x&1 == 0:
#     print("Even")
# else:
#     print("Odd")

# READ = 0b100 # 4
# WRITE = 0b010 # 2
# EXECUTE = 0b001 # 1
# perms = READ | WRITE # user can read and write, but not execute
# print(bin(perms))
# print(bool(perms & READ)) # can the user read?
# print(bool(perms & EXECUTE)) # can the user execute?


# print(0.1 + 0.2)
# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2 == 0.30000000000000004)
# print(f"{1/3:.3f}")
# print(bin(1))


# import sys
# print(sys.float_info.dig) # significant decimal digits of precision
# print(sys.float_info.max) # largest representable float

# print(f"{0.1:.20f}")
# print(f"{0.2:.20f}")
# print(f"{0.3:.20f}")
# print(f"{0.1 + 0.2:.20f}")

print(0.1 + 0.2 == 0.3) # direct ==
print(round(0.1 + 0.2, 1) == 0.3) # round first
import math
print(math.isclose(0.1 + 0.2, 0.3)) # tolerance-based