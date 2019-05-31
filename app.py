
#!/usr/bin/python

from flask import Flask, request, make_response, jsonify
import requests

app = Flask(__name__)

# *****************************
# Course Data
# *****************************
CourseNames = {

'certified business analysis professional preparatory course':'Certified Business Analysis Professional Preparatory Course',
'certified scrum product owner':'Certified Scrum Product Owner',
'citrep+':'CITREP+',
'enterprise architecture practicum - aop':'Enterprise Architecture Practicum - AOP',
'lean it foundation certification':'Lean IT Foundation Certification',
'ccsp cbk training seminar':'CCSP CBK Training Seminar',
'cissp cbk training seminar':'CISSP CBK Training Seminar',
'csslp cbk training seminar':'CSSLP CBK Training Seminar',
'advanced customer analytics':'Advanced Customer Analytics',
'agile testing':'Agile Testing',
'aisp qualified information security professional course':'AISP Qualified Information Security Professional Course',
'architecting iot solutions':'Architecting IoT Solutions',
'architecting software solutions':'Architecting Software Solutions',
'big data engineering for analytics':'Big Data Engineering for Analytics',
'business agility bootcamp':'Business Agility Bootcamp',
'business analysis for agile practitioners':'Business Analysis for Agile Practitioners',
'business process reengineering':'Business Process Reengineering',
'campaign analytics':'Campaign Analytics',
'certified enterprise architecture practitioner course':'Certified Enterprise Architecture Practitioner Course',
'certified less practitioner - principles to practices':'Certified LeSS Practitioner - Principles to Practices',
'certified scrummaster':'Certified ScrumMaster',
'client side foundation':'Client Side Foundation',
'cloud native solution design':'Cloud Native Solution Design',
'cobit 5 foundation':'COBIT 5 Foundation',
'communicating and managing change':'Communicating and Managing Change',
'containers for deploying and scaling apps':'Containers for Deploying and Scaling Apps',
'customer analytics':'Customer Analytics',
'cyber security for ict professionals':'Cyber Security for ICT Professionals',
'cybersecurity risk awareness':'Cybersecurity Risk Awareness',
'data analytics process and best practice':'Data Analytics Process and Best Practice',
'data and feature engineering for machine learning':'Data and Feature Engineering for Machine Learning',
'data driven decision making':'Data Driven Decision Making',
'data governance & protection':'Data Governance & Protection',
'data storytelling':'Data Storytelling',
'design secure mobile architecture':'Design Secure Mobile Architecture',
'designing cloud-enabled':'Designing Cloud-enabled',
'designing intelligent edge computing':'Designing Intelligent Edge Computing',
'developing smart urban iot solutions':'Developing Smart Urban IoT Solutions',
'devops engineering and automation':'DevOps Engineering and Automation',
'devops foundation with bizops':'DevOps Foundation with BizOps',
'digital & social engagement strategy':'Digital & Social Engagement Strategy',
'digital product strategy':'Digital Product Strategy',
'digital transformation planning':'Digital Transformation Planning',
'digital user experience design':'Digital User Experience Design',
'enterprise architecture masterclass':'Enterprise Architecture Masterclass',
'enterprise architecture practicum':'Enterprise Architecture Practicum',
'enterprise digital governance':'Enterprise Digital Governance',
'envisioning smart urban iot solutions':'Envisioning Smart Urban IoT Solutions',
'essential practices for agile teams':'Essential Practices for Agile Teams',
'feature engineering and analytics using iot data':'Feature Engineering and Analytics using IOT Data',
'feature extraction and supervised modeling with deep learning':'Feature Extraction and Supervised Modeling with Deep Learning',
'health analytics':'Health Analytics',
'humanizing smart systems':'Humanizing Smart Systems',
'innovation bootcamp':'Innovation Bootcamp',
'intelligent sensing and sense making':'Intelligent Sensing and Sense Making',
'introduction to blockchain & dlt for executives':'Introduction to Blockchain & DLT for Executives',
'continual service improvement certificate':'Continual Service Improvement Certificate',
'foundation certificate in it service management':'Foundation Certificate in IT Service Management',
'operational support and analysis certificate':'Operational Support and Analysis Certificate',
'release, control and validation certificate':'Release, Control and Validation Certificate',
'service offerings and agreements certificate':'Service Offerings and Agreements Certificate',
'machine reasoning':'Machine Reasoning',
'managing business analytics projects':'Managing Business Analytics Projects',
'managing cybersecurity risk':'Managing Cybersecurity Risk',
'mobile user experience design':'Mobile User Experience Design',
'new media and sentiment mining':'New Media and Sentiment Mining',
'object oriented analysis & design':'Object Oriented Analysis & Design',
'object oriented design patterns':'Object Oriented Design Patterns',
'pattern recognition and machine learning systems':'Pattern Recognition and Machine Learning Systems',
'persistence and analytics fundamentals':'Persistence and Analytics Fundamentals',
'platform engineering':'Platform Engineering',
'pmi agile certified practitioner':'PMI Agile Certified Practitioner',
'pmp for project managers':'PMP For Project Managers',
'portfolio, programme and project offices':'Portfolio, Programme and Project Offices',
'predictive analytics - insights of trends and irregularities':'Predictive Analytics - Insights of Trends and Irregularities',
'prince2':'PRINCE2',
'problem solving using pattern recognition':'Problem Solving using Pattern Recognition',
'product thinking for organisations':'Product Thinking for Organisations',
'python for data, ops and things':'Python for Data, Ops and Things',
'reasoning systems':'Reasoning Systems',
'recommender systems':'Recommender Systems',
'restful api design':'RESTful API Design',
'robotic systems':'Robotic Systems',
'secure software development lifecycle for agile':'Secure Software Development Lifecycle for Agile',
'securing iot':'Securing IoT',
'security notification and messaging fundamentals':'Security Notification and Messaging Fundamentals',
'sequence modeling with deep learning':'Sequence Modeling with Deep Learning',
'server side foundation':'Server Side Foundation',
'service design':'Service Design',
'social media analytics':'Social Media Analytics',
'spatial reasoning from sensor data':'Spatial Reasoning from Sensor Data',
'statistics bootcamp':'Statistics Bootcamp',
'statistics for business':'Statistics for Business',
'strategic business analysis':'Strategic Business Analysis',
'strategic design & innovation':'Strategic Design & Innovation',
'strategic futures & foresight':'Strategic Futures & Foresight',
'strategic product manager':'Strategic Product Manager',
'strategic product market fit':'Strategic Product Market Fit',
'supervised and unsupervised modeling with machine learning':'Supervised and Unsupervised Modeling with Machine Learning',
'systems thinking & root cause analysis':'Systems Thinking & Root Cause Analysis',
'technopreneurship':'Technopreneurship',
'text analytics':'Text Analytics',
'text processing using machine learning':'Text Processing using Machine Learning',
'vision systems':'Vision Systems',
'web analytics and seo':'Web Analytics and SEO',
'nus graduate diploma in systems analysis':'NUS Graduate Diploma in Systems Analysis',
'pmi agile certified practitioner ':'PMI Agile Certified Practitioner',
}

