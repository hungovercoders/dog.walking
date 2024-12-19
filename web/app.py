import streamlit as st
import requests

API_URL = "http://localhost:8080/dogs"

VALID_BREEDS = [
    "Afghan Hound", "Airedale Terrier", "Akita", "Alaskan Malamute", "Australian Shepherd",
    "Basenji", "Beagle", "Belgian Malinois", "Belgian Sheepdog", "Belgian Tervuren",
    "Bernese Mountain Dog", "Bichon Frise", "Bloodhound", "Border Collie", "Borzoi",
    "Boston Terrier", "Bouvier des Flandres", "Boxer", "Briard", "Brittany",
    "Brussels Griffon", "Bull Terrier", "Bullmastiff", "Cairn Terrier", "Cardigan Welsh Corgi",
    "Cavalier King Charles Spaniel", "Chesapeake Bay Retriever", "Chihuahua", "Chinese Crested",
    "Chinese Shar-Pei", "Clumber Spaniel", "Cocker Spaniel", "Curly-Coated Retriever",
    "Dachshund", "Dalmatian", "Doberman Pinscher", "English Cocker Spaniel", "English Foxhound",
    "English Setter", "English Springer Spaniel", "French Bulldog", "German Shepherd",
    "Golden Retriever", "Gordon Setter", "Great Dane", "Havanese", "Irish Setter",
    "Irish Wolfhound", "Italian Greyhound", "Japanese Chin", "Keeshond", "Komondor",
    "Kuvasz", "Lakeland Terrier", "Labrador Retriever", "Leonberger", "Lhasa Apso",
    "Maltese", "Manchester Terrier", "Miniature Schnauzer", "Neapolitan Mastiff", "Newfoundland",
    "Norfolk Terrier", "Norwich Terrier", "Papillon", "Pembroke Welsh Corgi", "Petit Basset Griffon Vendeen",
    "Pharaoh Hound", "Plott", "Pointer", "Polish Lowland Sheepdog", "Pomeranian",
    "Poodle", "Portuguese Water Dog", "Pug", "Puli", "Redbone Coonhound",
    "Rhodesian Ridgeback", "Rottweiler", "Saint Bernard", "Saluki", "Samoyed",
    "Schipperke", "Scottish Deerhound", "Scottish Terrier", "Sealyham Terrier", "Setter",
    "Shetland Sheepdog", "Shiba Inu", "Shih Tzu", "Siberian Husky", "Silky Terrier",
    "Skye Terrier", "Sloughi", "Soft Coated Wheaten Terrier", "Staffordshire Bull Terrier",
    "Standard Schnauzer", "Sussex Spaniel", "Swedish Vallhund", "Tibetan Mastiff", "Tibetan Spaniel",
    "Tibetan Terrier", "Toy Fox Terrier", "Treeing Walker Coonhound", "Vizsla", "Weimaraner",
    "Welsh Corgi", "West Highland White Terrier", "Whippet", "Wirehaired Pointing Griffon",
    "Xoloitzcuintli", "Yorkshire Terrier"
]

st.title("Dog Walker API")

# Add a new dog profile
st.header("Add a New Dog Profile")
name = st.text_input("Name")
sex = st.selectbox("Sex", ["Male", "Female"])
year_of_birth = st.number_input("Year of Birth", min_value=2000, max_value=2025, step=1)
breed = st.multiselect("Breed", VALID_BREEDS)
notes = st.text_area("Notes (optional)")

if st.button("Add Dog"):
    dog_data = {
        "name": name,
        "sex": sex,
        "yearOfBirth": year_of_birth,
        "breed": breed,
        "notes": notes
    }
    response = requests.post(API_URL, json=dog_data)
    if response.status_code == 201:
        st.success("Dog added successfully!")
    else:
        st.error(f"Error: {response.json().get('error')}")

# List all dog profiles
st.header("List All Dog Profiles")
if st.button("Get All Dogs"):
    response = requests.get(API_URL)
    if response.status_code == 200:
        dogs = response.json().get("data", {}).get("dogs", [])
        if dogs:
            st.table(dogs)
        else:
            st.write("No dogs found.")
    else:
        st.error(f"Error: {response.json().get('error')}")

# Get details for a specific dog profile
st.header("Get Dog Details")
dog_id = st.text_input("Dog ID")
if st.button("Get Dog Details"):
    response = requests.get(f"{API_URL}/{dog_id}")
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.json().get('error')}")

# Update a dog profile
st.header("Update Dog Profile")
update_dog_id = st.text_input("Dog ID to Update")
update_name = st.text_input("New Name")
update_sex = st.selectbox("New Sex", ["Male", "Female"])
update_year_of_birth = st.number_input("New Year of Birth", min_value=2000, max_value=2025, step=1)
update_breed = st.multiselect("Breed", VALID_BREEDS)
update_notes = st.text_area("New Notes (optional)")

if st.button("Update Dog"):
    update_dog_data = {
        "name": update_name,
        "sex": update_sex,
        "yearOfBirth": update_year_of_birth,
        "breed": update_breed,
        "notes": update_notes
    }
    response = requests.put(f"{API_URL}/{update_dog_id}", json=update_dog_data)
    if response.status_code == 200:
        st.success("Dog updated successfully!")
    else:
        st.error(f"Error: {response.json().get('error')}")

# Delete a dog profile
st.header("Delete Dog Profile")
delete_dog_id = st.text_input("Dog ID to Delete")
if st.button("Delete Dog"):
    response = requests.delete(f"{API_URL}/{delete_dog_id}")
    if response.status_code == 204:
        st.success("Dog deleted successfully!")
    else:
        st.error(f"Error: {response.json().get('error')}")