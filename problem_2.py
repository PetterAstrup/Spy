# PROBLEM 2 — Fiber vs. Copper Cost
# Goal: For each region, decide whether to switch from copper to fiber
# based on operating cost and feasibility.

# 1) Input data

# Regions: each is a small "record" with all info.
regions = [
    {"name": "Alpha",   "length": 120, "incidents": 30, "terrain": "low",    "permit": True},
    {"name": "Beta",    "length": 200, "incidents": 45, "terrain": "medium", "permit": False},
    {"name": "Gamma",   "length": 150, "incidents": 60, "terrain": "high",   "permit": True},
    {"name": "Delta",   "length": 90,  "incidents": 20, "terrain": "medium", "permit": True},
    {"name": "Epsilon", "length": 300, "incidents": 90, "terrain": "high",   "permit": False}
]

# Cost model per year
# maint_cost = NOK per km per year
# incident_cost = NOK per incident
copper = {"maint_cost": 300, "incident_cost": 500}
fiber  = {"maint_cost": 100, "incident_cost": 100}

# Terrain multipliers
terrain_multiplier = {"low": 1.0, "medium": 1.2, "high": 1.5}


# 2) Total annual cost
def total_cost(length_km, incidents, maint_cost, incident_cost, terrain):
    """
    Compute total annual operating cost:
      (length * maint_cost * terrain_multiplier) + (incidents * incident_cost)
    """
    mult = terrain_multiplier[terrain]
    return (length_km * maint_cost * mult) + (incidents * incident_cost)


# 3) Main loop: evaluate each region
for region in regions:
    # Naming region data into short variable names 
    name      = region["name"]
    length    = region["length"]
    incidents = region["incidents"]
    terrain   = region["terrain"]
    permit    = region["permit"]

    # Copper cost is defined
    copper_cost = total_cost
    (length, incidents,
    copper["maint_cost"], copper["incident_cost"],
    terrain)

    
    # Fiber is not feasible only if terrain is "high" and permit is False.
    if terrain == "high" and not permit:
        fiber_feasible = False
        fiber_cost = "N/A"
        savings    = "N/A"
        recommendation = "Fiber Not Feasible"
    else:
        fiber_feasible = True
        fiber_cost = total_cost(length, incidents,
        fiber["maint_cost"], fiber["incident_cost"],
        terrain)
      
        savings = copper_cost - fiber_cost
        if savings > 0:
            recommendation = "Switch to Fiber"
        else:
            recommendation = "Stay on Copper"

    # 4) Output
    print(f"Region: {name}")
    print(f"Terrain: {terrain}")
    print(f"Permit Approved: {permit}")
    print(f"Fiber Feasible?: {fiber_feasible}")
    print(f"Copper Cost: NOK {copper_cost}")
    print(f"Fiber Cost: NOK {fiber_cost}")
    print(f"Savings: NOK {savings}")
    print(f"Recommendation: {recommendation}")
    print("-" * 40)  # visual divider line in the output
