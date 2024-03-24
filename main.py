import streamlit as st
import tensorflow as tf
import numpy as np

#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

def Apple___Apple_scab():
    prevention=("""
                Improve air circulation: Prune trees to allow sunlight and air to penetrate the canopy\n
                Sanitation: Remove fallen leaves and fruit in autumn to reduce fungal spore harborage\n
                Watering: Water early in the morning to allow leaves to dry quickly. Avoid overhead watering\n
                """)
    treatment=("""
               Fungicides: Use sulfur-based fungicides, neem oil, or strobilurins once symptoms appear\n
               Organic options: Consider baking soda or potassium bicarbonate sprays for organic management\n
               """)
    st.header("affect by:")
    st.image("pest image\AppleScab.jpg")
    st.header("prevention:")
    st.write(prevention)
    st.header("treatment:")
    return(treatment)

def Apple___Black_rot():
    prevention1=("""
                Pruning: Regularly prune trees to improve air circulation and allow sunlight penetration.\n
                Sanitation: Remove and destroy infected branches, cankers and fallen fruits. These harbor fungal spores that contribute to future infections.\n
                Wound care: Properly prune and treat any wounds on the tree with a fungicide-based wound dressing to prevent fungal entry.\n
                Mulch: Apply a layer of organic mulch around the base of the tree to suppress weed growth and maintain soil moisture\n
                """)
    treatment1=("""
                Fungicides: Apply fungicides containing copper or chlorothalonil early in the season before symptoms appear for preventative control.\n
                Remove infected fruit: Promptly remove and destroy any infected fruits to prevent further spread of the disease.\n
                Fruit thinning: Thin developing fruits on heavily fruiting trees to improve air circulation and reduce humidity, which favors fungal growth.\n
                """)
    st.header("affect by:")
    st.write("aphids")
    st.image("pest image\Apple balck rot.jpeg")
    st.header("prevention:")
    st.write(prevention1)
    st.header("treatment:")
    return(treatment1)

def Apple___Cedar_apple_rust():
    prevention2=("""
                Break the cycle: Since cedar-apple rust requires both junipers (eastern red cedar) and apple trees to complete its life cycle, consider removing one from the vicinity. Removing junipers within 1-2 miles is ideal, but even a shorter distance can help.\n
                Resistant apple varieties: Choose apple varieties with known resistance to cedar-apple rust, such as Enterprise, Freedom, Liberty, or Gala.\n
                Proper sanitation: Rake and remove fallen leaves from both apple trees and junipers in autumn to reduce fungal spore harborage.\n
                """)
    treatment2=("""
                Fungicides: Once orange spots appear on apple leaves, apply fungicides containing copper or myclobutanil.Note: Effectiveness is limited once symptoms appear.\n
                Pruning: Prune and remove heavily infected branches on both apple trees and junipers to reduce fungal spore production.\n
                """)
    st.header("affect by:")
    st.write("Scales")
    st.image("pest image\Apple cedar and rust.jpeg")
    st.header("prevention:")
    st.write(prevention2)
    st.header("treatment:")
    return(treatment2)

def Cherry___Powdery_mildew():
    prevention3=("""
                Weed control: Control weeds around the base of the tree to improve air circulation and reduce humidity.\n
                Avoid excessive nitrogen fertilizer: Excess nitrogen can make trees more susceptible to powdery mildew.\n
                Dormant oil: Apply dormant oil sprays in late winter to smother overwintering fungal spores.\n
                Sulfur fungicides: Apply preventative sulfur fungicides early in the growing season before buds open.\n
                """)
    treatment3=("""
            Fungicides: Once powdery mildew is observed, apply fungicides containing sulfur, neem oil, or potassium bicarbonate.\n
            Heavy infection: For severe cases, consider stronger fungicides containing copper or strobilurins, but use them judiciously to avoid resistance development.\n
            Pruning: Prune and remove heavily infected branches to reduce fungal spore production and improve air circulation.\n
            """)
    st.header("affect by:")
    st.write("Thrips")
    st.image("pest image\Cherry.jpeg")
    st.header("prevention:")
    st.write(prevention3)
    st.header("treatment:")
    return(treatment3)