CourseLinks = {

'certified business analysis professional preparatory course':'https://www.iss.nus.edu.sg/executive-education/course/detail/certified-business-analysis-professional-(cbap)-preparatory-course',
'certified scrum product owner':'https://www.iss.nus.edu.sg/executive-education/course/detail/certified-scrum-product-owner-',
'citrep+':'https://www.iss.nus.edu.sg/executive-education/course/detail/certified-information-systems-security-professional--(cissp-exam-only)',
'enterprise architecture practicum - aop':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf---enterprise-architecture-practicum---aop-(sf)',
'lean it foundation certification':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf---lean-it-foundation-certification-(sf)',
'ccsp cbk training seminar':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--(isc)-ccsp-cbk-training-seminar-(sf)',
'cissp cbk training seminar':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--(isc)-cissp-cbk-training-seminar-(sf)',
'csslp cbk training seminar':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--(isc)-csslp-cbk-training-seminar-(sf)',
'advanced customer analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--advanced-customer-analytics-(sf)',
'agile testing':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--agile-testing-(sf)',
'aisp qualified information security professional course':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--aisp-qualified-information-security-professional-course-(sf)',
'architecting iot solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--architecting-iot-solutions-(sf)',
'architecting software solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--architecting-software-solutions-(sf)',
'big data engineering for analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--big-data-engineering-for-analytics-(sf)',
'business agility bootcamp':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf-business-agility-bootcamp',
'business analysis for agile practitioners':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--business-analysis-for-agile-practitioners-(sf)',
'business process reengineering':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--business-process-reengineering-(sf)',
'campaign analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf-campaign-analytics-(sf)',
'certified enterprise architecture practitioner course':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--certified-enterprise-architecture-practitioner-course-(sf)',
'certified less practitioner - principles to practices':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--certified-less-practitioner---principles-to-practices-(sf)',
'certified scrummaster':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--certified-scrummaster-(sf)',
'client side foundation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--client-side-foundation-(sf)',
'cloud native solution design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf---cloud-native-solution-design-(sf)',
'cobit 5 foundation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--cobit-5-foundation-(sf)',
'communicating and managing change':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--communicating-and-managing-change-(sf)',
'containers for deploying and scaling apps':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--containers-for-deploying-and-scaling-apps-(sf)',
'customer analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--customer-analytics-(sf)',
'cyber security for ict professionals':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--cyber-security-for-ict-professionals-(sf)',
'cybersecurity risk awareness':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--cybersecurity-risk-awareness-(sf)',
'data analytics process and best practice':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-analytics-process-and-best-practice-(sf)',
'data and feature engineering for machine learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-and-feature-engineering-for-machine-learning--(sf)',
'data driven decision making':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-driven-decision-making-(sf)',
'data governance & protection':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-governance-protection-(sf)',
'data storytelling':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-storytelling-(sf)',
'design secure mobile architecture':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--design-secure-mobile-architecture-(sf)',
'designing cloud-enabled':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--designing-cloud-enabled-mobile-applications-(sf)',
'designing intelligent edge computing':'https://www.iss.nus.edu.sg/executive-education/course/detail/designing-intelligent-edge-computing-SF',
'developing smart urban iot solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--developing-smart-urban-iot-solutions-(sf)',
'devops engineering and automation':'https://www.iss.nus.edu.sg/executive-education/course/detail/devops-engineering-and-automation-SF',
'devops foundation with bizops':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--devops-foundation-with-bizops-(sf)',
'digital & social engagement strategy':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-social-engagement-strategy-(sf)',
'digital product strategy':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-product-strategy-(sf)',
'digital transformation planning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-transformation-planning-(sf)',
'digital user experience design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-user-experience-design-(sf)',
'enterprise architecture masterclass':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--enterprise-architecture-masterclass-(sf)',
'enterprise architecture practicum':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--enterprise-architecture-practicum-(sf)',
'enterprise digital governance':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--enterprise-digital-governance-(sf)',
'envisioning smart urban iot solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--envisioning-smart-urban-iot-solutions-(sf)',
'essential practices for agile teams':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--essential-practices-for-agile-teams-(sf)',
'feature engineering and analytics using iot data':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--feature-engineering-and-analytics-using-iot-data-(sf)',
'feature extraction and supervised modeling with deep learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--feature-extraction-and-supervised-modeling-with-deep-learning-(sf)',
'health analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--health-analytics_(sf)',
'humanizing smart systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/humanizing-smart-systems-SF',
'innovation bootcamp':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--innovation-bootcamp-(sf)',
'intelligent sensing and sense making':'https://www.iss.nus.edu.sg/executive-education/course/detail/intelligent-sensing-and-sense-making',
'introduction to blockchain & dlt for executives':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--introduction-to-blockchain-dlt-for-executives-(sf)',
'continual service improvement certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/-nicf--itil%C3%A2-continual-service-improvement-certificate-(sf)',
'foundation certificate in it service management':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-foundation-certificate-in-it-service-management-(sf)',
'operational support and analysis certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-operational-support-and-analysis-certificate-(sf)',
'release, control and validation certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-release-control-and-validation-certificate-(sf)',
'service offerings and agreements certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-service-offerings-and-agreements-certificate-(sf)',
'machine reasoning':'https://www.iss.nus.edu.sg/executive-education/course/detail/machine-reasoning',
'managing business analytics projects':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--managing-business-analytics-projects-(sf)',
'managing cybersecurity risk':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--managing-cybersecurity-risk-(sf)',
'mobile user experience design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--mobile-user-experience-design-(sf)',
'new media and sentiment mining':'https://www.iss.nus.edu.sg/executive-education/course/detail/new-media-and-sentiment-mining-new',
'object oriented analysis & design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--object-oriented-analysis-design-(sf)',
'object oriented design patterns':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--object-oriented-design-patterns-(sf)',
'pattern recognition and machine learning systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/pattern-recognition-and-machine-learning-systems',
'persistence and analytics fundamentals':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--persistence-and-analytics-fundamentals-(sf)',
'platform engineering':'https://www.iss.nus.edu.sg/executive-education/course/detail/platform-engineering-SF',
'pmi agile certified practitioner':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--pmi-agile-certified-practitioner-(pmi-acp)-preparatory-course-acp-sf',
'pmp for project managers':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--pmp-for-project-managers-(sf)',
'portfolio, programme and project offices':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf-portfolio-programme-and-project-offices-(p3o)--foundation-practitioner',
'predictive analytics - insights of trends and irregularities':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--predictive-analytics---insights-of-trends-and-irregularities-(sf)',
'prince2':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--prince2-(projects-in-controlled-environments)---foundation-and-practitioner-certificate-(sf)',
'problem solving using pattern recognition':'https://www.iss.nus.edu.sg/executive-education/course/detail/problem-solving-using-pattern-recognition',
'product thinking for organisations':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--product-thinking-for-organisations-(sf)',
'python for data, ops and things':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--python-for-data-ops-and-things-(sf)',
'reasoning systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/reasoning-systems',
'recommender systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--recommender-systems-(sf)',
'restful api design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--restful-api-design-(sf)',
'robotic systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/robotic-systems',
'secure software development lifecycle for agile':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--design-secure-mobile-architecture-ssdla-sf',
'securing iot':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--securing-iot-(sf)',
'security notification and messaging fundamentals':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--security-notification-and-messaging-fundamentals-(sf)',
'sequence modeling with deep learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--sequence-modeling-with-deep-learning-(sf)',
'server side foundation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--server-side-foundation-(sf)',
'service design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--service-design-(sf)',
'social media analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--social-media-analytics-(sf)',
'spatial reasoning from sensor data':'https://www.iss.nus.edu.sg/executive-education/course/detail/spatial-reasoning-from-sensor-data',
'statistics bootcamp':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--statistics-bootcamp-(sf)',
'statistics for business':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--statistics-for-business-(sf)',
'strategic business analysis':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-business-analysis-(sf)',
'strategic design & innovation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-design-innovation-(sf)',
'strategic futures & foresight':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-futures-foresight-(sf)',
'strategic product manager':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-product-manager-(sf)',
'strategic product market fit':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-product-market-fit-(sf)',
'supervised and unsupervised modeling with machine learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--supervised-and-unsupervised-modeling-with-machine-learning-(sf)',
'systems thinking & root cause analysis':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--systems-thinking-root-cause-analysis-(sf)',
'technopreneurship':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--technopreneurship-(sf)',
'text analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--text-analytics-(sf)',
'text processing using machine learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/text-processing-using-machine-learning',
'vision systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/vision-systems',
'web analytics and seo':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--web-analytics-seo-(sf)',
'nus graduate diploma in systems analysis':'https://www.iss.nus.edu.sg/executive-education/course/detail/nus-graduate-diploma-in-systems-analysis-(sf)',
'pmi agile certified practitioner ':'https://www.iss.nus.edu.sg/executive-education/course/detail/pmi-agile-certified-practitioner--(pmi-acp-exam-only)',


}

