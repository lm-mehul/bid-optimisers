# bid-optimisers
bid-optimisers - To bid or not to bid

# Install dependencies : 
pip install -r requirements.txt


# API specs : 

Request : 

curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
    "pub_id": "123",
    "ad_unit_id": "456",
    "ad_type_id": "789",
    "platform_id": "2",
    "country": "US",
    "make": "Apple",
    "model": "iPhone",
    "dsp_id": "10",
    "tmax": 200,
    "schain_length": 3,
    "day_of_week": 4,
    "hour_of_day": 15
}'


Response : 