def Corn___Cercospora_leaf_spot_Gray_leaf_spot():
    prevention4=("""
                Crop rotation: Practice crop rotation with non-susceptible crops like soybeans or small grains to reduce fungal inoculum in the soil.\n
                Tillage practices: Tillage can help bury crop residue where fungal spores overwinter, reducing their survival and spread to the next season. However, consider minimal tillage practices to conserve soil health.\n
                Balanced fertilization: Ensure balanced fertilization with adequate potassium but avoid excessive nitrogen, which can worsen GLS.\n
                Residue management: Shred or chop corn stalks after harvest to promote faster decomposition and reduce fungal spore survival on crop residue.\n
                """)
    treatment4=("""
                Fungicides: Apply fungicides containing chlorothalonil or strobilurins only when necessary, following scouting and reaching specific disease thresholds. Fungicide overuse can lead to resistance development.\n
                Scouting: Regularly monitor your cornfields for signs of GLS, especially during warm, humid weather when the disease is most prevalent.\n
                """)
    st.header("affect by:")
    st.write("Leafhopper")
    st.image("pest image\Corn grey leaf.jpeg")
    st.header("prevention:")
    st.write(prevention4)
    st.header("treatment:")
    return(treatment4)

def Corn___Common_rust():
    prevention5=("""
                Crop rotation: Practice crop rotation with non-susceptible crops like soybeans or small grains to reduce fungal inoculum (spores) in the soil.\n
                Balanced fertilization: Ensure balanced fertilization with adequate potassium but avoid excessive nitrogen, which can worsen GLS.\n
                Scouting: Regularly monitor your cornfields, especially during warm, humid weather, when the disease is most prevalent.\n
                """)
    treatment5=("""
                Fungicides: Apply fungicides containing chlorothalonil or strobilurins only when necessary, following scouting and reaching specific disease thresholds. Fungicide overuse can lead to resistance development.\n
                Early intervention: If fungal pustules are observed early, fungicide application might be more effective than at later stages.\n
                Weather monitoring: Be more vigilant during periods of warm (around 75-80°F) and humid weather (over 80% humidity) as these conditions favor common rust development.\n
                """)
    st.header("affect by:")
    st.write("Bettle")
    st.image("pest image\Corn comon rust.jpeg")
    st.header("prevention:")
    st.write(prevention5)
    st.header("treatment:")
    return(treatment5)

def Corn___Northern_Leaf_Blight():
    prevention6=("""
                Resistant hybrids: The most crucial step is choosing corn varieties known for resistance to Northern Leaf Blight (NLB). Consult seed suppliers or agricultural extension services for recommendations in your region.\n
                Crop rotation: Practice crop rotation with non-susceptible crops like soybeans or small grains to reduce fungal inoculum (spores) in the soil.\n
                Balanced fertilization: Ensure balanced fertilization with adequate potassium and avoid excessive nitrogen, which can worsen NLB severity.\n
                Volunteer corn control: Eliminate volunteer corn plants emerging after harvest, as they can harbor the fungus and act as a source of infection for the next season's crop.\n
                """)
    treatment6=("""
                Fungicides: Apply fungicides containing chlorothalonil or strobilurins only when necessary, following scouting and reaching specific disease thresholds. Fungicide overuse can lead to resistance development.\n
                Scouting: Regularly monitor your cornfields, especially during cool, wet weather when the disease is most prevalent. Look for large, grayish-green lesions on leaves.\n
                """)
    st.header("affect by:")
    st.write("thrips")
    st.image("pest image\Cherry.jpeg")
    st.header("prevention:")
    st.write(prevention6)
    st.header("treatment:")
    return(treatment6)