TeachingStaffDesc = {
'angela huang':'Angela teaches and provides consulting services in the areas of information security, IT risk management and project management. She is a lead instructor for (ISC)2 CISSP CBK Review Seminar and the course manager for information security courses and selected project management courses at ISS.',
'ashok kumar seetharaman':'Ashok has over 35 years of ICT experience that spans across Government and Private sector organisations in Asia.  His primary domain of expertise and experience is on leadership and management of Digital Government Transformation, Design of Public Services and Innovation programs.',
'barry adrian shepherd':'Barry teaches Business Analytics, Data Mining and Knowledge Engineering at ISS and has over 30 years experience in these areas. Before joining ISS he was based in the US and specialized in web analytics and user response modeling for online ad targeting at Microsoft Display Advertising and in process optimization and data analytics for ecommerce order fulfillment at Amazon.com.',
'brandon ng':'Brandon is currently an Associate in Institute of Systems Science, National University of Singapore (NUS-ISS). He completed his study in Computer Science, major in Software Engineering and Artificial Intelligence. Under the NUS full time research scholarship sponsored by The Logistics Institute - Asia Pacific, he did research in Intelligent Transportation System for his master study.',
'brian ng':'Brian has 5 years of healthcare service improvement and innovation experience. Prior to joining NUS ISS, he was a pioneering member of Jurong Health Services, building a new integrated hospital and healthcare system in the west. He is a lean six sigma practitioner and has the experience facilitating large scale cross-functional hospital improvement projects. He has also led many business and technology innovation projects from prototyping devices to piloting new services and technologies.',
'chandrasekaran paramasivam':'Chandra has a wide experience in Software Quality Management as a SQA and SEPG involved in identifying, developing, implementing, verifying the adherence, assessing the effectiveness and improving of the organizational standard software processes with reference to the SW CMM & CMMI Dev Models, ISO 9001 quality system and RUP Framework. He has participated in the SEIs SW CMM - CBAIPI Assessments and CMMI - SCAMPI Class A Appraisals as an Appraisal Team Member. He has led the CMMI Implementation for the IT organizations to achieve the CMMI Maturity Level 3 & Maturity Level 5 and successfully completed the Intermediate Concept of CMMI Dev Model Certification with the excellent grade from Software Engineering Institute, Pittsburgh, USA.',
'charles pang':'Charles lectures and consults on artificial intelligence, knowledge engineering and knowledge management. He has been a principal investigator, project manager, supervisor and developer for many knowledge based systems project in Canada and Singapore. Previously, he was a research scientist with the Centre for Cold Ocean Resources Engineering in Canada where he researched and developed expert systems for the offshore oil and gas industry. He had also lectured at the Memorial University of Newfoundland (Marine Institute of Fisheries and Oceans) and at the Japan Singapore AI Centre. At NCB, Charles held several portfolios including the promotion of the software development industry, regionalisation and was the general manager of an NCB subsidiary company.',
'chia yuen kwan':'Yuen Kwan teaches courses in the areas of object-oriented technology and application development methodology. Prior to joining ISS, he was involved in application development projects in the government and transportation industries. He also led various large scale developments in business critical and legacy systems, in particular, the conversion of such systems to adopt the object oriented technology.',
'chin wun yunn':'Wun Yunn has about 8 years of industry experience spanning across various industries, working in Singapore, China and UK. A few of her notable projects included developing touch screen kiosks for Singapore Airlines, HMV, Nike, Jusco, as well as designing websites for Carrier, Brother and digital TV for Starhub. Having completed her Master degree under a UK government scholarship, she honed her design skills in a multi-awards design agency, ATTIK, which later became part of Dentsu, the fifth largest advertising agency network in the world.',
'daniel boey':'Daniel Boey is the Chief, Project Management Practice at the Institute of System Science, National University of Singapore. He manages a teaching and consultancy practice in project management, specializing in project management competency development and training. He and his team provide consultancy and training based on the PMBOK® (A Guide to Project Management Body of Knowledge, Project Management Institute), CITPM BOK (Certification in IT Project Management) and COMIT BOK (Certificate in Outsourcing Management). Other offerings under the practice include Project Leadership for Project Managers, P3O – Portfolio, Program Project Office Certification, Scrum Master Certification and PRINCE2 Certification and Project Management for Information Systems.',
'debashis tarafdar':'With over 30 years in consulting, research, advisory and operations, Debashis helps private and public sector leaders create world class, integrated and sustainable processes that deliver positive outcome through streamlined business and digitalization, by empowering them with the knowledge of industry best practices and global standards that improve stakeholder value through service innovation.',
'eric tham':'Eric has about 15 years of analytics and data science experience in the financial services, start-ups and web analytics. Prior joining ISS, he was an Enterprise Data Scientist with Thomson Reuters and was also director of quantitative data science in a China fintech start-up with 4 million users. He has also experience in web analytics as a partner in a Malaysian start-up. He has diverse financial experiences in risk management, quantitative analytics and energy economics as a vice-president with Credit Suisse, Standard Chartered bank, BP Oil and London Metal Exchange.',
'esther tan':'Esther specialises in designing and developing internet / mobile solutions to support organisations needs and business activities. Her current research areas include context aware, organizing and chunking information for mobile platform, mobile user interface design which includes visualization and presenting of information on small screen display. She also supervises mobile application projects with the latest wireless technology such as MMS, GPS and LBS. Her interests include tracking the internet and wireless technology trends and studying how these technologies can improve business processes. Prior to joining ISS, she was with the multimedia application centre at Singapore Polytechnic. Her experience included designing and developing multimedia applications and online learning packages. She was previously with Wearnes R&D centre as a firmware engineer, designing and developing BIOS for in-house designed computers.',
'fan zhen zhen':'Zhenzhen has been with Institute of Systems Science, NUS, since 2006. She currently lectures in the Master of Technology programme in the areas of case-based reasoning, text mining, KBS development, hybrid KBS, and formal specification. Prior to joining ISS, she was a senior research engineer at the Institute for Infocomm Research working in the areas of machine translation and natural language processing. Her current research interests lie in text mining and computational linguistics.',
'felicitas seah':'Felicitas is a member of the Project Management Practice at the Institute of System Science, NUS where she teaches and consults in project management practices and soft skills for post graduate students and industry professionals, working with corporate clients to deliver customized training for staff development.',
'goh boon nam':'Boon Nam has over 20 years of management experience in IT, holding management portfolios in IT governance, planning, architecture, quality and process improvement, application development, operations, human resource development, financial management and outsourcing. He has also developed and implemented various IT management processes, and successfully led IT organisations in achieving CMM / CMMI Level 3. He was also engaged in national IT efforts including marketing CITPM to regional computer societies as the then Secretary of the Special Regional Interest Group on Certification in the South East Asia Regional Computer Confederation as well as being the Honorary Secretary in initiating the set up of the National Infocomm Competency Centre (both organizations being predecessors to current regional and national IT competency organizations). At ISS, he oversees the initiation and incubation of new venture areas. In addition, he also teaches and consults on enterprise architecture, business analysis and IT process improvement (eg. IT service management and CMMI).',
'gu zhan':'GU Zhan (Sam) lectures Master of Technology programme in the areas of data science, machine intelligence, soft computing, and applied deep learning. Prior to joining ISS, he was in New Zealand running Kudos Data start-up, which focussed on training programs to democratize artificial intelligence and machine learning.  Before that, he was a data scientist in Yokogawa Engineering, leading industrial innovation initiatives.  Sam had also spent many years in financial sector wearing versatile hats: project manager, consultant, and business analyst in Barclays bank, system manager and senior software engineer at Citibank, leading to experience in actualizing information technology values in complex business environment.',
'heng boon kui':'Boon Kui is passionate with processes and methods in development of software systems. His current teaching interests in ISS include Solution/Software Architecture, Platform Engineering, Platform & Mobile Security, Analysis and Design, Design Patterns and Software Product Line. Prior to joining ISS, Boon Kui was in the telecommunication industry, playing various roles in software development and integration. He had experienced full lifecycles of various software development projects on telecommunication switching systems and their peripheral systems for narrowband, mobile and IP networks.',
'hoe siu loon':'Hoe Siu Loon is Principal Lecturer and Consultant at the Institute of Systems Science, National University of Singapore (NUS). He has more than 20 years of industry experience in assisting C-suite executives from both the private and public sectors. Siu Loon has held various managerial and consulting roles in strategic planning, corporate affairs, talent management and business process reengineering in multinational and local companies. He has led large-scale organisational change management projects across the region in China, Hong Kong, Malaysia and South Korea, and conducted digital government training for senior public sector officers from a number of countries.',
'kenneth phang':'Kenneth is a Senior Lecturer & Consultant in Software Systems Practice',
'khoong chan meng':'Mr Khoong Chan Meng brings 30 years of international experience in the information and communication technology industry. Chan Meng is driving NUS-ISS to develop and inspire the next generation of digital talent through education, applied research and consulting services. He has transformed NUS-ISS with a vision and strategy focused on delivering impact to the industry and aligned to the national agendas of SkillsFuture, the Smart Nation and the Future Economy. ',
'koh wai kin':'Wai Kin had spent 6 years as a Senior R&D Engineer specializing in electronic circuit design, development of firmware, PC Sync software and Android application development. He is currently pursuing Master of Technology in Software Engineering at NUS. He has keen interest in healthcare application and is working on the m-Health Rehabilitation System for Stroke Patient Recovery under the grant from SG Enable.',
'lee boon kee':'Boon Kee is a consultant and lecturer at the Institute of Systems Science, National University of Singapore, with over twenty-four years of professional experience in project and product management. His focus is on consulting and teaching for professional development and post-graduate programmes at ISS, and helping customers drive success through project and product management best practices. Prior to joining ISS, he has worked as a consultant and project manager in Accenture, HP, EDS, Sun Microsystems, and NEC. His work experience spans the financial and telecommunications industries, as well as the education and government sectors. He is a certified PMI Project Management Professional (PMP) and a Master Blackblot Product Management Professional (Master BPMP).',
'lee chuk munn':'Chuk is with the Advanced Technology Applications Practice for National University of Singapore, Institute of Systems Science (NUS-ISS). His current responsibilities includes developing courseware, and teaching graduate and public courses in enterprise software engineering, software architecture, web technologies and enterprise Java.',
'leong mun kew':'Mun Kew is appointed as Director, Graduate Programmes of ISS. Prior to joining ISS, Mun Kew held multiple positions with the National Library Board, Singapore, as CTO, Deputy CIO & Director CIO Office, and Director, Digital & Knowledge Infrastructure Division. As Deputy CIO, he was responsible for governance and architecture and started ongoing efforts in master data management, enterprise architecture and corporate governance of IT. In particular, he designed a federated approach to EA that allows a gradual easing of operations oriented organizations into a business driven architecture, and started the Government EA Forum to promote practitioner sharing of EA pains and successes. ',
'lim wee khee':'Ms Lim Wee Khee leads the Digital Innovation and Design practice at the Institute of System Science, National University of Singapore (NUS-ISS).   The Digital Innovation & Design team focuses on developing and delivering curriculum and consultancy projects related to the areas of user experience, service design and digital marketing.',
'lisa ong':'Lisa is with the Software Engineering and Design Practice, StackUp program for National University of Singapore, Institute of Systems Science (NUS-ISS).',
'matthew chua':'Dr Matthew Chua is currently a lecturer and principal investigator at the NUS Institute of System Science where he specializes in Medical & Cybernetics Systems. He is overseeing the research programme in Smart Healthcare, Artificial Intelligence and Advanced Robotics. He has won prestigious research grants, amounting to more than S$1 million, from National Medical Research Council (NMRC), Ministry of Health, SG Enable and internationally for his work in intelligent systems. His wide array of expertise makes him a highly sought-after collaborator from various industries. He is currently the Associate Editor for IEEE Access journals and the appointed Residential Fellow for Kent Ridge Hall, NUS. He is also a ScrumMaster with Scrum Alliance and a certified Project Management Professional (PMP) with PMI.',
'michael tan':'Michael, a Certified Business Analysis Professional (CBAP®), has over 10 years of IT experience in project management, business analysis and software application development. Prior to joining ISS, he was a Project Manager with a leading System Integrator where he managed end to end turnkey application development for clients in the financial sector. Prior to that, he has also manage projects implementations in healthcare, logistics and government organizations. During the project, Michael has employed different software development methodology and managed both in-house teams, vendors, and offshore development team. Technology wise, Michael has both experience in application development and infrastructure setup. He is also involved in the formation of International Institute of Business Analysis Singapore Chapter.',
'ng kok leong':'Kok Leong is a Senior Lecturer & Consultant in Digital Strategy & Leadership Practice.',
'nicholas tan':'Nicholas Tan is Principal Lecturer and Consultant at the Institute of Systems Science, National University of Singapore. He has been designing and delivering enterprise technology solutions and services since 2000 in regional and global organisations in the hospitality, logistics, consumer packaged goods and pharmaceutical sectors. Prior to joining the private sector, he began his career in a Singapore Government IT research laboratory, working in various ministries and agencies.',
'nirmal raja palaparthi':'Nirmal is an Analytics professional with 18 years of experience in building practices from ground up in Asia. He has Co-founded and successfully exited from two Analytics companies. The first was Fractal Analytics, India’s leading third party analytics provider and the second: Mobius Innovations, a context awareness platform company, which was acquired for building significant IP. He has consulted for clients in 15 countries, across Banking, Retail, Telecom, Consumer Product and Enterprise Software verticals. He has also built digital ecosystems for multiple clients. ',
'prakash chandra sukhwal':'Prakash is an Associate Lecturer in Institute of Systems Science, National University of Singapore (NUS-ISS). He taught for various analytics modules at School of Information Systems, SMU Singapore for nearly three years prior to joining NUS-ISS.',
'prasanna veerapandi':'Prasanna is a Associate Lecturer & Consultant in Software Systems Practice',
'rajnish tuli':'Rajnish is a Principal Lecturer & Consultant, Data Science Practice',
'richard tan':'Richard lectures in project management competency development and training courses; the Certified Outsourcing Manager (Associate) for IT Programme; the Certified Enterprise Architecture Practitioner Programme; and the Master of Technology Programme that include IT Service Management and Data Warehouse for Business Analytics.',
'rita chakravarti':'Rita as a seasoned analytics professional has 25+ years of experience in Financial Services, Insurance and Market Research specializing in Scoring (operational & regulatory), Risk Management, Marketing Analytics, Analytics Strategy Development, Analytics Infrastructure, Analytics team management and training. Experience spans across Asia Pacific, Middle East, US & Canada.',
'sean hoang':'Seah is a Research Engineer in Smart Health Leadership Centre',
'sharon lau':'Sharon has 20 years of career in Information Technology (IT), with vast experience in Retail and Telecommunication industries. She is an experienced technology leader who had worked in multinational companies for Asia Pacific region and excel at strategic planning, business engagement and portfolio management. Sharon’s passion is to educate and enable business leaders in all aspects of technology strategy, especially in the focus of implementing best practice methodologies and continuous improvement programs for corporate organizations. She is an enthusiastic lifelong learner who believe never stop learning because life never stops teaching.',
'suriya priya asaithambi':'Suria has twenty years of teaching and consulting experience in areas such as software engineering, application architecture, crafting cloud services, agile development and big data engineering.  Her research interest spans around cloud computing, software engineering, test automation and big data engineering.  Prior to joining ISS, she worked as technical consultant in various capacities for software firms and MNCs where her roles and contribution involved application architecture, leadership, and software delivery and stakeholder management. Prior to migrating to Singapore, she was a senior lecturer in School of Computing, SASTRA India.',
'swarnalatha ashok':'Swarna teaches object oriented technology, web services and Java technology at ISS. Having been with leading manufacturing and consulting companies like D.C.M Data Products and Tata Consultancy Services in India, she has extensive experience in networking and systems software development. At Information Communication Institute of Singapore, she was responsible for managing and delivering courses on software engineering, UNIX and object oriented technology. Prior to this, she was in-charge of network management (cellular networks) software development projects at the Motorola Software Centre, Singapore. Swarna has most recently co-authored a book entitled Object Oriented Programming and Java.',
'tamsin emma maria greulich-smith':'Tamsin, a Senior Fellow at the Ministry of Health’s Office for Healthcare Transformation, and expert design strategist on DesignSingapore Council’s ‘Innovation by Design’ panel, has more than 20 years of international experience in delivering change and transformation programmes, integrating user-centric design, risk communications, change leadership, and social innovation practices.',
'tan cher wah':'Cher Wah has over 20 years of software development experience in the Education, Security and Applied R&D domains. Prior to joining ISS, he headed up a software team to develop mobile, desktop and web applications at Marshall Cavendish Education. He has also worked at Startups, SMEs, MNCs and Government entities.',
'tan chi siong':'Chi Siong is currently the Chief of MTech Digital Leadership Programme and the Deputy Chief of Digital Strategy & Leadership Practice at the Institute of System Science (ISS), National University of Singapore.  Chi Siong joined ISS from GIC Private Limited, where he was the Senior Vice President of the Technology Group.  During his tenure with GIC, he had served in various key appointments and had spearheaded many significant and notable projects, including developing the first GIC IT Master Plan and initiating the second Digital Master Plan to transform GIC into a technology-driven investment company.  A member of the Technology Management committee, he also played an instrumental role in championing various IT business, innovation and quality improvement initiatives.  One of his key achievements included the successful implementation of the Agile Operating Model to enable project teams to adopt agile methods for fast turnaround in application development and delivery. ',
'tan eng tsze':'Tan Eng Tsze is a practising enterprise architect consultant and lecturer at ISS. He conducts Enterprise Architecture certification short courses and for a Masters degree programme at NUS. He also provides enterprise architecture consulting for public and private sector companies. He has provided EA consulting for defence, healthcare and the Singapore Governments Enterprise Architecture Methodology and Toolkit project. He was also involved in the development of the NICF EA and SOA competency units. Previously, Eng Tsze also consulted for a large government agency using IBMs EA Methodology. Having worked in IBM, BearingPoint and NCS, he has accumulated experiences in Enterprise Architecture, IT architecting, solution architecting and systems integration. He started his IT career many years ago as a software engineer with the Defence Science Organisation, developing stringent mission planning systems for the Singapore Navy and subsequently moved on to research institute KRDL, developing knowledge based systems.',
'tan jen hong':'Jen Hong develops algorithms. He specializes in deep learning, image processing and medical image diagnosis. He designs illustrations, web page and posters. He plays piano.',
'tan lay ngan':'Lay Ngan delivers courses and manages consulting projects on IT Governance, Strategic IT Planning, Enterprise IT Architecture and Data Governance. She also conducts Postgraduate Course and Essential Leadership Skills for Project Managers. Her recent completed consultancy projects included a large Insurance Company located in Singapore. She is appointed by Singapore Information Technology Standards Committee, as Chairman of IT Governance Technical Committee. She works with International Joint Technical Standards Committee with the aims in establishing Singapore as a practice-leader in effective IT Governance directed to enhancing business value of IT. She is also actively involved in setting the Technical Guides on Cloud Computing. Prior to joining ISS , she was with various ministries and statutory boards holding high position in IT Management.',
'tan liong choon':'Liong Choon is currently the product manager for the course Product Thinking for Organisations and a Senior Lecturer cum Consultant in ISS.',
'tan peng wei':'Peng Wei is currently the Chief of Information & Technology (IT) Strategy & Management Practice at the Institute of System Science (ISS), National University of Singapore. He has more than 30 years of working experience in Business and Technology Services. He begin his teaching career with ISS as an adjunct lecturer for ISS eGovernment leadership programme delivering courses in Cambodia, China, Singapore and Sri-Lanka in 2014 and joined ISS officially in 2016. Prior to joining ISS, He was the co-founder of a US-based Start-Up working on an integrated online-offline marketing promotion platform. In his work career, he has held various leadership positions including being the Asia Pacific President for a Global Automotive Dealership Solution Company (CDK), South East Asia Managing Director for Electronic Data Systems and HP China’s General Manager for Application Services. He has worked across many industry sectors including Automotive, Electronic Manufacturing, Logistics and Finance. Peng Wei has a good understanding of cultural diversity having worked and lived in China (8 years), Taiwan and the US (3 years).',
'tan tzann chang':'Tzann currently teaches in areas of IT management and outsourcing. His advisory engagements span IT governance and management, strategic sourcing, service delivery management, business startup and e-government development. He has close to 30 years of experience in a variety of management roles with various MNCs, local and government organisations.',
'tian jing':'Tian Jing currently lectures in the Analytics and Intelligent Systems Practice in the areas of artificial intelligence, data analytics, and machine learning. He received his Ph.D. degree from School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore.',
'wang aobo':'Aobo Wang is currently a lecturer and consultant with National University of Singapore, Institute of Systems Science (NUS-ISS) with responsibility in teaching, consulting and research. He lectures in the areas of text mining, natural language processing, and machine learning. He received his Ph.D. degree from School of Computing, National University of Singapore in the year of 2015. His research interests lie in text mining and natural language processing especially for social media. Prior to joining ISS, he was served as an IT Lead and PM in the bank of BNP PARIBAS, Global IT-HUB in Singapore.',
'yu chen kuang':'Yu Chen Kuang was from Deloitte Consulting and Arthur Andersen, specialising in strategic business planning, business process reengineering and supply chain management. He had spent 3 years in China with a Shanghai-based management consulting firm. Prior to this, Chen Kuang was from the Infocomm Development Authority of Singapore, where he was involved in many national IT programmes such as the Singapore IT 2000 Masterplan, Singapore ONE and the Local Industry Upgrading Programme (IT LIUP). At NUS-ISS, he is involved with teaching and consultancy on BPR, BPM and ESB (Enterprise Social Business).',
'yum hui yuen':'In addition to overseeing the overall operations in ISS, Hui Yuen also manages the Professional Studies Programme. She designs and plans the implementation of new programmes based on industry requirements and alignment to national and international standards. Her area of specialization is Strategic IT Management including strategic IT planning, business process reengineering and knowledge management. She had conducted courses and executive seminars and was lead consultant in many consulting projects. She was a member of the National Infocomm Competency Framework Adoption Sub-committee. Prior to joining ISS, Hui Yuen had worked for both the port and banking industries. Her experience in PSA included applications development, maintenance and technical support in information systems. Subsequently, she worked at Citibank NA as the systems development manager in charge of all the systems for the entire retail bank.',
'yunghans irawan':'Yunghans is currently an associate with National University of Singapore, Institute of Systems Science (NUS-ISS) with responsibility in teaching, consulting and research. He teaches graduate and public courses in enterprise software engineering in Java and .NET, software architecture, cloud computing, agile software development and service innovation.',
'zhu fang ming':'Dr. Zhu Fangming is with the Institute of Systems Science of the National University of Singapore (NUS-ISS).  He currently lectures in the Master of Technology programme in the areas of evolutionary computation, neural networks and data mining. Prior to joining ISS, he was a postdoctoral fellow in the Department of Electrical and Computer Engineering at NUS. He also worked as a research and development engineer in an IT company before pursuing his PhD studies at NUS. His research interests include evolutionary computation, neural networks, data mining, machine learning, and pattern recognition. Fangming was a recipient of the prestigious Singapore Millennium Foundation (SMF) Postdoctoral Fellowship in 2003.  He has also published many papers in leading journals and conferences.',

}

