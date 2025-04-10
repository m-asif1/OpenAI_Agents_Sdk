import asyncio

async def bake_lasagna():
    print("Cook: Putting lasagna in the oven...")
    # Simulate a slow task (like baking) with asyncio.sleep
    await asyncio.sleep(3)  
    print("Cook: Lasagna is done baking!")
    return "baked lasagna"

async def chop_veggies():
    print("Cook: Starting to chop vegetables for the salad...")
    # Simulate chopping time with asyncio.sleep
    await asyncio.sleep(2)  
    print("Cook: Finished chopping vegetables!")
    return "chopped veggies"

async def prepare_meal():
    # Start baking the lasagna (this begins the slow task)
    baking_task = asyncio.create_task(bake_lasagna())
    
    # While the lasagna is baking, start chopping veggies.
    veggies = await chop_veggies()
    
    # Now wait for the lasagna to finish baking.
    lasagna = await baking_task
    
    # Assemble the meal using both results.
    print(f"Cook: Assembling the meal with {lasagna} and {veggies}.")

if __name__ == "__main__":
    asyncio.run(prepare_meal())