def Grape___Black_rot():
    prevention7=("""
                Resistant varieties: Choose grape varieties with known resistance to black rot, like Concord, Niagara, or Jupiter\n
                Watering practices: Avoid overhead watering, which can keep leaves wet for extended periods and favor fungal growth. Water deeply but infrequently, aiming for moist soil but not soggy roots.\n
                Spacing: Allow for adequate space between grapevines to promote good air circulation.\n
                """)
    treatment7=("""
                Fungicides: Once black rot lesions become visible on fruit, apply fungicides containing copper, mancozeb, or Ziram as soon as possible. Follow label instructions carefully and prioritize preventative applications whenever possible.\n
                Removal of infected fruit: Promptly remove and destroy any infected berries or clusters to prevent further spread of the disease\n
                """)
    st.header("affect by:")
    st.write("Grape berry moth larvae")
    st.image("pest image\Grapg balck rot.jpeg")
    st.header("prevention:")
    st.write(prevention7)
    st.header("treatment:")
    return(treatment7)

def Grape___Esca():
    prevention8=("""
                Stress management: Avoid practices that stress the vines, such as excessive water stress or nutrient deficiencies. Healthy vines are more resilient to disease.\n
                Monitoring: Regularly inspect grapevines for symptoms of Esca, such as stunted shoots, dead spurs, and cankered areas on trunks.\n
                """)
    treatment8=("""
                Calcium chloride, magnesium nitrate, and seaweed extract: Studies suggest this mixture might reduce disease symptoms in some cases. Consult with viticultural experts for specific recommendations and product availability.\n
                Early detection and removal: Removing infected vines as soon as symptoms are identified can help prevent further spread within the vineyard.\n
                """)
    st.header("affect by:")
    st.write("Psyllids")
    st.image("pest image\graph esca.jpeg")
    st.header("prevention:")
    st.write(prevention8)
    st.header("treatment:")
    return(treatment8)

def Grape___Leaf_blight():
    prevention9=("""
                Spacing and air circulation: Plant vines with adequate spacing to improve air circulation and reduce humidity around leaves.\n
                Canopy management: Prune and train vines to create an open canopy that allows for better light penetration and faster drying of leaves.\n
                Sanitation: Remove and destroy fallen leaves and debris around the base of the vine to reduce fungal inoculum (spores) overwintering.\n
                """)
    treatment9=("""
                Fungicides: If preventative measures fail, fungicides containing copper, chlorothalonil, or potassium bicarbonate can be used for control.\n
                Leaf removal: Remove heavily infected leaves to reduce fungal spore production and spread within the vine.\n
                """)
    st.header("affect by:")
    st.write("Psyllids")
    st.image("pest image\graph esca.jpeg")
    st.header("prevention:")
    st.write(prevention9)
    st.header("treatment:")
    return(treatment9)

def Orange___Haunglongbing():
    prevention10=("""
                Insecticides: Apply insecticides targeting ACPs following label instructions and consulting with citrus specialists.\n
                Natural enemies: Encourage natural predators like ladybugs and lacewings by providing habitat diversity.\n
                Sanitation: Remove and destroy any infected trees to prevent further spread.\n
                """)
    treatment10=("""
                Nutritional supplements: Applying supplements like zinc and micronutrients might help maintain tree health for a limited time.\n
                Antibiotics (limited effectiveness): Some research suggests trunk injections with antibiotics might suppress the bacteria in some cases. However, this is not a widespread practice due to cost, limited effectiveness, and potential for resistance development. Consult with citrus specialists for specific recommendations.\n
                """)
    st.header("affect by:")
    st.write("asian cirtus Psyllids")
    st.image("pest image\orange.jpeg")
    st.header("prevention:")
    st.write(prevention10)
    st.header("treatment:")
    return(treatment10)

def Peach___Bacterial_spot():
    prevention11=("""
                Dormant sprays: Apply copper-based bactericides during the dormant season (late fall or early winter) to kill overwintering bacteria on the tree.\n
                Spring and summer sprays: Continue applying copper-based bactericides or antibiotic sprays (oxytetracycline) during spring and early summer, following label instructions and local regulations.\n
                """)
    treatment11=("""
                Nutritional supplements: Applying supplements like zinc and micronutrients might help maintain tree health for a limited time.\n
                Antibiotics (limited effectiveness): Some research suggests trunk injections with antibiotics might suppress the bacteria in some cases. However, this is not a widespread practice due to cost, limited effectiveness, and potential for resistance development. Consult with citrus specialists for specific recommendations.\n
                """)
    st.header("affect by:")
    st.write("Leafhopper")
    st.image("pest image\Corn grey leaf.jpeg")
    st.header("prevention:")
    st.write(prevention11)
    st.header("treatment:")
    return(treatment11)

