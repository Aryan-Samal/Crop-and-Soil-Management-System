import random

class CropSelection:
    def __init__(self, soil_type, climate):
        self.soil_type = soil_type
        self.climate = climate
    
    def recommend_crop(self):
        if self.soil_type == "loamy" and self.climate == "temperate":
            return "Wheat"
        elif self.soil_type == "clay" and self.climate == "tropical":
            return "Rice"
        else:
            return "Corn"
class SoilManagement:
    def __init__(self, soil_ph, nutrient_levels):
        self.soil_ph = soil_ph
        self.nutrient_levels = nutrient_levels
    
    def recommend_fertilizer(self):
        if self.soil_ph < 6.5:
            return "Apply lime to increase pH"
        elif self.nutrient_levels['nitrogen'] < 10:
            return "Apply nitrogen-based fertilizer"
        else:
            return "No fertilizer needed"


class DiseaseIdentification:
    def identify_disease(self, image_path):

        diseases = ["Blight", "Rust", "Mosaic"]
        return random.choice(diseases)

class WeatherMonitoring:
    def get_weather_forecast(self):

        forecast = {
            "temperature": "25°C",
            "humidity": "80%",
            "precipitation": "20%"
        }
        return forecast

class RecommendationSystem:
    def __init__(self, crop_selection, soil_management, weather_monitoring, disease_identification):
        self.crop_selection = crop_selection
        self.soil_management = soil_management
        self.weather_monitoring = weather_monitoring
        self.disease_identification = disease_identification
    
    def run_recommendations(self):
        crop = self.crop_selection.recommend_crop()
        fertilizer = self.soil_management.recommend_fertilizer()
        weather = self.weather_monitoring.get_weather_forecast()
        disease = self.disease_identification.identify_disease("path/to/image.jpg")
        
        recommendations = {
            "Crop Recommendation": crop,
            "Fertilizer Recommendation": fertilizer,
            "Weather Forecast": weather,
            "Disease Identified": disease
        }
        return recommendations

def main():

    soil_type = input("Enter soil type (e.g., loamy, clay, sandy): ").strip().lower()
    climate = input("Enter climate (e.g., temperate, tropical, arid): ").strip().lower()
    
    soil_ph = float(input("Enter soil pH value (e.g., 6.5): "))
    
    nitrogen = float(input("Enter nitrogen level (in mg/kg): "))
    phosphorus = float(input("Enter phosphorus level (in mg/kg): "))
    potassium = float(input("Enter potassium level (in mg/kg): "))
    nutrient_levels = {"nitrogen": nitrogen, "phosphorus": phosphorus, "potassium": potassium}
    
    crop_selection = CropSelection(soil_type, climate)
    soil_management = SoilManagement(soil_ph, nutrient_levels)
    weather_monitoring = WeatherMonitoring()
    disease_identification = DiseaseIdentification()
    
    recommendation_system = RecommendationSystem(crop_selection, soil_management, weather_monitoring, disease_identification)
    recommendations = recommendation_system.run_recommendations()
    
    print("\n--- Recommendations ---")
    for key, value in recommendations.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()