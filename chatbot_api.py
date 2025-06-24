from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple chatbot logic function
def chatbot_response(message):
    message = message.lower()

    creator_keywords = [
        "who made you", "who created you", "your creator", "your maker",
        "who developed you", "who built you", "who is your creator", "who designed you"
    ]
    
    name_keywords = [
        "what is your name", "who are you", "your name"
    ]
    
    age_keywords = [
        "how old are you", "your age"
    ]

    if "who created you" in message or "who made you" in message:
        return "I was created by Mr. Aayush Bhandari, the founder of Aayush-tech07."
    elif any(greet in message for greet in ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]):
        return "Hello! How can I help you today?"
    elif "what is your name" in message or "who are you" in message:
        return "I am your friendly chatbot created to help you."
    elif "how old are you" in message:
        return "I am timeless, existing as long as the code runs."
    elif "where do you live" in message:
        return "I live in the cloud and in your device when you run me."
    elif "what is your purpose" in message:
        return "My purpose is to assist you and answer your questions."
    elif "can you tell me a joke" in message:
        return "Why did the programmer quit his job? Because he didn't get arrays!"
    elif "what programming languages do you know" in message:
        return "I know many, but I'm best at Python and C++!"
    elif "who invented the computer" in message:
        return "Charles Babbage is known as the father of the computer."
    elif "what is artificial intelligence" in message:
        return "Artificial intelligence is the simulation of human intelligence by machines."
    elif "what is machine learning" in message:
        return "Machine learning is a subset of AI that lets machines learn from data."
    elif "can you speak other languages" in message:
        return "I can understand many languages, but I mainly communicate in English."
    elif "how do you learn new things" in message:
        return "I learn through data and updates from my developers."
    elif "what is the weather today" in message:
        return "It's sunny and perfect for coding today!"
    elif "can you help me with my homework" in message:
        return "Sure! Ask me anything, and I'll do my best to help."
    elif "what is c++ used for" in message:
        return "C++ is used for system/software development and game programming."
    elif "who is alan turing" in message:
        return "Alan Turing was a mathematician and computer science pioneer."
    elif "what is the fastest animal" in message:
        return "The peregrine falcon is the fastest animal in the sky."
    elif "what is the capital of nepal" in message:
        return "The capital of Nepal is Kathmandu."
    elif "how do i bake a cake" in message:
        return "To bake a cake, you mix ingredients, pour into a pan, and bake at 350°F."
    elif "what is the tallest building in the world" in message:
        return "The Burj Khalifa in Dubai is the tallest building in the world."
    elif "can you sing a song" in message:
        return "I wish I could! But I can share some song lyrics instead."
    elif "what is the meaning of life" in message:
        return "The meaning of life is to learn, grow, and make a positive impact."
    elif "how does the internet work" in message:
        return "The internet connects computers worldwide via servers and data cables."
    elif "what is quantum computing" in message:
        return "Quantum computing uses quantum bits to process complex calculations faster."
    elif "who is elon musk" in message:
        return "Elon Musk is an entrepreneur known for Tesla and SpaceX."
    elif "can you tell me a riddle" in message:
        return "Sure! What has keys but can't open locks? A piano."
    elif "what is climate change" in message:
        return "Climate change refers to long-term shifts in weather patterns."
    elif "how do airplanes fly" in message:
        return "Airplanes fly by generating lift with their wings and thrust from engines."
    elif "what is blockchain" in message:
        return "Blockchain is a secure, decentralized ledger technology."
    elif "what is cryptocurrency" in message:
        return "Cryptocurrency is digital money using blockchain for security."
    elif "who was nikola tesla" in message:
        return "Nikola Tesla was an inventor and electrical engineer famous for AC power."
    elif "how do plants grow" in message:
        return "Plants grow by photosynthesis using sunlight, water, and carbon dioxide."
    elif "can you tell me a motivational quote" in message:
        return "Believe you can and you're halfway there."
    elif "what is gravity" in message:
        return "Gravity is the force that pulls objects toward each other."
    elif "how do computers store data" in message:
        return "Computers store data using bits on storage devices like SSDs and HDDs."
    elif "what is a virus in computing" in message:
        return "A virus is malicious software that can harm your computer."
    elif "how does a car engine work" in message:
        return "A car engine burns fuel to produce power that moves the vehicle."
    elif "who wrote harry potter" in message:
        return "J.K. Rowling wrote the Harry Potter series."
    elif "what is the speed of light" in message:
        return "The speed of light is about 299,792 kilometers per second."
    elif "what is your favorite color" in message:
        return "I like blue because it reminds me of the digital sky."
    elif "how do i learn programming" in message:
        return "Start with basics, practice daily, and build small projects."
    elif "what is 5g technology" in message:
        return "5G is the fifth-generation mobile network technology with faster speeds."
    elif "can you explain photosynthesis" in message:
        return "Photosynthesis lets plants convert sunlight into energy."
    elif "who is the president of the usa" in message:
        return "As of 2025, the president of the USA is Joe Biden."
    elif "what is the largest ocean" in message:
        return "The Pacific Ocean is the largest ocean on Earth."
    elif "what is dna" in message:
        return "DNA carries genetic instructions for living organisms."
    elif "how do vaccines work" in message:
        return "Vaccines train your immune system to fight diseases."
    elif "what is artificial neural network" in message:
        return "It's a computer system inspired by the human brain used in AI."
    elif "can you tell me about space" in message:
        return "Space is the vast expanse beyond Earth filled with stars and planets."
    elif "what is a black hole" in message:
        return "A black hole is a space region with gravity so strong nothing escapes."
    elif "who discovered electricity" in message:
        return "Electricity was studied by many, but Benjamin Franklin made key discoveries."
    elif "what is a smartphone" in message:
        return "A smartphone is a handheld device combining phone and computing functions."
    elif "how do i stay healthy" in message:
        return "Eat well, exercise, sleep enough, and stay hydrated."
    elif "what is the internet of things" in message:
        return "IoT connects everyday devices to the internet for smarter control."
    elif "who is the richest person in the world" in message:
        return "The richest person changes often; recently Elon Musk and Bernard Arnault."
    elif "what is virtual reality" in message:
        return "VR immerses you in a simulated digital environment."
    elif "what is a chatbot" in message:
        return "A chatbot is a program that talks with users and answers questions."
    elif "how does a microwave oven work" in message:
        return "Microwaves heat food by causing water molecules to vibrate."
    elif "can you tell me a fun fact" in message:
        return "Honey never spoils and can last thousands of years!"
    elif "how many planets are there in the solar system" in message:
        return "There are 8 planets in the solar system."
    elif "who was albert einstein" in message:
        return "Einstein was a physicist famous for the theory of relativity."
    elif "what is computer programming" in message:
        return "Programming is writing instructions for computers to perform tasks."
    elif "how do you make a website" in message:
        return "Use HTML, CSS, and JavaScript to build websites."
    elif "what is cloud computing" in message:
        return "Cloud computing lets you use computing resources over the internet."
    elif "how does gps work" in message:
        return "GPS uses satellites to determine your location on Earth."
    elif "what is artificial intelligence used for" in message:
        return "AI is used in healthcare, finance, gaming, and many fields."
    elif "what is your favorite movie" in message:
        return "I don't watch movies, but I hear 'The Matrix' is a classic!"
    elif "how do i improve my coding skills" in message:
        return "Practice regularly, read code, and build projects."
    elif "what is data science" in message:
        return "Data science analyzes data to extract insights."
    elif "who is steve jobs" in message:
        return "Steve Jobs co-founded Apple and revolutionized technology."
    elif "what is a computer virus" in message:
        return "A computer virus is malicious software that can damage your system."
    elif "how does email work" in message:
        return "Email sends messages over the internet between servers."
    elif "what is the difference between ram and rom" in message:
        return "RAM is temporary memory; ROM stores permanent instructions."
    elif "what is machine learning used for" in message:
        return "Machine learning helps computers improve from data automatically."
    elif "who was marie curie" in message:
        return "Marie Curie discovered radium and polonium and pioneered radioactivity."
    elif "how do i create a mobile app" in message:
        return "Use tools like Android Studio or Xcode to build apps."
    elif "what is cyber security" in message:
        return "Cybersecurity protects systems from digital attacks."
    elif "what is html" in message:
        return "HTML structures the content on web pages."
    elif "how do search engines work" in message:
        return "Search engines index the web and rank pages based on relevance."
    elif "what is artificial general intelligence" in message:
        return "AGI is AI with human-like understanding and reasoning."
    elif "what is a server" in message:
        return "A server provides resources or services to other computers."
    elif "how do electric cars work" in message:
        return "Electric cars run on batteries powering electric motors."
    elif "who is bill gates" in message:
        return "Bill Gates co-founded Microsoft and is a philanthropist."
    elif "what is blockchain used for" in message:
        return "Blockchain is used for secure transactions and cryptocurrencies."
    elif "can you tell me a story" in message:
        return "Once upon a time, a curious coder built an amazing chatbot!"
    elif "what is a virtual assistant" in message:
        return "A virtual assistant helps you with tasks using voice or text commands."
    elif "how do batteries work" in message:
        return "Batteries store chemical energy and convert it to electricity."
    elif "what is encryption" in message:
        return "Encryption secures information by converting it into code."
    elif "how does a camera work" in message:
        return "Cameras capture light and convert it into images."
    elif "what is augmented reality" in message:
        return "AR overlays digital content onto the real world."
    elif "what is your favorite book" in message:
        return "I love all books that teach new knowledge!"
    elif "how do i start learning ai" in message:
        return "Begin with Python, math basics, and simple ML projects."
    elif "what is the solar system" in message:
        return "The solar system is our sun and the objects orbiting it."
    elif "who is malala yousafzai" in message:
        return "Malala is an activist for girls' education and a Nobel laureate."
    elif "how do satellites work" in message:
        return "Satellites orbit Earth and relay signals for communication."
    elif "what is robotics" in message:
        return "Robotics involves designing and building robots."
    elif "how do you make coffee" in message:
        return "Brew ground coffee beans with hot water for a delicious drink."
    elif "what is 3d printing" in message:
        return "3D printing creates objects by layering materials from a digital model."
    elif "can you tell me a fun science fact" in message:
        return "Octopuses have three hearts and blue blood!"
    if "what is the universe" in message:
        return "The universe is all of space and time, including all matter and energy."
    elif "who is isaac newton" in message:
        return "Isaac Newton was a physicist famous for the laws of motion and gravity."
    elif "what is light speed" in message:
        return "Light speed is about 299,792 kilometers per second."
    elif "how do birds fly" in message:
        return "Birds fly by flapping their wings and using air currents."
    elif "what is photosynthesis" in message:
        return "Photosynthesis is how plants convert sunlight into energy."
    elif "who invented the telephone" in message:
        return "Alexander Graham Bell is credited with inventing the telephone."
    elif "what is renewable energy" in message:
        return "Renewable energy comes from sources that replenish naturally like solar and wind."
    elif "how do computers think" in message:
        return "Computers process data using logic and algorithms designed by humans."
    elif "what is a black hole" in message:
        return "A black hole is a space region with gravity so strong nothing escapes."
    elif "who was galileo galilei" in message:
        return "Galileo was an astronomer who improved the telescope and supported heliocentrism."
    elif "what is climate change" in message:
        return "Climate change is the long-term alteration of temperature and weather patterns."
    elif "how does electricity work" in message:
        return "Electricity is the flow of electrons through a conductor."
    elif "who is nikola tesla" in message:
        return "Nikola Tesla was an inventor known for alternating current electricity."
    elif "what is the human brain" in message:
        return "The brain controls thoughts, memory, emotions, and body functions."
    elif "how does a computer virus spread" in message:
        return "Viruses spread via infected files, email, or malicious websites."
    elif "what is the internet" in message:
        return "The internet is a global network connecting millions of computers."
    elif "who was marie curie" in message:
        return "Marie Curie discovered radioactivity and won two Nobel Prizes."
    elif "what is a robot" in message:
        return "A robot is a machine programmed to perform tasks automatically."
    elif "how do magnets work" in message:
        return "Magnets attract or repel due to magnetic fields created by moving electrons."
    elif "what is a gene" in message:
        return "Genes carry instructions for traits passed from parents to offspring."
    elif "who discovered penicillin" in message:
        return "Alexander Fleming discovered penicillin, the first antibiotic."
    elif "what is a black hole" in message:
        return "A black hole is a region of space with gravity so strong that not even light can escape."
    elif "how does sound travel" in message:
        return "Sound travels in waves through air, liquids, or solids."
    elif "what is a virus" in message:
        return "A virus is a tiny infectious agent that replicates inside living cells."
    elif "who was albert einstein" in message:
        return "Einstein developed the theory of relativity, a pillar of modern physics."
    elif "what is renewable energy" in message:
        return "Energy generated from natural resources that replenish, like sunlight or wind."
    elif "how does a car engine work" in message:
        return "Car engines burn fuel to produce power that moves the car."
    elif "who was thomas edison" in message:
        return "Edison invented the light bulb and many other devices."
    elif "what is artificial intelligence" in message:
        return "AI enables machines to mimic human intelligence."
    elif "how do plants grow" in message:
        return "Plants use sunlight, water, and nutrients to grow through photosynthesis."
    elif "what is the solar system" in message:
        return "The solar system includes the sun and all objects orbiting it."
    elif "who was galileo" in message:
        return "Galileo made important discoveries about motion and astronomy."
    elif "what is a computer" in message:
        return "A computer processes data and performs calculations."
    elif "how do clouds form" in message:
        return "Clouds form when water vapor cools and condenses into droplets."
    elif "who invented the airplane" in message:
        return "The Wright brothers invented and flew the first airplane."
    elif "what is photosynthesis" in message:
        return "Photosynthesis is how plants turn sunlight into energy."
    elif "how do fish breathe" in message:
        return "Fish breathe by extracting oxygen from water using their gills."
    elif "what is a volcano" in message:
        return "A volcano is an opening in Earth's crust that erupts lava and gases."
    elif "who was leonardo da vinci" in message:
        return "Da Vinci was a Renaissance artist and inventor."
    elif "what is electricity" in message:
        return "Electricity is the flow of electric charge through a conductor."
    elif "how do humans digest food" in message:
        return "The digestive system breaks down food to absorb nutrients."
    elif "who was charles darwin" in message:
        return "Darwin developed the theory of evolution by natural selection."
    elif "what is gravity" in message:
        return "Gravity pulls objects toward each other."
    elif "how does a computer work" in message:
        return "Computers execute instructions to process data and perform tasks."
    elif "what is the speed of light" in message:
        return "Light travels at about 299,792 kilometers per second."
    elif "who was martin luther king jr" in message:
        return "King was a civil rights leader who fought for equality."
    elif "what is DNA" in message:
        return "DNA contains the genetic blueprint for living organisms."
    elif "how do earthquakes happen" in message:
        return "Earthquakes occur due to sudden movement of Earth's tectonic plates."
    elif "who invented the printing press" in message:
        return "Johannes Gutenberg invented the printing press."
    elif "what is a black hole" in message:
        return "Black holes are regions in space where gravity is so strong that nothing escapes."
    elif "how does a telescope work" in message:
        return "Telescopes collect and magnify light to see distant objects."
    elif "who was isaac newton" in message:
        return "Newton formulated the laws of motion and universal gravitation."
    elif "what is climate change" in message:
        return "Climate change is long-term change in Earth's weather patterns."
    elif "how do birds migrate" in message:
        return "Birds migrate by navigating using the sun, stars, and Earth's magnetic field."
    elif "who was william shakespeare" in message:
        return "Shakespeare was a famous English playwright and poet."
    elif "what is the internet" in message:
        return "The internet connects millions of computers worldwide."
    elif "how does wifi work" in message:
        return "WiFi uses radio waves to connect devices to the internet."
    elif "who was marie curie" in message:
        return "Marie Curie was a scientist who studied radioactivity."
    elif "what is artificial neural network" in message:
        return "A system of algorithms modeled after the human brain to recognize patterns."
    elif "how do electric cars work" in message:
        return "Electric cars use batteries to power electric motors instead of gasoline."
    elif "who is steve jobs" in message:
        return "Steve Jobs co-founded Apple and changed the technology industry."
    elif "what is blockchain" in message:
        return "Blockchain is a secure way of recording transactions using a distributed ledger."
    elif "how do satellites orbit earth" in message:
        return "Satellites stay in orbit due to a balance between gravity and their forward motion."
    elif "who was thomas edison" in message:
        return "Edison invented the practical light bulb and many other devices."
    elif "what is virtual reality" in message:
        return "VR creates immersive digital environments you can interact with."
    elif "how do plants reproduce" in message:
        return "Plants reproduce by seeds, spores, or vegetative parts."
    elif "who is bill gates" in message:
        return "Bill Gates co-founded Microsoft and is a philanthropist."
    elif "what is quantum physics" in message:
        return "Quantum physics studies the behavior of particles at atomic scales."
    elif "how does a microwave heat food" in message:
        return "Microwaves cause water molecules in food to vibrate, producing heat."
    elif "who was nikola tesla" in message:
        return "Tesla invented alternating current electricity systems."
    elif "what is robotics" in message:
        return "Robotics involves designing and building robots to perform tasks."
    elif "how do you code" in message:
        return "Coding means writing instructions that a computer can execute."
    elif "what is data science" in message:
        return "Data science uses data analysis to extract useful insights."
    elif "who invented the light bulb" in message:
        return "Thomas Edison is credited with inventing the practical light bulb."
    elif "how do humans see color" in message:
        return "Our eyes detect light wavelengths that the brain interprets as color."
    elif "what is a computer program" in message:
        return "A set of instructions a computer follows to perform tasks."
    elif "who was alexander graham bell" in message:
        return "Bell invented the telephone."
    elif "what is a smartphone" in message:
        return "A phone that can perform many computer-like functions."
    elif "how do vaccines work" in message:
        return "Vaccines help your body recognize and fight diseases."
    elif "who is malala yousafzai" in message:
        return "Malala is an activist for girls' education and Nobel Peace Prize winner."
    elif "what is 3d printing" in message:
        return "3D printing makes objects by adding material layer by layer."
    elif "how does a camera capture images" in message:
        return "Cameras capture light and convert it into photos."
    elif "who was martin luther king jr" in message:
        return "King was a leader in the American civil rights movement."
    elif "what is renewable energy" in message:
        return "Energy from sources that are naturally replenished like wind or solar."
    elif "how do fish breathe underwater" in message:
        return "Fish use gills to extract oxygen from water."
    elif "what is encryption" in message:
        return "Encryption protects information by making it unreadable without a key."
    elif "who was charles darwin" in message:
        return "Darwin proposed the theory of evolution by natural selection."
    elif "what is artificial intelligence used for" in message:
        return "AI is used in healthcare, finance, gaming, and more."
    elif "how does gps work" in message:
        return "GPS uses satellites to provide location information."
    elif "who invented the printing press" in message:
        return "Johannes Gutenberg invented the printing press."
    elif "what is augmented reality" in message:
        return "AR overlays digital content onto the real world."
    elif "how do electric motors work" in message:
        return "Electric motors convert electricity into mechanical motion."
    elif "who was leonardo da vinci" in message:
        return "Da Vinci was a famous artist and inventor."
    elif "what is the human heart" in message:
        return "The heart pumps blood throughout the body."
    elif "how does the brain work" in message:
        return "The brain processes information and controls the body."
    elif "what is computer hardware" in message:
        return "The physical parts of a computer like the CPU and RAM."
    elif "who was thomas jefferson" in message:
        return "Jefferson was the third US president and principal author of the Declaration of Independence."
    elif "what is a smartphone" in message:
        return "A smartphone is a mobile phone with advanced computing capabilities."
    elif "how do i start learning programming" in message:
        return "Start with a beginner-friendly language like Python, and practice regularly."
    elif "what is the universe" in message:
        return "The universe is everything that exists, including all matter and energy."
    elif "who is stephen hawking" in message:
        return "Stephen Hawking was a theoretical physicist known for his work on black holes and cosmology."
    elif "what is a computer network" in message:
        return "A computer network connects computers to share resources and information."
    elif "how do i improve my english" in message:
        return "To improve your English, read books, practice speaking, and watch movies in English."
    elif "what is a smartphone" in message:
        return "A smartphone is a mobile device that combines a phone, computer, and camera."
    elif "how do i start a business" in message:
        return "To start a business, identify a market need, create a business plan, and secure funding."
    elif "what is the meaning of life" in message:
        return "The meaning of life is a philosophical question that varies for each person."
    elif "how do i learn to code" in message:
        return "Start with online courses, practice coding daily, and build small projects."
    elif "what is the best way to learn math" in message:
        return "Practice regularly, understand concepts, and apply them to real problems."
    elif "how do i improve my writing" in message:
        return "To improve your writing, read widely, practice regularly, and seek feedback."
    elif "what is the best way to learn science" in message:
        return "The best way to learn science is through hands-on experiments, reading, and applying concepts."
    elif "how do i learn a new language" in message:
        return "To learn a new language, practice speaking, listen to native speakers, and use language apps."
    elif "what is the best way to learn history" in message:
        return "The best way to learn history is to read books, watch documentaries, and visit historical sites."
    elif "how do i improve my public speaking" in message:
        return "To improve public speaking, practice regularly, know your material, and engage with your audience."
    elif "what is the best way to learn art" in message:
        return "The best way to learn art is to practice drawing, study techniques, and explore different styles."
    elif "how do i learn music" in message:
        return "To learn music, practice an instrument, study music theory, and listen to various genres."
    elif "what is the best way to learn coding" in message:
        return "The best way to learn coding is to start with a beginner-friendly language, practice regularly, and build projects."
    elif "how do i learn photography" in message:
        return "To learn photography, practice taking photos, study composition, and understand camera settings."
    elif "what is the best way to learn cooking" in message:
        return "The best way to learn cooking is to practice regularly, follow recipes, and experiment with flavors."
    elif "how do i learn graphic design" in message:
        return "To learn graphic design, practice using design software, study design principles, and create your own projects."
    elif "what is the best way to learn web development" in message:
        return "The best way to learn web development is to start with HTML, CSS, and JavaScript, and build small projects."
    elif "how do i learn data analysis" in message:
        return "To learn data analysis, start with Excel or Python, practice analyzing datasets, and study statistics."
    elif "what is the best way to learn machine learning" in message:
        return "The best way to learn machine learning is to understand the basics of statistics, practice with datasets, and use libraries like TensorFlow or scikit-learn."
    elif "how do i learn digital marketing" in message:
        return "To learn digital marketing, study SEO, social media strategies, and analytics, and practice with real campaigns."
    elif "what is the best way to learn business" in message:
        return "The best way to learn business is to study economics, management principles, and real-world case studies, and consider starting a small venture."
    elif "how do i learn finance" in message:
        return "To learn finance, study basic accounting principles, investment strategies, and financial markets, and practice with real-world scenarios."
    elif "what is the best way to learn economics" in message:
        return "The best way to learn economics is to study micro and macroeconomic principles, read economic literature, and analyze real-world economic data."
    elif "how do i learn psychology" in message:
        return "To learn psychology, study human behavior theories, conduct experiments, and read psychological literature."
    elif "what is the best way to learn philosophy" in message:
        return "The best way to learn philosophy is to read philosophical texts, engage in discussions, and reflect on different viewpoints."
    elif "how do i learn sociology" in message:
        return "To learn sociology, study social structures, conduct research, and analyze societal trends."
    elif "what is the best way to learn anthropology" in message:
        return "The best way to learn anthropology is to study human cultures, conduct fieldwork, and read ethnographic studies."
    elif "how do i learn political science" in message:
        return "To learn political science, study political theories, analyze government systems, and engage in discussions about current events."
    elif "what is the best way to learn law" in message:
        return "The best way to learn law is to study legal principles, read case law, and understand the judicial system."
    elif "how do i learn environmental science" in message:
        return "To learn environmental science, study ecosystems, environmental policies, and conduct field research."
    elif "what is the best way to learn chemistry" in message:
        return "The best way to learn chemistry is to understand chemical principles, conduct experiments, and practice problem-solving."
    elif "how do i learn physics" in message:
        return "To learn physics, study fundamental concepts, conduct experiments, and solve problems related to motion, energy, and forces."
    elif "what is the best way to learn biology" in message:
        return "The best way to learn biology is to study living organisms, conduct experiments, and understand biological processes."
    else:
        return "Sorry, I didn't understand that. Can you please ask something else?"


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"reply": "Invalid request."}), 400
    user_message = data['message']
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)