def Pepper_bell___Bacterial_spot():
    prevention12=("""
                Healthy seeds: Use certified disease-free pepper seeds from reputable suppliers.\n
                Copper sprays: Apply copper-based bactericides as a preventative measure before symptoms appear, following label instructions.\n
                """)
    treatment12=("""
               Sanitation: Remove and destroy any infected plant parts to reduce the source of inoculum (bacteria).\n
                """)
    st.header("affect by:")
    st.write("Stink Bugs")
    st.image("pest image\peach.jpeg")
    st.header("prevention:")
    st.write(prevention12)
    st.header("treatment:")
    return(treatment12)

def Potato___Early_blight():
    prevention13=("""
                Overhead irrigation: Avoid overhead irrigation, which can spread spores and keep leaves wet for extended periods, favoring fungal growth. Water at the soil level.\n
                Sanitation: Remove and destroy infected cull piles and volunteer potato plants to reduce sources of inoculum.\n
                Curing: Properly cure harvested potatoes before storage to allow wound healing, making them less susceptible to infection.\n
                """)
    treatment13=("""
                Fungicides: Apply fungicides containing chlorothalonil or strobilurins only when necessary, following scouting and reaching specific disease thresholds. Fungicide overuse can lead to resistance development.\n
                Early intervention: Fungicide application is most effective when fungal spots are first observed on leaves.\n
                """)
    st.header("affect by:")
    st.write("Leafhopper")
    st.image("pest image\Corn grey leaf.jpeg")
    st.header("prevention:")
    st.write(prevention13)
    st.header("treatment:")
    return(treatment13)

def Potato___Late_blight():
    prevention14=("""
                Certified seed potatoes: Use certified disease-free seed potatoes from reputable suppliers.\n
                Fungicides: Apply preventative fungicides containing copper or chlorothalonil according to label instructions, especially during cool, humid weather when the disease is most prevalent\n
                """)
    treatment14=("""
                Fungicides: If preventative measures fail and late blight is detected early, fungicides containing copper or strobilurins can be used for control.\n
                Removal of infected plants: Quickly remove and destroy any infected plants to prevent further spread within the field.\n
                """)
    st.header("affect by:")
    st.write("Aphids")
    st.image("pest image\Apple balck rot.jpeg")
    st.header("prevention:")
    st.write(prevention14)
    st.header("treatment:")
    return(treatment14)

def Squash___Powdery_mildew():
    prevention15=("""
                Spacing plants: Provide adequate space between squash plants to improve air circulation and reduce humidity around leaves\n
                Watering practices: Water plants at the base to avoid wetting leaves, which can favor fungal growth\n
                Sanitation: Remove and destroy any infected plant debris in the fall to reduce fungal spores overwintering in the garden\n
                """)
    treatment15=("""
                Fungicides: Apply organic fungicides containing sulfur or neem oil according to label instructions.\n
                Baking soda solution: Mix 1 teaspoon of baking soda with 1 quart of water and spray on leaves. Note: Effectiveness can be variable.\n
                """)
    st.header("affect by:")
    st.write("Whiteflies")
    st.image("pest image\sqash.jpeg")
    st.header("prevention:")
    st.write(prevention15)
    st.header("treatment:")
    return(treatment15)

