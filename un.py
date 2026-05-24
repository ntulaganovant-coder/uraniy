import tkinter as tk
from tkinter import ttk
import math
from PIL import Image, ImageTk  # ← add this at the top

root = tk.Tk()  # ← root must be defined first
root.title("Uraniumiy")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

# 🖼️ Load image (after root is defined)
img = Image.open("Icon-uranium (1).png")  # ← change to your image path
img = img.resize((40, 40))
photo = ImageTk.PhotoImage(img)

# 🏷️ Title frame
title_frame = tk.Frame(root, bg="#1e1e1e")
title_frame.pack(pady=(20, 5))

tk.Label(title_frame, image=photo, bg="#1e1e1e").pack(side="left", padx=(0, 10))
tk.Label(title_frame, text="Uraniumiy", bg="#1e1e1e", fg="white",
         font=("Arial", 18, "bold")).pack(side="left")

root.photo = photo  # ← prevent garbage collection

# Subtitle
tk.Label(root, text="Education has no limit",
         bg="#1e1e1e", fg="#888888", font=("Arial", 10)).pack(pady=(0, 10))

# ... rest of your code below


data = {
    # 🍎 Fruits
    "Apple": "A sweet red or green fruit rich in fiber and vitamin C. Great for digestion.",
    "Banana": "A yellow tropical fruit high in potassium. Good for energy and heart health.",
    "Cherry": "A small red fruit rich in antioxidants. Helps reduce inflammation.",
    "Mango": "A tropical fruit rich in vitamins A and C. Known as the king of fruits.",
    "Grape": "Small juicy fruit rich in antioxidants. Good for heart health.",
    "Watermelon": "A large fruit with high water content. Great for hydration.",
    "Strawberry": "A red berry rich in vitamin C and antioxidants.",
    "Orange": "A citrus fruit high in vitamin C. Boosts immune system.",
    "Pineapple": "A tropical fruit containing bromelain enzyme. Aids digestion.",
    "Lemon": "A sour citrus fruit rich in vitamin C. Great for detox drinks.",
    "Lime": "A small green citrus fruit. Used in cooking and drinks.",
    "Peach": "A soft sweet fruit rich in vitamins A and C.",
    "Pear": "A sweet fruit high in fiber and vitamin C.",
    "Plum": "A small purple fruit rich in antioxidants and vitamin C.",
    "Blueberry": "A small blue berry packed with antioxidants. Great for brain health.",
    "Raspberry": "A red berry rich in fiber and vitamin C.",
    "Blackberry": "A dark berry high in antioxidants and vitamins.",
    "Coconut": "A tropical fruit rich in healthy fats and electrolytes.",
    "Avocado": "A creamy fruit rich in healthy fats and potassium.",
    "Pomegranate": "A red fruit full of antioxidants. Good for heart health.",
    "Kiwi": "A small green fruit rich in vitamin C and K.",
    "Papaya": "A tropical fruit rich in vitamin C and digestive enzymes.",
    "Guava": "A tropical fruit high in vitamin C and fiber.",
    "Lychee": "A sweet tropical fruit rich in vitamin C.",
    "Fig": "A sweet fruit rich in fiber and minerals.",
    "Date": "A sweet dried fruit high in energy and minerals.",
    "Apricot": "A small orange fruit rich in vitamins A and C.",
    "Cantaloupe": "A melon rich in vitamins A and C.",
    "Honeydew": "A sweet green melon high in water content.",
    "Durian": "A tropical fruit known for its strong smell and creamy taste.",
    "Jackfruit": "A large tropical fruit used as a meat substitute.",
    "Passion Fruit": "A tropical fruit rich in antioxidants and fiber.",
    "Starfruit": "A star-shaped fruit rich in vitamin C.",
    "Persimmon": "A sweet orange fruit rich in vitamins A and C.",
    "Quince": "A yellow fruit rich in fiber and antioxidants.",
    "Mulberry": "A sweet berry rich in iron and vitamin C.",
    "Gooseberry": "A small tart berry rich in vitamin C.",
    "Cranberry": "A red berry known for urinary tract health benefits.",
    "Elderberry": "A dark berry used for immune support.",
    "Tamarind": "A sour tropical fruit used in cooking and sauces.",
    "Kumquat": "A tiny citrus fruit eaten whole, skin and all.",
    "Mandarin": "A small sweet citrus fruit easy to peel.",
    "Tangerine": "A sweet citrus fruit similar to mandarin.",
    "Plantain": "A starchy banana-like fruit used in cooking.",
    "Yuzu": "A Japanese citrus fruit with a unique flavor.",
    "Nectarine": "A smooth-skinned peach-like fruit rich in vitamins.",
    "Ugli Fruit": "A Jamaican citrus fruit with a rough exterior.",
    "Olive": "A small fruit rich in healthy fats. Used for oil.",
    "Currant": "A small tart berry rich in vitamin C.",

    # 🥦 Vegetables
    "Carrot": "An orange vegetable rich in beta-carotene and vitamin A. Good for eyesight.",
    "Broccoli": "A green vegetable rich in vitamin C and K. Great for immunity.",
    "Spinach": "A leafy green vegetable rich in iron and vitamins.",
    "Tomato": "A red vegetable rich in lycopene and vitamin C.",
    "Potato": "A starchy vegetable rich in carbohydrates and potassium.",
    "Onion": "A pungent vegetable rich in antioxidants and vitamin C.",
    "Garlic": "A strong-flavored vegetable with antibacterial properties.",
    "Cucumber": "A green vegetable high in water content. Good for hydration.",
    "Cabbage": "A leafy vegetable rich in vitamin C and K.",
    "Cauliflower": "A white vegetable rich in vitamins and fiber.",
    "Bell Pepper": "A colorful vegetable rich in vitamin C and antioxidants.",
    "Eggplant": "A purple vegetable rich in antioxidants and fiber.",
    "Zucchini": "A green vegetable low in calories and rich in vitamins.",
    "Pumpkin": "An orange vegetable rich in vitamin A and fiber.",
    "Sweet Potato": "An orange root vegetable rich in vitamins A and C.",
    "Corn": "A yellow vegetable rich in fiber and vitamins.",
    "Pea": "A small green vegetable rich in protein and fiber.",
    "Celery": "A crunchy vegetable low in calories and high in water.",
    "Lettuce": "A leafy vegetable low in calories and high in water.",
    "Kale": "A leafy green vegetable packed with vitamins K, A, and C.",
    "Asparagus": "A green vegetable rich in folate and vitamins.",
    "Beetroot": "A red vegetable rich in iron and antioxidants.",
    "Mushroom": "A fungus rich in B vitamins and minerals.",
    "Ginger": "A spicy root vegetable used for digestive health.",
    "Artichoke": "A vegetable rich in fiber and antioxidants.",
    "Leek": "A mild onion-flavored vegetable rich in vitamins.",
    "Radish": "A crunchy root vegetable rich in vitamin C.",
    "Turnip": "A root vegetable rich in vitamins C and K.",
    "Parsnip": "A white root vegetable rich in fiber and vitamins.",
    "Fennel": "An aromatic vegetable with a mild anise flavor.",
    "Okra": "A green vegetable rich in fiber and vitamins.",
    "Brussels Sprout": "A small cabbage-like vegetable rich in vitamins C and K.",
    "Bok Choy": "A Chinese cabbage rich in vitamins A and C.",
    "Arugula": "A peppery leafy green rich in vitamins.",
    "Kohlrabi": "A bulb vegetable rich in vitamin C and fiber.",
    "Butternut Squash": "A sweet orange squash rich in vitamins A and C.",
    "Chili Pepper": "A spicy vegetable rich in capsaicin and vitamin C.",
    "Green Bean": "A slender vegetable rich in vitamins C and K.",
    "Shallot": "A mild onion-like vegetable rich in antioxidants.",
    "Yam": "A starchy root vegetable rich in potassium and vitamins.",
    "Watercress": "A peppery leafy green rich in vitamins K and C.",
    "Endive": "A bitter leafy vegetable rich in vitamins.",
    "Radicchio": "A red leafy vegetable rich in antioxidants.",
    "Rutabaga": "A root vegetable rich in vitamins C and E.",
    "Sorrel": "A sour leafy green rich in vitamins C and A.",
    "Chard": "A leafy green vegetable rich in vitamins K and A.",
    "Collard Greens": "A leafy green vegetable rich in vitamins K and C.",
    "Rapini": "A bitter green vegetable rich in vitamins A and C.",
    "White Radish": "A mild root vegetable rich in vitamin C.",
    "Beet": "A root vegetable rich in iron and antioxidants.",

    # 💻 Programming Languages
    "Python": "A high-level, general-purpose language known for simplicity and readability. Widely used in AI, data science, and web development. Created by Guido van Rossum in 1991.",
    "HTML": "HyperText Markup Language. The standard language for creating web pages. Not a programming language but a markup language.",
    "CSS": "Cascading Style Sheets. A style sheet language used to describe the presentation of HTML documents. Controls layout, colors, and fonts.",
    "JS": "Short for JavaScript. A lightweight interpreted language used for interactive web pages.",
    "JavaScript": "A lightweight, interpreted programming language. The core language of the web alongside HTML and CSS. Used for interactive web pages and Node.js backend.",
    "TS": "Short for TypeScript. A strongly typed superset of JavaScript.",
    "TypeScript": "A strongly typed superset of JavaScript developed by Microsoft. Adds static typing to JavaScript. Compiles to plain JavaScript.",
    "Java": "A class-based, object-oriented language designed to be platform-independent. Famous for 'Write Once, Run Anywhere'. Used in Android, enterprise, and backend development.",
    "C": "A general-purpose, procedural language created in 1972. The foundation of modern programming. Used in operating systems and embedded systems.",
    "C+": "Not a standard language. Informally refers to a step between C and C++.",
    "C++": "An extension of C with object-oriented features. Used in game development, system software, and high-performance applications. Created by Bjarne Stroustrup.",
    "C#": "A modern, object-oriented language developed by Microsoft. Used heavily in game development with Unity and enterprise applications on .NET.",
    "C Plus": "Another way to refer to C+. See C+.",
    "C Plus Plus": "Another way to refer to C++. See C++.",
    "C Sharp": "Another way to refer to C#. See C#.",
    "Go": "A statically typed, compiled language designed by Google. Known for simplicity, fast compilation, and strong concurrency support via goroutines.",
    "Golang": "Another name for the Go programming language. Designed at Google for scalable server-side development.",
    "IronPython": "An implementation of Python running on the .NET framework. Allows Python code to interoperate with .NET libraries.",
    "PyPy": "A fast alternative implementation of Python using Just-In-Time (JIT) compilation. Often much faster than standard CPython.",
    "PHP": "A server-side scripting language designed for web development. Powers over 75% of websites including WordPress.",
    "Ruby": "A dynamic, object-oriented language known for elegant syntax. Famous for the Ruby on Rails web framework.",
    "Bash": "A Unix shell and command language. Used for scripting and automating tasks in Linux/macOS environments. Stands for Bourne Again SHell.",
    "Shell": "A general term for command-line interpreters like Bash, Zsh, or Fish. Used to interact with the operating system.",
    "Perl": "A high-level, general-purpose language known for text processing. Once widely used for CGI scripts and system administration.",
    "Rust": "A systems programming language focused on safety, speed, and concurrency. Prevents memory errors at compile time.",
    "Zig": "A low-level systems language aimed at being a modern replacement for C. Focuses on simplicity and explicit memory management.",
    "Carbon": "An experimental successor to C++ developed by Google. Designed for performance-critical code with modern language features.",
    "Whenever": "An esoteric programming language where statements run in non-deterministic order. The interpreter decides when to execute each line.",
    "Chef": "An esoteric language where programs look like cooking recipes. Variables are ingredients and operations are cooking steps.",
    "Piet": "An esoteric language where programs are images made of colored pixels. Named after the artist Piet Mondrian.",
    "Brainfrick": "A minimalist esoteric language with only 8 commands. Extremely hard to write but Turing complete.",
    "Befunge": "An esoteric language where code runs in 2D space. The program counter can move up, down, left, or right through the code.",
    "Deadfish": "An esoteric language with only 4 commands: increment, decrement, square, and output.",
    "R": "A language and environment for statistical computing and graphics. Widely used by statisticians and data scientists.",

    # ⚗️ Periodic Table
    "Hydrogen": "Symbol: H | Atomic Number: 1 | A colorless, odorless gas. The lightest and most abundant element in the universe.",
    "Helium": "Symbol: He | Atomic Number: 2 | A colorless noble gas. Used in balloons and cooling MRI machines.",
    "Lithium": "Symbol: Li | Atomic Number: 3 | A soft, silvery metal. Used in batteries and psychiatric medication.",
    "Beryllium": "Symbol: Be | Atomic Number: 4 | A hard, lightweight metal. Used in aerospace and X-ray equipment.",
    "Boron": "Symbol: B | Atomic Number: 5 | A metalloid used in glass, ceramics, and nuclear reactors.",
    "Nitrogen": "Symbol: N | Atomic Number: 7 | Makes up 78% of Earth's atmosphere. Used in fertilizers and refrigeration.",
    "Oxygen": "Symbol: O | Atomic Number: 8 | Essential for breathing and combustion. Makes up 21% of Earth's atmosphere.",
    "Fluorine": "Symbol: F | Atomic Number: 9 | The most reactive element. Used in toothpaste and Teflon coatings.",
    "Neon": "Symbol: Ne | Atomic Number: 10 | A noble gas used in neon signs and lasers.",
    "Sodium": "Symbol: Na | Atomic Number: 11 | A soft, reactive metal. Essential for human body. Found in table salt.",
    "Magnesium": "Symbol: Mg | Atomic Number: 12 | A lightweight metal used in alloys, fireworks, and supplements.",
    "Aluminum": "Symbol: Al | Atomic Number: 13 | A lightweight, corrosion-resistant metal. Used in packaging and transport.",
    "Silicon": "Symbol: Si | Atomic Number: 14 | A metalloid used in computer chips, solar cells, and glass.",
    "Phosphorus": "Symbol: P | Atomic Number: 15 | Essential for life, found in DNA and bones. Used in fertilizers.",
    "Sulfur": "Symbol: S | Atomic Number: 16 | A yellow nonmetal used in gunpowder and sulfuric acid production.",
    "Chlorine": "Symbol: Cl | Atomic Number: 17 | Used in water purification, bleach, and PVC plastic.",
    "Argon": "Symbol: Ar | Atomic Number: 18 | A noble gas used in welding and light bulbs.",
    "Potassium": "Symbol: K | Atomic Number: 19 | An essential mineral for the human body. Used in fertilizers.",
    "Calcium": "Symbol: Ca | Atomic Number: 20 | Essential for bones and teeth. Used in cement and supplements.",
    "Scandium": "Symbol: Sc | Atomic Number: 21 | A rare metal used in aerospace alloys and sports equipment.",
    "Titanium": "Symbol: Ti | Atomic Number: 22 | A strong, lightweight metal. Used in aerospace and implants.",
    "Vanadium": "Symbol: V | Atomic Number: 23 | A hard metal used in steel alloys and batteries.",
    "Chromium": "Symbol: Cr | Atomic Number: 24 | A shiny metal used in stainless steel and chrome plating.",
    "Manganese": "Symbol: Mn | Atomic Number: 25 | Used in steel production and batteries.",
    "Iron": "Symbol: Fe | Atomic Number: 26 | The most used metal in the world. Essential for blood (hemoglobin).",
    "Cobalt": "Symbol: Co | Atomic Number: 27 | Used in lithium-ion batteries and blue pigments.",
    "Nickel": "Symbol: Ni | Atomic Number: 28 | A corrosion-resistant metal used in stainless steel and batteries.",
    "Copper": "Symbol: Cu | Atomic Number: 29 | An excellent conductor of electricity. Used in wiring and plumbing.",
    "Zinc": "Symbol: Zn | Atomic Number: 30 | Used in galvanizing steel and as a dietary supplement.",
    "Gallium": "Symbol: Ga | Atomic Number: 31 | A metal that melts in your hand. Used in LEDs and semiconductors.",
    "Germanium": "Symbol: Ge | Atomic Number: 32 | A metalloid used in fiber optics and early transistors.",
    "Arsenic": "Symbol: As | Atomic Number: 33 | A toxic metalloid used in semiconductors and wood preservation.",
    "Selenium": "Symbol: Se | Atomic Number: 34 | Used in solar cells and as a dietary antioxidant.",
    "Bromine": "Symbol: Br | Atomic Number: 35 | A reddish-brown liquid halogen used in flame retardants.",
    "Krypton": "Symbol: Kr | Atomic Number: 36 | A noble gas used in high-performance light bulbs and lasers.",
    "Rubidium": "Symbol: Rb | Atomic Number: 37 | A soft, reactive metal used in atomic clocks.",
    "Strontium": "Symbol: Sr | Atomic Number: 38 | Used in fireworks (red color) and bone research.",
    "Yttrium": "Symbol: Y | Atomic Number: 39 | Used in LEDs, cancer treatment, and superconductors.",
    "Zirconium": "Symbol: Zr | Atomic Number: 40 | Used in nuclear reactors and cubic zirconia gemstones.",
    "Niobium": "Symbol: Nb | Atomic Number: 41 | Used in superconducting magnets and steel alloys.",
    "Molybdenum": "Symbol: Mo | Atomic Number: 42 | Used in high-strength steel alloys and oil refining catalysts.",
    "Technetium": "Symbol: Tc | Atomic Number: 43 | The first artificially produced element. Used in nuclear medicine.",
    "Ruthenium": "Symbol: Ru | Atomic Number: 44 | A rare platinum-group metal used in electrical contacts.",
    "Rhodium": "Symbol: Rh | Atomic Number: 45 | One of the rarest metals. Used in catalytic converters.",
    "Palladium": "Symbol: Pd | Atomic Number: 46 | Used in catalytic converters and hydrogen purification.",
    "Silver": "Symbol: Ag | Atomic Number: 47 | The best electrical conductor. Used in jewelry and electronics.",
    "Cadmium": "Symbol: Cd | Atomic Number: 48 | Used in rechargeable batteries. Toxic to humans.",
    "Indium": "Symbol: In | Atomic Number: 49 | Used in touchscreens and LCD displays.",
    "Tin": "Symbol: Sn | Atomic Number: 50 | Used in food cans, solder, and bronze alloys.",
    "Antimony": "Symbol: Sb | Atomic Number: 51 | Used in flame retardants and lead-acid batteries.",
    "Tellurium": "Symbol: Te | Atomic Number: 52 | Used in solar panels and thermoelectric devices.",
    "Iodine": "Symbol: I | Atomic Number: 53 | Essential for thyroid function. Used in antiseptics.",
    "Xenon": "Symbol: Xe | Atomic Number: 54 | A noble gas used in flash lamps and ion propulsion engines.",
    "Cesium": "Symbol: Cs | Atomic Number: 55 | Used in atomic clocks and oil drilling.",
    "Barium": "Symbol: Ba | Atomic Number: 56 | Used in X-ray imaging and fireworks (green color).",
    "Lanthanum": "Symbol: La | Atomic Number: 57 | A rare earth metal used in camera lenses and hybrid car batteries.",
    "Cerium": "Symbol: Ce | Atomic Number: 58 | The most abundant rare earth metal. Used in catalytic converters.",
    "Praseodymium": "Symbol: Pr | Atomic Number: 59 | Used in strong permanent magnets and aircraft engines.",
    "Neodymium": "Symbol: Nd | Atomic Number: 60 | Used in the strongest permanent magnets in headphones and EVs.",
    "Promethium": "Symbol: Pm | Atomic Number: 61 | A radioactive rare earth metal used in nuclear batteries.",
    "Samarium": "Symbol: Sm | Atomic Number: 62 | Used in samarium-cobalt magnets and cancer treatment.",
    "Europium": "Symbol: Eu | Atomic Number: 63 | Used in red and blue phosphors in TV screens.",
    "Gadolinium": "Symbol: Gd | Atomic Number: 64 | Used as MRI contrast agent and in nuclear reactor control rods.",
    "Terbium": "Symbol: Tb | Atomic Number: 65 | Used in green phosphors for displays.",
    "Dysprosium": "Symbol: Dy | Atomic Number: 66 | Used in neodymium magnets for high-temperature performance.",
    "Holmium": "Symbol: Ho | Atomic Number: 67 | Has the strongest magnetic moment of any element. Used in lasers.",
    "Erbium": "Symbol: Er | Atomic Number: 68 | Used in fiber optic amplifiers and pink colorant in glass.",
    "Thulium": "Symbol: Tm | Atomic Number: 69 | The rarest stable rare earth element. Used in portable X-ray devices.",
    "Ytterbium": "Symbol: Yb | Atomic Number: 70 | Used in atomic clocks and lasers.",
    "Lutetium": "Symbol: Lu | Atomic Number: 71 | The heaviest rare earth metal. Used in PET scan detectors.",
    "Hafnium": "Symbol: Hf | Atomic Number: 72 | Used in nuclear reactor control rods and semiconductors.",
    "Tantalum": "Symbol: Ta | Atomic Number: 73 | Used in capacitors for smartphones and surgical implants.",
    "Tungsten": "Symbol: W | Atomic Number: 74 | The highest melting point of all metals. Used in light bulb filaments.",
    "Rhenium": "Symbol: Re | Atomic Number: 75 | One of the rarest elements. Used in jet engine turbine blades.",
    "Osmium": "Symbol: Os | Atomic Number: 76 | The densest naturally occurring element. Used in fountain pen tips.",
    "Iridium": "Symbol: Ir | Atomic Number: 77 | The most corrosion-resistant metal. Used in spark plugs.",
    "Platinum": "Symbol: Pt | Atomic Number: 78 | A precious metal used in catalytic converters and jewelry.",
    "Gold": "Symbol: Au | Atomic Number: 79 | A precious yellow metal used in jewelry and electronics.",
    "Mercury": "Symbol: Hg | Atomic Number: 80 | The only metal liquid at room temperature. Used in thermometers.",
    "Thallium": "Symbol: Tl | Atomic Number: 81 | A toxic metal used in electronics and glass.",
    "Lead": "Symbol: Pb | Atomic Number: 82 | A dense, toxic metal. Used in batteries and radiation shielding.",
    "Bismuth": "Symbol: Bi | Atomic Number: 83 | A brittle metal used in cosmetics and low-melting alloys.",
    "Polonium": "Symbol: Po | Atomic Number: 84 | A highly radioactive element used in antistatic devices.",
    "Astatine": "Symbol: At | Atomic Number: 85 | The rarest naturally occurring element. Used in cancer research.",
    "Radon": "Symbol: Rn | Atomic Number: 86 | A radioactive noble gas. A health hazard in buildings.",
    "Francium": "Symbol: Fr | Atomic Number: 87 | The second rarest natural element. Highly radioactive.",
    "Radium": "Symbol: Ra | Atomic Number: 88 | A radioactive metal discovered by Marie Curie.",
    "Actinium": "Symbol: Ac | Atomic Number: 89 | A radioactive metal used in cancer treatment research.",
    "Thorium": "Symbol: Th | Atomic Number: 90 | A radioactive metal considered a safer nuclear fuel alternative.",
    "Protactinium": "Symbol: Pa | Atomic Number: 91 | A rare, toxic radioactive metal with few practical applications.",
    "Uranium": "Symbol: U | Atomic Number: 92 | A radioactive metal used as fuel in nuclear power plants.",
    "Neptunium": "Symbol: Np | Atomic Number: 93 | The first synthetic transuranium element. Used in neutron detection.",
    "Plutonium": "Symbol: Pu | Atomic Number: 94 | A radioactive metal used in nuclear weapons and reactors.",
    "Americium": "Symbol: Am | Atomic Number: 95 | A synthetic radioactive element used in smoke detectors.",
    "Curium": "Symbol: Cm | Atomic Number: 96 | Named after Marie and Pierre Curie. Used in Mars rover instruments.",
    "Berkelium": "Symbol: Bk | Atomic Number: 97 | A synthetic radioactive element named after Berkeley, California.",
    "Californium": "Symbol: Cf | Atomic Number: 98 | Used in nuclear reactor startup and cancer treatment.",
    "Einsteinium": "Symbol: Es | Atomic Number: 99 | Named after Albert Einstein. A synthetic radioactive element.",
    "Fermium": "Symbol: Fm | Atomic Number: 100 | Named after Enrico Fermi. A synthetic radioactive element.",
    "Mendelevium": "Symbol: Md | Atomic Number: 101 | Named after Dmitri Mendeleev, creator of the periodic table.",
    "Nobelium": "Symbol: No | Atomic Number: 102 | Named after Alfred Nobel. A synthetic radioactive element.",
    "Lawrencium": "Symbol: Lr | Atomic Number: 103 | Named after Ernest Lawrence. The last actinide element.",
    "Rutherfordium": "Symbol: Rf | Atomic Number: 104 | Named after Ernest Rutherford. A synthetic transactinide element.",
    "Dubnium": "Symbol: Db | Atomic Number: 105 | Named after Dubna, Russia. A synthetic highly radioactive element.",
    "Seaborgium": "Symbol: Sg | Atomic Number: 106 | Named after Glenn Seaborg. A synthetic radioactive element.",
    "Bohrium": "Symbol: Bh | Atomic Number: 107 | Named after Niels Bohr. A synthetic radioactive element.",
    "Hassium": "Symbol: Hs | Atomic Number: 108 | Named after Hesse, Germany. A synthetic radioactive element.",
    "Meitnerium": "Symbol: Mt | Atomic Number: 109 | Named after Lise Meitner. A synthetic radioactive element.",
    "Darmstadtium": "Symbol: Ds | Atomic Number: 110 | Named after Darmstadt, Germany. A synthetic radioactive element.",
    "Roentgenium": "Symbol: Rg | Atomic Number: 111 | Named after Wilhelm Röntgen, discoverer of X-rays.",
    "Copernicium": "Symbol: Cn | Atomic Number: 112 | Named after Nicolaus Copernicus. A synthetic radioactive element.",
    "Nihonium": "Symbol: Nh | Atomic Number: 113 | Named after Japan (Nihon). First element discovered in Asia.",
    "Flerovium": "Symbol: Fl | Atomic Number: 114 | Named after Flerov Laboratory in Russia.",
    "Moscovium": "Symbol: Mc | Atomic Number: 115 | Named after Moscow. A synthetic radioactive element.",
    "Livermorium": "Symbol: Lv | Atomic Number: 116 | Named after Livermore, California.",
    "Tennessine": "Symbol: Ts | Atomic Number: 117 | Named after Tennessee. A synthetic radioactive halogen.",
    "Oganesson": "Symbol: Og | Atomic Number: 118 | Named after Yuri Oganessian. The heaviest known element.",
    #🧬biology
    "Cell": "The cell is the basic structural and functional unit of all forms of life or organisms. The term comes from the Latin word cellula meaning 'small room'. A biological cell basically consists of a semipermeable cell membrane enclosing cytoplasm that contains genetic material. Most cells are only visible under a microscope. Except for highly-differentiated cell types (examples include red blood cells and gametes) most cells are capable of replication, and protein synthesis. Some types of cell are motile. Cells emerged on Earth about 4 billion years ago.",
    "DNA": "Deoxyribonucleic acid (pronunciationⓘ;[1] DNA) is a polymer composed of two polynucleotide chains that coil around each other to form a double helix. The polymer carries genetic instructions for the development, functioning, growth and reproduction of all known organisms and many viruses. DNA and ribonucleic acid (RNA) are nucleic acids. Alongside proteins, lipids and complex carbohydrates (polysaccharides), nucleic acids are one of the four major types of macromolecules that are essential for all known forms of life.",
    "brain": "The brain is an organ that serves as the center of the nervous system in all vertebrate and most invertebrate animals. It consists of nervous tissue and is typically located in the head (cephalization), usually near organs for special senses such as vision, hearing, and olfaction. Being the most specialized organ, it is responsible for receiving information from the sensory nervous system, processing that information (thought, cognition, and intelligence) and the coordination of motor control (muscle activity and endocrine system).",
    "Skeleton": "A skeleton is the structural frame that supports the body of most animals. There are several types of skeletons, including the exoskeleton, which is a rigid outer shell that holds up an organism's shape; the endoskeleton, a rigid internal frame to which the organs and soft tissues attach; and the hydroskeleton, a flexible internal structure supported by the hydrostatic pressure of body fluids.",
    "heart": "The heart is a muscular organ found in humans and other animals. This organ pumps blood through the blood vessels.[1] The heart and blood vessels together make up the circulatory system.[2] The pumped blood carries oxygen and nutrients to the tissue, while carrying metabolic waste such as carbon dioxide to the lungs.[3] In humans, the heart is approximately the size of a closed fist and is located between the lungs, in the middle compartment of the chest, called the mediastinum.",
    "stomach": "The stomach is a muscular, hollow organ in the upper gastrointestinal tract of humans and many other animals, including several invertebrates. The Ancient Greek name for the stomach is gaster which is used as gastric in medical terms related to the stomach.[3] The stomach has a dilated structure and functions as a vital organ in the digestive system. The stomach is involved in the gastric phase of digestion, following the cephalic phase in which the sight and smell of food and the act of chewing are stimuli. In the stomach a chemical breakdown of food takes place by means of secreted digestive enzymes and gastric acid. It also plays a role in regulating gut microbiota, influencing digestion and overall health.[4] The stomach is located between the esophagus and the small intestine. The pyloric sphincter controls the passage of partially digested food (chyme) from the stomach into the duodenum, the first and shortest part of the small intestine, where peristalsis takes over to move this through the rest of the intestines.",
    "lung": "The lungs are the primary organs of the respiratory system in many animals, including humans. In mammals and most other tetrapods, two lungs are located near the backbone on either side of the heart. Their function in the respiratory system is to extract oxygen from the atmosphere and transfer it into the bloodstream, and to release carbon dioxide from the bloodstream into the atmosphere, in a process of gas exchange. Respiration is driven by different muscular systems in different species. Mammals, reptiles and birds use their musculoskeletal systems to support and foster breathing. In early tetrapods, air was driven into the lungs by the pharyngeal muscles via buccal pumping, a mechanism still seen in amphibians. In humans, the primary muscle that drives breathing is the diaphragm. The lungs also provide airflow that makes vocalisation including speech possible.Humans have two lungs, a right lung and a left lung. They are situated within the thoracic cavity of the chest. The right lung is bigger than the left, and the left lung shares space in the chest with the heart. The lungs together weigh approximately 1.3 kilograms (2.9 lb), and the right is heavier. The lungs are part of the lower respiratory tract that begins at the trachea and branches into the bronchi and bronchioles, which receive air breathed in via the conducting zone. These divide until air reaches microscopic alveoli, where gas exchange takes place. Together, the lungs contain approximately 2,400 kilometers (1,500 mi) of airways and 300 to 500 million alveoli. Each lung is enclosed within a pleural sac of two pleurae which allows the inner and outer walls to slide over each other whilst breathing takes place, without much friction. The inner visceral pleura divides each lung as fissures into sections called lobes. The right lung has three lobes and the left has two. The lobes are further divided into bronchopulmonary segments and lobules. The lungs have a unique blood supply, receiving deoxygenated blood sent from the heart to receive oxygen (the pulmonary circulation) and a separate supply of oxygenated blood (the bronchial circulation). The tissue of the lungs can be affected by several respiratory diseases including pneumonia and lung cancer. Chronic diseases such as chronic obstructive pulmonary disease and emphysema can be related to smoking or exposure to harmful substances. Diseases such as bronchitis can also affect the respiratory tract. Medical terms related to the lung often begin with pulmo-, from the Latin pulmonarius (of the lungs) as in pulmonology, or with pneumo- (from Greek πνεύμων lung) as in pneumonia. In embryonic development, the lungs begin to develop as an outpouching of the foregut, a tube which goes on to form the upper part of the digestive system. When the lungs are formed the fetus is held in the fluid-filled amniotic sac and so they do not function to breathe. Blood is also diverted from the lungs through the ductus arteriosus. At birth however, air begins to pass through the lungs, and the diversionary duct closes so that the lungs can begin to respire.",
    "Eye": "An eye is a sensory organ that allows an organism to perceive visual information. It detects light and converts it into electro-chemical impulses in neurons (neurones). It is part of an organism's visual system.In higher organisms, the eye is a complex optical system that collects light from the surrounding environment, regulates its intensity through a diaphragm, focuses it through an adjustable assembly of lenses to form an image, converts this image into a set of electrical signals, and transmits these signals to the brain through neural pathways that connect the eye via the optic nerve to the visual cortex and other areas of the brain.Eyes with resolving power have come in ten fundamentally different forms, classified into compound eyes and non-compound eyes. Compound eyes are made up of multiple small visual units, and are common on insects and crustaceans. Non-compound eyes have a single lens and focus light onto the retina to form a single image. This type of eye is common in mammals, including humans. The simplest eyes are pit eyes. They are eye-spots which may be set into a pit to reduce the angle of light that enters and affects the eye-spot, to allow the organism to deduce the angle of incoming light.[1]Eyes enable several photo response functions that are independent of vision. In an organism that has more complex eyes, retinal photosensitive ganglion cells send signals along the retinohypothalamic tract to the suprachiasmatic nuclei to effect circadian adjustment and to the pretectal area to control the pupillary light reflex.",
    "arm": "In human anatomy, the arm refers to the upper limb in common usage, although academically the term specifically means the upper arm[1][2] between the glenohumeral joint (shoulder joint) and the elbow joint. The distal part of the upper arm between the elbow and the radiocarpal joint (wrist joint) is known as the forearm or lower arm, and the extremity beyond the wrist is the hand.",
    "leg": "A leg is a weight-bearing and locomotive anatomical structure, usually having a columnar shape. During locomotion, legs function as extensible struts.[1] The combination of movements at all joints can be modeled as a single, linear element capable of changing length and rotating about an omnidirectional hip joint.As an anatomical animal structure, it is used for locomotion. The distal end is often modified to distribute force (such as a foot). Most animals have an even number of legs.As a component of furniture, it is used for the economy of materials needed to provide the support for the useful surface, such as the table top or chair seat.",
    "teeth": "A tooth (pl.: teeth) is a hard, calcified structure found in the jaws (or mouths) of many vertebrates and used to break down food. Some animals, particularly carnivores and omnivores, also use teeth to help with capturing or wounding prey, tearing food, for defensive purposes, to intimidate other animals often including their own, or to carry prey or their young. The roots of teeth are covered by gums. Teeth are not made of bone, but rather of multiple tissues of varying density and hardness that originate from the outermost embryonic germ layer, the ectoderm.",
    "pancreas": "The pancreas (plural pancreases, or pancreata) is an organ of the digestive system and endocrine system of vertebrates. In humans, it is located in the abdomen behind the stomach and functions as a gland. The pancreas is a mixed or heterocrine gland, i.e., it has both an endocrine and a digestive exocrine function.[2] Ninety-nine percent of the pancreas is exocrine and 1% is endocrine.[3][4][5][6] As an endocrine gland, it functions mostly to regulate blood sugar levels, secreting the hormones insulin, glucagon, somatostatin and pancreatic polypeptide. As a part of the digestive system, it functions as an exocrine gland secreting pancreatic juice into the duodenum through the pancreatic duct. This juice contains bicarbonate, which neutralizes acid entering the duodenum from the stomach; and digestive enzymes, which break down carbohydrates, proteins, and fats in food entering the duodenum from the stomach.",
    "Liver": "The liver is a major metabolic organ exclusively found in vertebrates, which performs many essential biological functions such as detoxification of the organism, and the synthesis of various proteins and various other biochemicals necessary for digestion and growth.[2][3][4] In humans, it is located in the right upper quadrant of the abdomen, below the diaphragm and mostly shielded by the lower right rib cage. Its other metabolic roles include carbohydrate metabolism, the production of a number of hormones, conversion and storage of nutrients such as glucose and glycogen, and the decomposition of red blood cells.[4] Anatomical and medical terminology often use the prefix hepat- from ἡπατο-, from the Greek word for liver, such as hepatology, and hepatitis.[5]",
    "kidney": "In humans, the kidneys are two reddish-brown bean-shaped blood-filtering organs[1] that are a multilobar, multipapillary form of mammalian kidneys, usually without signs of external lobulation.[2][3] They are located on the left and right in the retroperitoneal space, and in adult humans are about 12 centimetres (4+1⁄2 inches) in length.[4][5] They receive blood from the paired renal arteries; blood exits into the paired renal veins. Each kidney is attached to a ureter, a tube that carries excreted urine to the bladder.",
    "bladder": "The bladder (from Old English blædre 'bladder, blister, pimple') is a hollow organ in humans and other vertebrates that stores urine from the kidneys. In placental mammals, urine enters the bladder via the ureters and exits via the urethra during urination.[1][2] In humans, the bladder is a distensible organ that sits on the pelvic floor. The typical adult human bladder will hold between 300 and 500 ml (10 and 17 fl oz) before the urge to empty occurs, but can hold considerably more.[3][4]",
    "mucle": "Muscle is a specialised soft tissue, one of the four basic types of animal tissues. There are three types of muscle tissues in vertebrates: skeletal muscle tissue, cardiac muscle tissue, and smooth muscle tissue. Muscle tissue gives skeletal muscles the ability to contract and relax. Muscle tissue contains special contractile proteins called actin and myosin which interact to cause movement. Among many other muscle proteins present are two regulatory proteins, troponin and tropomyosin.[1] Muscle is formed during embryonic development, in a process known as myogenesis.[2]",
    "skin": "Skin is the layer of usually soft, flexible outer tissue covering the body of a vertebrate animal, with three main functions: protection, regulation, and sensation.",
    "animal": "Animals are multicellular, eukaryotic organisms belonging to the biological kingdom Animalia (/ˌænɪˈmeɪliə/[4]). With few exceptions, animals consume organic material, breathe oxygen, have myocytes and are able to move, can reproduce sexually, and grow from a hollow sphere of cells, the blastula, during embryonic development. Animals form a clade, meaning that they arose from a single common ancestor. Over 1.5 million living animal species have been described, of which around 1.05 million are insects, over 85,000 are molluscs, and around 65,000 are vertebrates. It has been estimated there are as many as 7.77 million animal species on Earth. Animal body lengths range from 8.5 μm (0.00033 in) to 33.6 m (110 ft). They have complex ecologies and interactions with each other and their environments, forming intricate food webs. The scientific study of animals is known as zoology, and the study of animal behaviour is known as ethology.",
    "human": "Humans (Homo sapiens, meaning 'thinking man' or 'wise man') are the most abundant and widespread species of primates, characterized by bipedality, hairlessness, and large, complex brains enabling the development of advanced technology, culture, and language. Humans are highly social beings and tend to live in complex social structures composed of many cooperating and competing groups, from families and kinship networks to political states. Social interactions between humans have established a wide variety of values, social norms, and rituals, which bolster human society. Curiosity and the human desire to understand and influence the environment have motivated humanity's development of science, philosophy, religion, mythology and other fields of knowledge.",
    "plant": "Plants are the eukaryotic organisms that constitute the kingdom Plantae. They are predominantly photosynthetic, meaning that they obtain their energy from sunlight. They do that using the green pigment chlorophyll in their chloroplasts to produce sugars from carbon dioxide and water. Exceptions are parasitic plants that have lost the genes for chlorophyll and photosynthesis, and obtain their energy from other plants or fungi. Most plants are multicellular, except for some green algae."
}

