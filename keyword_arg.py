def cheeseshop(kind, *args, **keywords):
   print("-- Do you have any", kind, "?")
   print("-- I'm sorry, we are all out of ", kind)
   for arg in args:
      print(arg)
   print("-" * 40)
   keys = sorted(keywords.keys())
   for key in keys:
      print(key, ":", keywords[key])


cheeseshop("Limburger", "It's very runny, Sir.",
           "It's really very very runny, Sir.",
           shopkeeper = "Shilpa Sherigar",
           client = "Jatheen Anand",
           sketch = "Cheese cake factory")