def Strawberry___Leaf_scorch():
    prevention16=("""
                Sunlight and air circulation: Plant strawberries in a sunny location with good air circulation to help leaves dry faster and discourage fungal growth.\n
                Watering: Water deeply and directly at the soil level, avoiding overhead watering that can spread fungal spores.\n
                """)
    treatment16=("""
                Fungicides: While not a primary control strategy due to potential fungicide resistance development, fungicides containing copper or strobilurins might be used in some situations as a last resort. Consult with extension services or a plant pathologist for specific recommendations and application timing.\n
                Removal of infected leaves: Removing heavily infected leaves can help reduce fungal sporulation and spread within the plant.\n
                """)
    st.header("affect by:")
    st.write("Bettle larva")
    st.image("pest image\strawberry.jpeg")
    st.header("prevention:")
    st.write(prevention16)
    st.header("treatment:")
    return(treatment16)

def Tomato___Bacterial_spot():
    prevention17=("""
                Healthy seeds: Use certified disease-free tomato seeds from reputable suppliers.\n
                Copper sprays: Apply copper-based bactericides as a preventative measure before symptoms appear, following label instructions. Organic options like Bordeaux mixture can also be considered.\n
                """)
    treatment17=("""
                Fungicides: Apply fungicides containing chlorothalonil or strobilurins only when necessary, following scouting and reaching specific disease thresholds. Fungicide overuse can lead to resistance development.\n
                Early intervention: Fungicide application is most effective when fungal spots are first observed on leaves.\n
                """)
    st.header("affect by:")
    st.write("Leafhopper")
    st.image("pest image\Corn grey leaf.jpeg")
    st.header("prevention:")
    st.write(prevention17)
    st.header("treatment:")
    return(treatment17)

def Tomato___Early_blight():
    prevention18=("""
                Certified seed potatoes: Use certified disease-free seed potatoes from reputable suppliers.\n
                Fungicides: Apply preventative fungicides containing copper or chlorothalonil according to label instructions, especially during cool, humid weather when the disease is most prevalent\n
                """)
    treatment18=("""
                Fungicides: Apply fungicides containing chlorothalonil or strobilurins only when necessary, following scouting and reaching specific disease thresholds. Fungicide overuse can lead to resistance development.\n
                Early intervention: Fungicide application is most effective when fungal spots are first observed on leaves.\n
                """)
    st.header("affect by:")
    st.write("thrips")
    st.image("pest image\Cherry.jpeg")
    st.header("prevention:")
    st.write(prevention18)
    st.header("treatment:")
    return(treatment18)

def Tomato___Late_blight():
    prevention19=("""
                Watering practices: Water plants at the base to avoid wetting leaves, which can spread the fungus.\n
                Spacing: Provide adequate spacing between tomato plants to promote good air circulation and faster drying of leaves.\n
                """)
    treatment19=("""
                Fungicides: Once symptoms appear, fungicide application can help slow the spread but may not completely cure infected plants. Follow label instructions carefully and choose products safe for edible crops.\n
                Removal of infected plants: Remove and destroy any infected plants to prevent further spread within the garden\n
                """)
    st.header("affect by:")
    st.write("Aphids")
    st.image("pest image\Apple balck rot.jpeg")
    st.header("prevention:")
    st.write(prevention19)
    st.header("treatment:")
    return(treatment19)

def Tomato___Septoria_leaf_spot():
    prevention20=("""
                Crop rotation: Practice crop rotation with non-susceptible crops like lettuce or beans to reduce fungal inoculum (spores) in the soil.\n
                Sanitation: Remove and destroy any infected plant debris at the end of the season to prevent overwintering of the fungus.\n
                """)
    treatment20=("""
                Fungicides: While copper-based fungicides may offer some preventive or suppressive effects, their effectiveness against established Septoria leaf spot infections can be limited.\n
                Removal of infected leaves: If infections are mild, promptly remove and destroy infected lower leaves to prevent further spread to upper foliage and fruit.\n
                """)
    st.header("affect by:")
    st.write("Beetled")
    st.image("pest image\Corn comon rust.jpeg")
    st.header("prevention:")
    st.write(prevention20)
    st.header("treatment:")
    return(treatment20)

