from fastmcp import FastMCP

mcp = FastMCP("Car Store")

car_data = {
    "tata": {
        "punch": {"price": 600000, "fuel": "Petrol"},
        "nexon": {"price": 800000, "fuel": "Petrol"},
        "harrier": {"price": 1500000, "fuel": "Diesel"},
        "safari": {"price": 1600000, "fuel": "Diesel"}
    },
    "mahindra": {
        "bolero": {"price": 1000000, "fuel": "Diesel"},
        "xuv": {"price": 1300000, "fuel": "Diesel"},
        "thar": {"price": 1100000, "fuel": "Petrol"}
    },
    "toyota": {
        "innova": {"price": 1900000, "fuel": "Diesel"},
        "fortuner": {"price": 3500000, "fuel": "Diesel"},
        "camry": {"price": 4500000, "fuel": "Hybrid"}
    },
    "honda": {
        "city": {"price": 1200000, "fuel": "Petrol"},
        "amaze": {"price": 800000, "fuel": "Petrol"}
    },
    "hyundai": {
        "venue": {"price": 800000, "fuel": "Petrol"},
        "creta": {"price": 1100000, "fuel": "Petrol"}
    },
    "maruti suzuki": {
        "alto": {"price": 400000, "fuel": "Petrol"},
        "baleno": {"price": 700000, "fuel": "Petrol"}
    },
    "bmw": {
        "x1": {"price": 5000000, "fuel": "Petrol"},
        "x3": {"price": 7000000, "fuel": "Diesel"}
    },
    "kia": {
        "seltos": {"price": 1100000, "fuel": "Petrol"},
        "sonet": {"price": 800000, "fuel": "Diesel"}
    },
    "mg": {
        "hector": {"price": 1400000, "fuel": "Petrol"},
        "zs": {"price": 1800000, "fuel": "Electric"}
    }
}

@mcp.tool()
def cars_models():
    '''Gives all available cars'''
    return list(car_data.keys())

@mcp.tool()
def cars_available():
    '''this is car models available'''
    return car_data

@mcp.tool()
def get_models_by_brand(brand: str):
    """Get all car models belonging to a specific brand."""
    brand = brand.lower().strip()

    if brand not in car_data:
        return {"error": f"Brand '{brand}' not found"}

    return {
        "brand": brand,
        "models": list(car_data[brand].keys())
    }    

@mcp.tool()
def search_car(model: str):
    """Search for a car using its model name."""
    model = model.lower().strip()

    for brand, models in car_data.items():
        if model in models:
            return {
                "brand": brand,
                "model": model,
                **models[model]
            }

    return {"error": f"Car model '{model}' not found"}

@mcp.tool()
def get_car_price(model: str):
    """Get the sample price of a specific car."""
    result = search_car(model)

    if "error" in result:
        return result

    return {
        "model": result["model"],
        "price_inr": result["price"],
        "currency": "INR"
    }


if __name__=='__main__':
    mcp.run(transport = 'streamable-http',port = 5001 , host = '0.0.0.0')