entry_var = tk.StringVar()

# 🔍 Search bar
search_frame = tk.Frame(root, bg="#b1b1b1")
search_frame.pack(pady=20, padx=20, fill="x")

tk.Label(search_frame, text="🔍", bg="#b1b1b1", fg="white", font=("Arial", 14)).pack(side="left")
entry = tk.Entry(search_frame, textvariable=entry_var, font=("Arial", 14), bg="#3d3d3d", fg="white",
                 insertbackground="white", relief="flat", bd=5)
entry.pack(side="left", fill="x", expand=True, ipady=5)

# 📋 Results listbox
list_frame = tk.Frame(root, bg="#000000")
list_frame.pack(padx=20, fill="both", expand=True)

listbox = tk.Listbox(list_frame, font=("Arial", 12), bg="#181818", fg="white",
                     selectbackground="#000000", relief="flat", bd=0, activestyle="none")
listbox.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)

# ℹ️ Info box
info_box = tk.Text(root, font=("Arial", 12), bg="#2d2d2d", fg="#000000", height=6,
                   relief="flat", bd=10, wrap="word", state="disabled")
info_box.pack(padx=20, pady=10, fill="x")

# 📌 Show info on click
def show_info(event):
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        try:
            n = int(item)
            is_even = "Even" if n % 2 == 0 else "Odd"
            is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
            prime_str = "Prime ✅" if is_prime else "Not Prime ❌"
            factorial_str = str(math.factorial(n)) if n <= 20 else "Too large to display"
            info = (f"Number: {n}\n"
                    f"Even/Odd: {is_even}\n"
                    f"Prime: {prime_str}\n"
                    f"Square: {n**2} | Square Root: {round(n**0.5, 4)}\n"
                    f"Factorial: {factorial_str}")
            icon = "🔢"
        except ValueError:
            info = data.get(item, "No information available.")
            icon = "💡" if item in [k for k in data if k in [
                "Python","HTML","CSS","JS","JavaScript","TS","TypeScript","Java",
                "C","C+","C++","C#","Go","Golang","IronPython","PyPy","PHP","Ruby",
                "Bash","Shell","Perl","Rust","Zig","Carbon","Whenever","Chef","Piet",
                "Brainfrick","Befunge","Deadfish","R","C Plus","C Plus Plus","C Sharp"
            ]] else "🌿"

        info_box.config(state="normal")
        info_box.delete("1.0", tk.END)
        info_box.insert("1.0", f"{icon} {item}\n{info}")
        info_box.config(state="disabled")

# 🔄 Update search results
def update_search(*args):
    search_term = entry_var.get().strip()
    listbox.delete(0, tk.END)
    if search_term:
        # 🔢 Check if it's a number
        try:
            n = int(search_term)
            listbox.insert(tk.END, str(n))
        except ValueError:
            pass
        # 🔤 Search data dictionary
        for item in data:
            if search_term.lower() in item.lower():
                listbox.insert(tk.END, item)

entry_var.trace("w", update_search)
listbox.bind("<<ListboxSelect>>", show_info)

root.mainloop()