def Tomato___Spider_mites():
    prevention21=("""
                Monitor regularly: Inspect the undersides of leaves for webbing and tiny, moving mites (use a magnifying glass if needed). Early detection is crucial.\n
                Promote healthy plants: Maintain healthy tomato plants through proper watering, fertilization, and weed control. Stressed plants are more susceptible to spider mites.\n
                """)
    treatment21=("""
                Insecticidal soap: Apply insecticidal soap sprays directly to the undersides of leaves, ensuring thorough coverage, and repeat every 3-5 days as needed.\n
                Biological controls: Introduce commercially available predatory mites (Phytoseiulus persimilis) that feed on spider mites\n
                """)
    st.header("affect by:")
    st.write("Spider mite")
    st.image("pest image\spider mite.jpeg")
    st.header("prevention:")
    st.write(prevention21)
    st.header("treatment:")
    return(treatment21)

def Tomato___Target_Spot():
    prevention22=("""
                Staking or caging: Provide support for tomato plants to improve air circulation around leaves and fruits.\n
                """)
    treatment22=("""
                Fungicides: If preventative measures fail and target spot is observed, fungicides containing chlorothalonil or strobilurins might be used for control. However,\n
                Apply them only when necessary, following strict guidelines and scouting for disease thresholds.\n
                Alternate fungicide modes of action to reduce the risk of resistance development.\n
                """)
    st.header("affect by:")
    st.write("Threps")
    st.image("pest image\Cherry.jpeg")
    st.header("prevention:")
    st.write(prevention22)
    st.header("treatment:")
    return(treatment22)

def Tomato___Yellow_Leaf_Curl_Virus():
    prevention23=("""
                Monitoring: Use yellow sticky traps to monitor whitefly presence.\n
                Insecticides: Use insecticides targeting whiteflies as a last resort, following label instructions and considering their impact on beneficial insects.\n
                Natural enemies: Encourage natural predators of whiteflies like ladybugs and lacewings by providing habitat diversity.\n
                """)
    treatment23=("""
                Fungicides: If preventative measures fail and target spot is observed, fungicides containing chlorothalonil or strobilurins might be used for control. However,\n
                Apply them only when necessary, following strict guidelines and scouting for disease thresholds.\n
                Alternate fungicide modes of action to reduce the risk of resistance development.\n
                """)
    st.header("affect by:")
    st.write("Whiteflies")
    st.image("pest image\sqash.jpeg")
    st.header("prevention:")
    st.write(prevention23)
    st.header("treatment:")
    return(treatment23)

def Tomato___mosaic_virus():
    prevention24=("""
                Plant early: Plant tomatoes earlier in the season to avoid peak whitefly populations.\n
                Physical barriers: Use insect netting or row covers to exclude whiteflies from reaching plants.\n
                Trap crops: Plant trap crops like squash or melons around the tomato plot to attract whiteflies away from tomatoes.\n
                """)
    treatment24=("""
                Fungicides: If preventative measures fail and target spot is observed, fungicides containing chlorothalonil or strobilurins might be used for control. However,\n
                Apply them only when necessary, following strict guidelines and scouting for disease thresholds.\n
                Alternate fungicide modes of action to reduce the risk of resistance development.\n
                """)
    st.header("affect by:")
    st.write(" silverleafWhiteflies")
    st.image("pest image\mosaic.jpeg")
    st.header("prevention:")
    st.write(prevention24)
    st.header("treatment:")
    return(treatment24)

def Tomato___Leaf_Mold():
    prevention25=("""
                Insect nets: Use insect netting or row covers to exclude whiteflies from your tomato plants.\n
                Insecticidal soaps: Apply insecticidal soaps or neem oil sprays (as permitted by regulations) to target whiteflies, following label instructions.\n
                Encourage beneficial insects: Promote beneficial insects like ladybugs and lacewings that can help control whitefly populations naturally.\n
                """)
    treatment25=("""
                Fungicides: If preventative measures fail and target spot is observed, fungicides containing chlorothalonil or strobilurins might be used for control. However,\n
                Apply them only when necessary, following strict guidelines and scouting for disease thresholds.\n
                Alternate fungicide modes of action to reduce the risk of resistance development.\n
                """)
    st.header("affect by:")
    st.write(" silverleafWhiteflies")
    st.image("pest image\mosaic.jpeg")
    st.header("prevention:")
    st.write(prevention25)
    st.header("treatment:")
    return(treatment25)

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])