TeachingStaffLinks = {

'angela huang':'https://www.iss.nus.edu.sg/about-us/staff/detail/170/Angela%20HUANG',
'ashok kumar seetharaman':'https://www.iss.nus.edu.sg/about-us/staff/detail/521/Ashok%20Kumar%20SEETHARAMAN',
'barry adrian shepherd':'https://www.iss.nus.edu.sg/about-us/staff/detail/24/Barry%20Adrian%20SHEPHERD',
'brandon ng':'https://www.iss.nus.edu.sg/about-us/staff/detail/653/Brandon%20NG',
'brian ng':'https://www.iss.nus.edu.sg/about-us/staff/detail/330/Brian%20NG',
'chandrasekaran paramasivam':'https://www.iss.nus.edu.sg/about-us/staff/detail/492/Chandrasekaran%20PARAMASIVAM',
'charles pang':'https://www.iss.nus.edu.sg/about-us/staff/detail/173/Charles%20PANG',
'chia yuen kwan':'https://www.iss.nus.edu.sg/about-us/staff/detail/169/CHIA%20Yuen%20Kwan',
'chin wun yunn':'https://www.iss.nus.edu.sg/about-us/staff/detail/338/CHIN%20Wun%20Yunn',
'daniel boey':'https://www.iss.nus.edu.sg/about-us/staff/detail/225/Daniel%20BOEY',
'debashis tarafdar':'https://www.iss.nus.edu.sg/about-us/staff/detail/339/Debashis%20TARAFDAR',
'eric tham':'https://www.iss.nus.edu.sg/about-us/staff/detail/ce1c1b29-c27b-41d7-a8bd-9b4645806bef/Eric%20THAM',
'esther tan':'https://www.iss.nus.edu.sg/about-us/staff/detail/53/Esther%20TAN',
'fan zhen zhen':'https://www.iss.nus.edu.sg/about-us/staff/detail/278/FAN%20Zhen%20Zhen',
'felicitas seah':'https://www.iss.nus.edu.sg/about-us/staff/detail/406/Felicitas%20SEAH',
'goh boon nam':'https://www.iss.nus.edu.sg/about-us/staff/detail/377/GOH%20Boon%20Nam',
'gu zhan':'https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan',
'heng boon kui':'https://www.iss.nus.edu.sg/about-us/staff/detail/261/HENG%20Boon%20Kui',
'hoe siu loon':'https://www.iss.nus.edu.sg/about-us/staff/detail/623/HOE%20Siu%20Loon',
'kenneth phang':'https://www.iss.nus.edu.sg/about-us/staff/detail/648/Kenneth%20PHANG',
'khoong chan meng':'https://www.iss.nus.edu.sg/about-us/staff/detail/561/KHOONG%20Chan%20Meng',
'koh wai kin':'https://www.iss.nus.edu.sg/about-us/staff/detail/209/KOH%20Wai%20Kin',
'lee boon kee':'https://www.iss.nus.edu.sg/about-us/staff/detail/512/LEE%20Boon%20Kee',
'lee chuk munn':'https://www.iss.nus.edu.sg/about-us/staff/detail/532/LEE%20Chuk%20Munn',
'leong mun kew':'https://www.iss.nus.edu.sg/about-us/staff/detail/281/LEONG%20Mun%20Kew',
'lim wee khee':'https://www.iss.nus.edu.sg/about-us/staff/detail/668/LIM%20Wee%20Khee',
'lisa ong':'https://www.iss.nus.edu.sg/about-us/staff/detail/203/Lisa%20ONG',
'matthew chua':'https://www.iss.nus.edu.sg/about-us/staff/detail/654/Matthew%20CHUA',
'michael tan':'https://www.iss.nus.edu.sg/about-us/staff/detail/654/Matthew%20CHUA',
'ng kok leong':'https://www.iss.nus.edu.sg/about-us/staff/detail/122/NG%20Kok%20Leong',
'nicholas tan':'https://www.iss.nus.edu.sg/about-us/staff/detail/583/Nicholas%20TAN',
'nirmal raja palaparthi':'https://www.iss.nus.edu.sg/about-us/staff/detail/732/Nirmal%20Raja%20PALAPARTHI',
'prakash chandra sukhwal':'https://www.iss.nus.edu.sg/about-us/staff/detail/98592a25-d6d1-4260-9130-d666923fced3/Prakash%20Chandra%20SUKHWAL',
'prasanna veerapandi':'https://www.iss.nus.edu.sg/about-us/staff/detail/687/Prasanna%20VEERAPANDI',
'rajnish tuli':'https://www.iss.nus.edu.sg/about-us/staff/detail/05f26cbd-ccac-4028-ac2f-6e85f925cfe6/Rajnish%20TULI',
'richard tan':'https://www.iss.nus.edu.sg/about-us/staff/detail/369/Richard%20TAN',
'rita chakravarti':'https://www.iss.nus.edu.sg/about-us/staff/detail/672/Rita%20CHAKRAVARTI',
'sean hoang':'https://www.iss.nus.edu.sg/about-us/staff/detail/208/Sean%20HOANG',
'sharon lau':'https://www.iss.nus.edu.sg/about-us/staff/detail/312/Sharon%20LAU',
'suriya priya asaithambi':'https://www.iss.nus.edu.sg/about-us/staff/detail/272/Suriya%20Priya%20ASAITHAMBI',
'swarnalatha ashok':'https://www.iss.nus.edu.sg/about-us/staff/detail/66/Swarnalatha%20ASHOK',
'tamsin emma maria greulich-smith':'https://www.iss.nus.edu.sg/about-us/staff/detail/584/Tamsin%20Emma%20Maria%20GREULICH-SMITH',
'tan cher wah':'https://www.iss.nus.edu.sg/about-us/staff/detail/326/TAN%20Cher%20Wah',
'tan chi siong':'https://www.iss.nus.edu.sg/about-us/staff/detail/309/TAN%20Chi%20Siong',
'tan eng tsze':'https://www.iss.nus.edu.sg/about-us/staff/detail/283/TAN%20Eng%20Tsze',
'tan jen hong':'https://www.iss.nus.edu.sg/about-us/staff/detail/212/TAN%20Jen%20Hong',
'tan lay ngan':'https://www.iss.nus.edu.sg/about-us/staff/detail/79/TAN%20Lay%20Ngan',
'tan liong choon':'https://www.iss.nus.edu.sg/about-us/staff/detail/333/TAN%20Liong%20Choon',
'tan peng wei':'https://www.iss.nus.edu.sg/about-us/staff/detail/632/TAN%20Peng%20Wei',
'tan tzann chang':'https://www.iss.nus.edu.sg/about-us/staff/detail/254/TAN%20Tzann%20Chang',
'tian jing':'https://www.iss.nus.edu.sg/about-us/staff/detail/179/TIAN%20Jing',
'wang aobo':'https://www.iss.nus.edu.sg/about-us/staff/detail/328/WANG%20Aobo',
'yu chen kuang':'https://www.iss.nus.edu.sg/about-us/staff/detail/461/YU%20Chen%20Kuang',
'yum hui yuen':'https://www.iss.nus.edu.sg/about-us/staff/detail/5/YUM%20Hui%20Yuen',
'yunghans irawan':'https://www.iss.nus.edu.sg/about-us/staff/detail/423/Yunghans%20IRAWAN',
'zhu fang ming':'https://www.iss.nus.edu.sg/about-us/staff/detail/260/ZHU%20Fang%20Ming',

}