#Main Page
if(app_mode=="Home"):
    st.header("PEST DETECTION AND SOLUTION RECOMMENDATION")
    image_path = "back.jpeg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
    Welcome to the Pest detection System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    #### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Identify:** after analysis it display the pest identified.
    4. **Solution:** It will recommend the solution for identified disease.            

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our pest detection System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purpose.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)

                """)
    
#Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    imageCaptured=st.camera_input("capture image",key="firstCamera")
    test_image = imageCaptured
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        final_result=("Model is Predicting it's a {}".format(class_name[result_index]))
        st.success(final_result)
        if(class_name[result_index]=='Apple___Apple_scab'):
            st.write(Apple___Apple_scab())
        elif(class_name[result_index]=='Apple___Black_rot'):
            st.write(Apple___Black_rot())
        elif(class_name[result_index]=='Apple___Cedar_apple_rust'):
            st.write(Apple___Cedar_apple_rust())
        elif(class_name[result_index]=='Cherry_(including_sour)___Powdery_mildew'):
            st.write(Cherry___Powdery_mildew())
        elif(class_name[result_index]=='Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot'):
            st.write(Corn___Cercospora_leaf_spot_Gray_leaf_spot())
        elif(class_name[result_index]=='Corn_(maize)___Common_rust_'):
            st.write(Corn___Common_rust())
        elif(class_name[result_index]=='Corn_(maize)___Northern_Leaf_Blight'):
            st.write(Corn___Northern_Leaf_Blight())
        elif(class_name[result_index]=='Grape___Black_rot'):
            st.write(Grape___Black_rot())
        elif(class_name[result_index]=='Grape___Esca_(Black_Measles)'):
            st.write(Grape___Esca())
        elif(class_name[result_index]=='Grape___Leaf_blight_(Isariopsis_Leaf_Spot)'):
            st.write(Grape___Leaf_blight())
        elif(class_name[result_index]=='Orange___Haunglongbing_(Citrus_greening)'):
            st.write(Orange___Haunglongbing())
        elif(class_name[result_index]=='Peach___Bacterial_spot'):
            st.write(Peach___Bacterial_spot())
        elif(class_name[result_index]=='Potato___Early_blight'):
            st.write(Potato___Early_blight())
        elif(class_name[result_index]=='Potato___Late_blight'):
            st.write(Potato___Late_blight())
        elif(class_name[result_index]=='Squash___Powdery_mildew'):
            st.write(Squash___Powdery_mildew())
        elif(class_name[result_index]=='Strawberry___Leaf_scorch'):
            st.write(Strawberry___Leaf_scorch())
        elif(class_name[result_index]=='Tomato___Bacterial_spot'):
            st.write(Tomato___Bacterial_spot())
        elif(class_name[result_index]=='Tomato___Early_blight'):
            st.write(Tomato___Early_blight())
        elif(class_name[result_index]=='Tomato___Late_blight'):
            st.write(Tomato___Late_blight())
        elif(class_name[result_index]=='Tomato___Septoria_leaf_spot'):
            st.write(Tomato___Septoria_leaf_spot())
        elif(class_name[result_index]=='Tomato___Spider_mites Two-spotted_spider_mite'):
            st.write(Tomato___Spider_mites())
        elif(class_name[result_index]=='Tomato___Target_Spot'):
            st.write(Tomato___Target_Spot())
        elif(class_name[result_index]=='Tomato___Tomato_Yellow_Leaf_Curl_Virus'):
            st.write(Tomato___Yellow_Leaf_Curl_Virus())
        elif(class_name[result_index]=='Tomato___Tomato_mosaic_virus'):
            st.write(Tomato___mosaic_virus())
        elif(class_name[result_index]=='Tomato___Leaf_Mold'):
            st.write(Tomato___Leaf_Mold())
        else:
            st.write("it is healthy")
        
        
        