PDUcourses = {	
	'NICF- Secure Software Development Lifecycle for Agile (SF)':'10hrs',
'NICF- Managing Business Analytics Projects (SF)':'19.25hrs',
' NICF- ITIL® Continual Service Improvement Certificate (SF)':'21hrs',
'Certified Scrum Product Owner':'9hrs',
'NICF - Lean IT Foundation Certification (SF)':'14.5hrs',
'NICF- Business Analysis for Agile Practitioners (SF)':'10hrs',
'NICF- Certified ScrumMaster (SF)':'19.5hrs',
'NICF- DevOps Foundation with BizOps (SF)':'17.5hrs',
' NICF- ITIL® Foundation Certificate in IT Service Management (SF)':'13.5hrs',
' NICF- ITIL® Operational Support and Analysis Certificate (SF)':'17.5hrs',
' NICF- ITIL® Release, Control and Validation Certificate (SF)':'25.5hrs',
' NICF- ITIL® Service Offerings and Agreements Certificate (SF)':'27.5hrs',
' NICF- PMI Agile Certified Practitioner (PMI-ACP)® Preparatory Course (SF)':'21hrs',
'Certified Scrum Product Owner':'9hrs',
'NICF- Certified ScrumMaster (SF)':'19.5hrs',
'NICF- Communicating and Managing Change (SF)':'19.5hrs',
'NICF- Digital Product Strategy (SF)':'15hrs',
'NICF- Managing Business Analytics Projects (SF)':'19.25hrs',
' NICF- PMI Agile Certified Practitioner (PMI-ACP)® Preparatory Course (SF)':'21hrs',
' NICF- PMP® For Project Managers (SF)':'35hrs',
' NICF- Portfolio, Programme and Project Offices (P3O®)- Foundation & Practitioner':'29.5hrs',
' NICF- PRINCE2® (PRojects IN Controlled Environments) - Foundation and Practitioner Certificate  (SF)':'25hrs',
'NICF- Product Thinking for Organisations (SF)':'8.5hrs',
'NICF- Strategic Product Manager ™ (SF)':'12hrs',
'NICF– Strategic Product Market Fit (SF)':'17hrs',
' Certified Business Analysis Professional (CBAP®) Preparatory Course':'31hrs',
'Certified Scrum Product Owner':'9hrs',
'NICF- Business Analysis for Agile Practitioners (SF)':'10hrs',
'NICF- Business Process Reengineering (SF)':'17hrs',
'NICF- Certified Enterprise Architecture Practitioner Course (SF)':'25hrs',
' NICF- COBIT® 5 Foundation (SF)':'18hrs',
'NICF- Communicating and Managing Change (SF)':'19.5hrs',
'NICF- Secure Software Development Lifecycle for Agile (SF)':'10hrs',
'NICF- Strategic Business Analysis (SF)':'13hrs',
'NICF- Architecting Software Solutions (SF)':'20hrs',
'NICF- Digital Product Strategy (SF)':'15hrs',
'NICF- Object Oriented Analysis & Design (SF)':'19hrs',
'NICF- Secure Software Development Lifecycle for Agile (SF)':'10hrs',
'NICF- Strategic Product Manager ™ (SF)':'12hrs'
}	

# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req["queryResult"]["intent"]["displayName"]
    
    
    if intent_name == "GetCourseFees" : ##     
        respose_text = getCourseFeesIntent(req) ## Call your getWeatherIntentHandler with req object as input. 
        print(req) # to print the entire output for the request
    elif intent_name == "GetCourseDetails" : ##    
        respose_text = getCourseDetailsIntent(req) ## Call your getWeatherIntentHandler with req object as input. 
        print(req) # to print the entire output for the request
    elif intent_name == "GetTeachingStaff" : ##    
        respose_text = getTeachingStaffIntent(req) ## Call your getWeatherIntentHandler with req object as input. 
        print(req) # to print the entire output for the request  
    elif intent_name == "getcoursePDUintent" : ##     
        respose_text = getcoursePDUintent(req) ## Call your getWeatherIntentHandler with req object as input. 
        print(req) # to print the entire output for the request
    elif intent_name == "getCourseTopicintent" : ##     
        respose_text = getCourseTopicintent(req) ## Call your getWeatherIntentHandler with req object as input. 
        print(req) # to print the entire output for the request
    else:
        respose_text = "Im sorry, could you say that again?"
    # Branching ends here

    # Finally sending this response to Dialogflow.
    return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************


# *****************************
# Intent Handlers funcs : START
# *****************************

def getCourseFeesIntent(req):

    course = req.get("queryResult").get("parameters").get("Course")
    course = course.lower()

    if course in CourseLinks:
        
        CourseLinkOutput = CourseLinks[course]
        CourseNameOutput = CourseNames[course]
        
        return f"A typical ISS course cost between $200 - $4000. Many of the courses are heavily subsidised by the Singapore Government if you are a Citizen or Permanent Resident of Singapore. For a detailed breakdown of the course {CourseNameOutput}, please refer to the details in the following link. {CourseLinkOutput}"
    
    else:
        return f"Please enter a course name to enquire. Thank you."


def getCourseDetailsIntent(req):

    course = req.get("queryResult").get("parameters").get("Course")
    course = course.lower()

    if course in CourseLinks:
        
        CourseLinkOutput = CourseLinks[course]
        CourseNameOutput = CourseNames[course]
        
        return f"For a detailed description of {CourseNameOutput}, please refer to the following link. {CourseLinkOutput}"
    
    else:
        return f"Please enter a course name to enquire. Thank you."


def getTeachingStaffIntent(req):

    teachingstaff2 = req.get("queryResult").get("parameters").get("TeachingStaff")
    teachingstaff = teachingstaff2.lower()

    if teachingstaff in TeachingStaffLinks:
        
        TeachingStaffLinkOutput = TeachingStaffLinks[teachingstaff]
        TeachingStaffDescOutput = TeachingStaffDesc[teachingstaff]
        
        return f"{TeachingStaffDescOutput}. If you would like to find out more about {teachingstaff2} please refer to the following link. {TeachingStaffLinkOutput}"
    
    else:
        return f"Please enter a staff name to enquire. Thank you."

def getcoursePDUintent(req):

    s="NICF- Secure Software Development Lifecycle for Agile (SF):10hrs,\
    NICF- Managing Business Analytics Projects (SF):19.25hrs,\
    NICF- ITIL® Continual Service Improvement Certificate (SF):21hrs,\
    Certified Scrum Product Owner:9hrs,\
    NICF - Lean IT Foundation Certification (SF):14.5hrs,\
    NICF- Business Analysis for Agile Practitioners (SF):10hrs,\
    NICF- Certified ScrumMaster (SF):19.5hrs,\
    NICF- DevOps Foundation with BizOps (SF):17.5hrs,\
     NICF- ITIL® Foundation Certificate in IT Service Management (SF):13.5hrs,\
     NICF- ITIL® Operational Support and Analysis Certificate (SF):17.5hrs,\
     NICF- ITIL® Release, Control and Validation Certificate (SF):25.5hrs,\
     NICF- ITIL® Service Offerings and Agreements Certificate (SF):27.5hrs,\
     NICF- PMI Agile Certified Practitioner (PMI-ACP)® Preparatory Course (SF):21hrs,\
    Certified Scrum Product Owner:9hrs,\
    NICF- Certified ScrumMaster (SF):19.5hrs,\
    NICF- Communicating and Managing Change (SF):19.5hrs,\
    NICF- Digital Product Strategy (SF):15hrs,\
    NICF- Managing Business Analytics Projects (SF):19.25hrs,\
     NICF- PMI Agile Certified Practitioner (PMI-ACP)® Preparatory Course (SF):21hrs,\
     NICF- PMP® For Project Managers (SF):35hrs,\
     NICF- Portfolio, Programme and Project Offices (P3O®)- Foundation & Practitioner:29.5hrs,\
     NICF- PRINCE2® (PRojects IN Controlled Environments) - Foundation and Practitioner Certificate  (SF):25hrs,\
    NICF- Product Thinking for Organisations (SF):8.5hrs,\
    NICF- Strategic Product Manager ™ (SF):12hrs,\
    NICF– Strategic Product Market Fit (SF):17hrs,\
     Certified Business Analysis Professional (CBAP®) Preparatory Course:31hrs,\
    Certified Scrum Product Owner:9hrs,\
    NICF- Business Analysis for Agile Practitioners (SF):10hrs,\
    NICF- Business Process Reengineering (SF):17hrs,\
    NICF- Certified Enterprise Architecture Practitioner Course (SF):25hrs,\
     NICF- COBIT® 5 Foundation (SF):18hrs,\
    NICF- Communicating and Managing Change (SF):19.5hrs,\
    NICF- Secure Software Development Lifecycle for Agile (SF):10hrs,\
    NICF- Strategic Business Analysis (SF):13hrs,\
    NICF- Architecting Software Solutions (SF):20hrs,\
    NICF- Digital Product Strategy (SF):15hrs,\
    NICF- Object Oriented Analysis & Design (SF):19hrs,\
    NICF- Secure Software Development Lifecycle for Agile (SF):10hrs,\
    NICF- Strategic Product Manager ™ (SF):12hrs"

    return s#    return str(PDUcourses)

def getCourseTopicintent(req):

    subject = req.get("queryResult").get("queryText")#get("parameters").get("Topic")
    print(subject)
    subject = subject.lower()

    s="We cant find the subject"
    if "artificial intelligence" in subject:
        s="NICF- Intelligent Sensing and Sense Making (SF),\
        NICF- Machine Reasoning (SF),\
        NICF- New Media and Sentiment Mining (SF),\
        NICF- Pattern Recognition and Machine Learning Systems (SF),\
        NICF- Problem Solving using Pattern Recognition (SF),\
        NICF- Reasoning Systems (SF),\
        NICF- Robotic Systems (SF),\
        NICF- Spatial Reasoning from Sensor Data (SF),\
        NICF- Text Analytics (SF),\
        NICF- Text Processing using Machine Learning (SF),\
        NICF- Vision Systems (SF)"


    elif "cyber security" in subject:
        s="Certified Cloud Security Professional (CCSP Exam Only) - Exams supported by CITREP+,\
        Certified Information Systems Security Professional (CISSP Exam Only) - Exams supported by  CITREP+,\
        Certified Secure Software Lifecycle Professional (CSSLP Exam Only) - Exams supported by CITREP+,\
        NICF- (ISC)2 CCSP CBK Training Seminar (SF),\
        NICF- (ISC)² CISSP CBK Training Seminar (SF),\
        NICF- (ISC)² CSSLP CBK Training Seminar (SF),\
        NICF- AISP Qualified Information Security Professional Course (SF),\
        NICF- Cyber Security for ICT Professionals (SF),\
        NICF- Cybersecurity Risk Awareness (SF),\
        NICF- Design Secure Mobile Architecture (SF),\
        NICF- Managing Cybersecurity Risk (SF),\
        NICF- Secure Software Development Lifecycle for Agile (SF),\
        NICF- Securing IoT (SF)"
    elif "data science" in subject:
        s="NICF- Advanced Customer Analytics (SF),\
        NICF- Big Data Engineering for Analytics (SF),\
        NICF- Campaign Analytics (SF),\
        NICF- Customer Analytics (SF),\
        NICF- Data Analytics Process and Best Practice (SF),\
        NICF- Data Driven Decision Making (SF),\
        NICF- Data Governance & Protection (SF),\
        NICF- Data Storytelling (SF),\
        NICF- Feature Engineering and Analytics using IOT Data (SF),\
        NICF- Health Analytics (SF),\
        NICF- Managing Business Analytics Projects (SF),\
        NICF- New Media and Sentiment Mining (SF),\
        NICF- Predictive Analytics - Insights of Trends and Irregularities (SF),\
        NICF- Recommender Systems (SF),\
        NICF- Social Media Analytics (SF),\
        NICF- Statistics Bootcamp (SF),\
        NICF- Statistics for Business (SF),\
        NICF- Text Analytics (SF),\
        NICF- Text Processing using Machine Learning (SF),\
        NICF- Web Analytics and SEO (SF),\
        NICF-Service Analytics (SF)"

    elif "digital agility" in subject:
        s=" NICF- ITIL® Continual Service Improvement Certificate (SF),\
        Certified Scrum Product Owner,\
        NICF - Lean IT Foundation Certification (SF),\
        NICF- Agile Testing (SF),\
        NICF- Business Agility Bootcamp (SF),\
        NICF- Business Analysis for Agile Practitioners (SF),\
        NICF- Certified LeSS Practitioner - Principles to Practices (SF),\
        NICF- Certified ScrumMaster (SF),\
        NICF- DevOps Foundation with BizOps (SF),\
        NICF- Essential Practices for Agile Teams (SF),\
         NICF- ITIL® Foundation Certificate in IT Service Management (SF),\
         NICF- ITIL® Operational Support and Analysis Certificate (SF),\
        ,\
         NICF- ITIL® Release, Control and Validation Certificate (SF),\
         NICF- ITIL® Service Offerings and Agreements Certificate (SF),\
         NICF- PMI Agile Certified Practitioner (PMI-ACP)® Preparatory Course (SF),\
        NICF- Systems Thinking & Root Cause Analysis (SF)"

    elif "digital innovation & design" in subject:
        s=" NICF- Digital & Social Engagement Strategy (SF),\
        NICF- Digital User Experience Design (SF),\
        NICF- Innovation Bootcamp (SF),\
        NICF- Mobile User Experience Design (SF),\
        NICF- Service Design (SF),\
        NICF- Social Media Analytics (SF),\
        NICF- Strategic Design & Innovation (SF),\
        NICF- Technopreneurship (SF),\
        NICF- Web Analytics and SEO (SF)"

    elif "digital products & platforms" in subject:
        s=" Certified Scrum Product Owner,\
        NICF- Certified ScrumMaster (SF),\
        NICF- Communicating and Managing Change (SF),\
        NICF- Digital Product Strategy (SF),\
        NICF- Managing Business Analytics Projects (SF),\
         NICF- PMI Agile Certified Practitioner (PMI-ACP)® Preparatory Course (SF),\
         NICF- PMP® For Project Managers (SF),\
         NICF- Portfolio, Programme and Project Offices (P3O®)- Foundation & Practitioner,\
         NICF- PRINCE2® (PRojects IN Controlled Environments) - Foundation and Practitioner Certificate  (SF),\
        NICF- Product Thinking for Organisations (SF),\
        NICF- Strategic Product Manager ™ (SF),\
        NICF– Strategic Product Market Fit (SF),\
         PMI Agile Certified Practitioner (PMI-ACP® Exam Only) - Exams supported by CITREP+,\
         Project Management Professional (PMP® Exam Only) - Exams supported by CITREP+"

    elif "digital strategy & leadership" in subject:
        s=" Certified Business Analysis Professional (CBAP®) Preparatory Course,\
        Certified Cloud Security Professional (CCSP Exam Only) - Exams supported by CITREP+,\
        Certified Information Systems Security Professional (CISSP Exam Only) - Exams supported by  CITREP+,\
        Certified Scrum Product Owner,\
        Certified Secure Software Lifecycle Professional (CSSLP Exam Only) - Exams supported by CITREP+,\
        e-Government Leadership,\
        NICF - Enterprise Architecture Practicum - AOP (SF),\
        NICF- (ISC)2 CCSP CBK Training Seminar (SF),\
        NICF- (ISC)² CISSP CBK Training Seminar (SF),\
        NICF- AISP Qualified Information Security Professional Course (SF),\
        NICF- Business Agility Bootcamp (SF),\
        NICF- Business Analysis for Agile Practitioners (SF),\
        NICF- Business Process Reengineering (SF),\
        NICF- Certified Enterprise Architecture Practitioner Course (SF),\
         NICF- COBIT® 5 Foundation (SF),\
        NICF- Communicating and Managing Change (SF),\
        NICF- Cyber Security for ICT Professionals (SF),\
        NICF- Cybersecurity Risk Awareness (SF),\
        NICF- Data Driven Decision Making (SF),\
        NICF- Data Governance & Protection (SF),\
        NICF- Design Secure Mobile Architecture (SF),\
        NICF- Digital Transformation Planning (SF),\
        NICF- Enterprise Architecture Masterclass (SF),\
        NICF- Enterprise Architecture Practicum (SF),\
        NICF- Enterprise Digital Governance (SF),\
        NICF- Innovation Bootcamp (SF),\
        NICF- Managing Cybersecurity Risk (SF),\
        NICF- Secure Software Development Lifecycle for Agile (SF),\
        NICF- Securing IoT (SF),\
        NICF- Strategic Business Analysis (SF),\
        NICF- Strategic Futures & Foresight (SF),\
        NICF-Specialist Diploma in Enterprise Architecture - Exams supported by CITREP+"

    elif "software systems" in subject:
        s=" NICF- (ISC)² CISSP CBK Training Seminar (SF),\
        NICF- Agile Testing (SF),\
        NICF- Architecting IOT Solutions (SF),\
        NICF- Architecting Software Solutions (SF),\
        NICF- Big Data Engineering for Analytics (SF),\
        NICF- Cloud Native Solution Design (SF),\
        NICF- Design Secure Mobile Architecture (SF),\
        NICF- Designing Cloud-enabled Mobile Applications (SF),\
        NICF- Designing Intelligent Edge Computing (SF),\
        NICF- Developing Smart Urban IoT Solutions (SF),\
        NICF- DevOps Engineering and Automation (SF),\
        NICF- Digital Product Strategy (SF),\
        NICF- Envisioning Smart Urban IoT Solutions (SF),\
        NICF- Essential Practices for Agile Teams (SF),\
        NICF- Humanizing Smart Systems (SF),\
        NICF- Introduction to Blockchain & DLT for Executives (SF),\
        NICF- Object Oriented Analysis & Design (SF),\
        NICF- Object Oriented Design Patterns (SF),\
        NICF- Platform Engineering (SF),\
        NICF- Secure Software Development Lifecycle for Agile (SF),\
        NICF- Securing IoT (SF),\
        NICF- Service Design (SF),\
        NICF- Strategic Product Manager ™ (SF),\
        NUS Graduate Diploma in Systems Analysis - Capstone & Internship,\
        NUS Graduate Diploma in Systems Analysis (SF),\
        NUS-ISS Certificate in Digital Solutions Development – Design (SF),\
        NUS-ISS Certificate in Digital Solutions Development – Foundations (SF),\
        NUS-ISS Certificate in Digital Solutions Development - Mobility Applications (SF),\
        NUS-ISS Certificate in Digital Solutions Development – Web Applications (SF),\
        NUS-ISS Stackable Certificate Programmes in Digital Solutions Development"

    elif "stackUp - startup tech talent development" in subject:
        s=" NICF- Client Side Foundation (SF),\
        NICF- Containers for Deploying and Scaling Apps (SF),\
        NICF- Data and Feature Engineering for Machine Learning (SF),\
        NICF- Feature Extraction and Supervised Modeling with Deep Learning (SF),\
        NICF- Persistence and Analytics Fundamentals (SF),\
        NICF- Python for Data, Ops and Things (SF),\
        NICF- RESTful API Design (SF),\
        NICF- Security Notification and Messaging Fundamentals (SF),\
        NICF- Sequence Modeling with Deep Learning (SF),\
        NICF- Server Side Foundation (SF),\
        NICF- Supervised and Unsupervised Modeling with Machine Learning (SF)"
# ***************************
# Intent Handlers funcs : END
# ***************************


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)