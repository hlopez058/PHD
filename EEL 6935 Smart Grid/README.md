References :



On-line monitoring of power curves
Author links open overlay panelAndrewKusiakHaiyangZhengZheSong
Department of Mechanical and Industrial Engineering, 3131 Seamans Center, The University of Iowa, Iowa City, IA 52242 – 1527, USA
Received 21 May 2008, Accepted 28 October 2008, Available online 6 December 2008.
Abstract
A data-driven approach to the performance analysis of wind turbines is presented. Turbine performance is captured with a power curve. The power curves are constructed using historical wind turbine data. Three power curve models are developed, one by the least squares method and the other by the maximum likelihood estimation method. The models are solved by an evolutionary strategy algorithm. The power curve model constructed by the least squares method outperforms the one built by the maximum likelihood approach. The third model is non-parametric and is built with the k-nearest neighbor (k-NN) algorithm. The least squares (parametric) model and the non-parametric model are used for on-line monitoring of the power curve and their performance is analyzed.


Monitoring of wind farms’ power curves using machine learning techniques
Author links open overlay panelAntoninoMarvugliaaAntonioMessineob
CRP Henri Tudor/CRTE, 66 rue de Luxembourg, L-4002 Esch/Alzette, Luxembourg
Faculty of Engineering & Architecture, Kore University of Enna, Italy
Received 11 November 2011, Revised 11 March 2012, Accepted 24 April 2012, Available online 22 May 2012.
Abstract
The estimation of a wind farm’s power curve, which links the wind speed to the power that is produced by the whole wind farm, is a challenging task because this relationship is nonlinear and bounded, in addition to being non-stationary due for example to changes in the site environment and seasonality. Even for a single wind turbine the measured power at different wind speeds is generally different than the rated power, since the operating conditions on site are generally different than the conditions under which the turbine was calibrated (the wind speed on site is not uniform horizontally across the face of the turbine; the vertical wind profile and the air density are different than during the calibration; the wind data available on site are not always measured at the height of the turbine’s hub).
The paper presents a data-driven approach for building an equivalent steady state model of a wind farm under normal operating conditions and shows its utilization for the creation of quality control charts at the aim of detecting anomalous functioning conditions of the wind farm. We use and compare three different machine learning models – viz. a self-supervised neural network called GMR (Generalized Mapping Regressor), a feed-forward Multi Layer Perceptron (MLP) and a General Regression Neural Network (GRNN) – to estimate the relationship between the wind speed and the generated power in a wind farm. GMR is a novel incremental self-supervised neural network which can approximate every multidimensional function or relation presenting any kind of discontinuity; MLPs are the most widely used state-of-the-art neural network models and GRNNs belong to the family of kernel neural networks.
The methodology allows the creation of a non-parametric model of the power curve that can be used as a reference profile for on-line monitoring of the power generation process, as well as for power forecasts. The results obtained show that the non-parametric approach provides fair performances, provided that a suitable pre-processing of the input data is accomplished.



An Evaluation of Machine Learning Methods to Detect Malicious SCADA Communications
Justin M. Beaver ; Raymond C. Borges-Hink ; Mark A. Buckner
Abstract:
Critical infrastructure Supervisory Control and Data Acquisition (SCADA) systems have been designed to operate on closed, proprietary networks where a malicious insider posed the greatest threat potential. The centralization of control and the movement towards open systems and standards has improved the efficiency of industrial control, but has also exposed legacy SCADA systems to security threats that they were not designed to mitigate. This work explores the viability of machine learning methods in detecting the new threat scenarios of command and data injection. Similar to network intrusion detection systems in the cyber security domain, the command and control communications in a critical infrastructure setting are monitored, and vetted against examples of benign and malicious command traffic, in order to identify potential attack events. Multiple learning methods are evaluated using a dataset of Remote Terminal Unit communications, which included both normal operations and instances of command and data injection attack scenarios.
Published in: 2013 12th International Conference on Machine Learning and Applications
Date of Conference: 4-7 Dec. 2013
Date Added to IEEE Xplore: 10 April 2014
Electronic ISBN: 978-0-7695-5144-9
INSPEC Accession Number: 14222552
DOI: 10.1109/ICMLA.2013.105
Publisher: IEEE
Conference Location: Miami, FL, USA



Using machine learning to predict wind turbine power output
A Clifton1, L Kilcher1, J K Lundquist1,2 and P Fleming1
Published 18 April 2013 • 2013 IOP Publishing Ltd
Environmental Research Letters, Volume 8, Number 2
Abstract
Wind turbine power output is known to be a strong function of wind speed, but is also affected by turbulence and shear. In this work, new aerostructural simulations of a generic 1.5 MW turbine are used to rank atmospheric influences on power output. Most significant is the hub height wind speed, followed by hub height turbulence intensity and then wind speed shear across the rotor disk. These simulation data are used to train regression trees that predict the turbine response for any combination of wind speed, turbulence intensity, and wind shear that might be expected at a turbine site. For a randomly selected atmospheric condition, the accuracy of the regression tree power predictions is three times higher than that from the traditional power curve methodology. The regression tree method can also be applied to turbine test data and used to predict turbine performance at a new site. No new data are required in comparison to the data that are usually collected for a wind resource assessment. Implementing the method requires turbine manufacturers to create a turbine regression tree model from test site data. Such an approach could significantly reduce bias in power predictions that arise because of the different turbulence and shear at the new site, compared to the test site.


Machine learning of rules for a power system alarm processor
 J. Ypsilantis ;  Hansen Yee
 Abstract:
An important function of a supervisory control and data acquisition (SCADA) system is the annunciation of alarms. The aim of alarm processing is to keep the number and annunciation rate of alarms manageable during emergencies. The majority of alarm processors have been implemented as hard-coded rule-based expert systems. The authors describe the use of machine learning to induce knowledge for an alarm processor from alarm sequences obtained via the SCADA from a power distribution system. An evaluation is made using data pertaining to a recent distribution system emergency.<>
Published in: 1991 International Conference on Advances in Power System Control, Operation and Management, APSCOM-91.
Date of Conference: 5-8 Nov. 1991
Date Added to IEEE Xplore: 06 August 2002
Print ISBN: 0-86341-246-7
INSPEC Accession Number: 4117840
Publisher: IET
Conference Location: Hong Kong,


Utilisation of on-line machine learning for SCADA system alarms forecasting
 Tomas Skripcak ;  Pavol Tanuska
 Abstract:
This paper describes a prototype design and implementation of a real-time (on-line) knowledge generation component which can be utilised in industrial Supervisory Control and Data Acquisition (SCADA) systems. The overall architecture of our SCADA scenario, which utilise proposed knowledge generation is based on a multi-agent approach. This design is different from what we can see in conventional commercial SCADA solutions. Nowadays, there is a big pressure on operators to precisely analyse a huge amount of data coming from technological processes and make right decisions in the right time. This is where a real-time knowledge generation can highly improve decision making strategies in complex industrial processes. Nevertheless, the actual state of the art solutions are usually not using the knowledge generation directly, or there are often restricted so called off-line learning approaches. The recent development in the area of machine learning lead to the creation of distributed solutions which could process real-time data and dynamically adapt the generated knowledge. We applied this on-line machine learning approach in our proposed prototype. The experimental agent is focused on the specific scenario of the process alarm forecasting, which is considered to be a binary classification problem. We describe our solution for useful classifier feature vector construction. The classifier itself is based on Passive-Aggressive algorithm. Furthermore, in order to evaluate a performance of the classification the results from knowledge generation experiments were provided in form of Matthews Correlation Coefficient (MCC) together with Receiver Operating Characteristic (ROC). The proposed prototype shows how to design and implement an on-line knowledge generation component for novel SCADA solutions.
Published in: 2013 Science and Information Conference
Date of Conference: 7-9 Oct. 2013
Date Added to IEEE Xplore: 14 November 2013
Electronic ISBN: 978-0-9893193-0-0
INSPEC Accession Number: 13899502
Publisher: IEEE
Conference Location: London, UK


Cloud-Assisted IoT-Based SCADA Systems
Security: A Review of the State of
the Art and Future Challenges
Received February 21, 2016, accepted March 25, 2016, date of publication March 31, 2016, date of current version April 21, 2016.
Digital Object Identifier 10.1109/ACCESS.2016.2549047
ANAM SAJID1
, HAIDER ABBAS2,3, AND KASHIF SALEEM3
1Shaheed Zulfikar Ali Bhutto Institute of Science and Technology, Islamabad 44000, Pakistan
2National University of Sciences and Technology, Islamabad 44000, Pakistan
3Center of Excellence in Information Assurance, King Saud University, Riyadh 11653, Saudi Arabia
Corresponding author: H. Abbas (haiderabbas-mcs@nust.edu.pk)
This work was supported by the National Plan of Science, Technology and Innovation, King Abdulaziz City for
Science and Technology, Saudi Arabia, under Grant 12-INF2817-02.
ABSTRACT Industrial systems always prefer to reduce their operational expenses. To support such reductions,
they need solutions that are capable of providing stability, fault tolerance, and flexibility. One such
solution for industrial systems is cyber physical system (CPS) integration with the Internet of Things (IoT)
utilizing cloud computing services. These CPSs can be considered as smart industrial systems, with their
most prevalent applications in smart transportation, smart grids, smart medical and eHealthcare systems, and
many more. These industrial CPSs mostly utilize supervisory control and data acquisition (SCADA) systems
to control and monitor their critical infrastructure (CI). For example, WebSCADA is an application used for
smart medical technologies, making improved patient monitoring and more timely decisions possible. The
focus of the study presented in this paper is to highlight the security challenges that the industrial SCADA
systems face in an IoT-cloud environment. Classical SCADA systems are already lacking in proper security
measures; however, with the integration of complex new architectures for the future Internet based on the
concepts of IoT, cloud computing, mobile wireless sensor networks, and so on, there are large issues at
stakes in the security and deployment of these classical systems. Therefore, the integration of these future
Internet concepts needs more research effort. This paper, along with highlighting the security challenges of
these CI’s, also provides the existing best practices and recommendations for improving and maintaining
security. Finally, this paper briefly describes future research directions to secure these critical CPSs and help
the research community in identifying the research gaps in this regard.


IoT based SCADA integrated with Fog for power distribution automation
Rijo Jackson Tom ;  Suresh Sankaranarayanan
Abstract:
Electrical Grid we have is more than 50 years old. The integration of information technology to the electric grid system is expected to address many shortcomings of the current and traditional electrical grids that have resulted in Smart Grid which is gaining lot of interest and momentum. In Smart Grid, Power Distribution is one part which requires monitoring and control. Lot of technologies and have been applied in Smart grid towards sensing and action. Supervisory Control and Data Acquisition (SCADA) system is very well proven within the substation region. There has been very less monitoring done on the distribution side due to the geographical distribution. Currently, Internet of Things has paved way for connecting huge number of devices to the Internet which would be very much effective and beneficial for power distribution and Automation. So accordingly, an IoT based SCADA integrated with Fog for Distribution Automation system has been proposed which takes care of the consumer utilization, outage management, power quality control and pole transformer health. This is supported by fog computing which does real-time streaming analytics. This helps in reducing the internet bandwidth and latency for immediate control action.
Published in: 2017 12th Iberian Conference on Information Systems and Technologies (CISTI)
Date of Conference: 21-24 June 2017
Date Added to IEEE Xplore: 13 July 2017
 ISBN Information:
Electronic ISBN: 978-9-8998-4347-9
Print on Demand(PoD) ISBN: 978-1-5090-5047-5
INSPEC Accession Number: 17029038
DOI: 10.23919/CISTI.2017.7975732
Publisher: IEEE
Conference Location: Lisbon, Portugal




CLOUD AND INTELLIGENT BASED
SCADA TECHNOLOGY
Sunaina Sulthana Sk, Geethika Thatiparthi, Raghavendra S Gunturi
ISSN: 2277 – 9043
International Journal of Advanced Research in Computer Science and Electronics Engineering (IJARCSEE)
Volume 2, Issue 3, March 2013


Intelligent SCADA System
Rajeev Kumar Chauhan, M. L. Dewal , Kalpana Chauhan
International Journal on power system optimization and Control Vol.2 No.1 2010
Abstract—Supervisory control and data Acquisition (SCADA)
systems are controlling and monitoring critical plants of the
nation’s infrastructure such as power generation and
distribution, Oil & Gas, water and waste management
etc.Supervisory control and data acquisition is a system in which
message or commands that are individual are sends to the
external world.
 For continuous operations we have to provide uninterrupted
power supply to the industries. But there are many reasons like
breakdown of alternator or increment in load etc. due to which
the interruption may be occur in power supply. In this paper we
have developed an intelligent system using SCADA which will
start spare unit when any one of the running unit will be
breakdown or increment in load.



Distributed SCADA system for optimization of power generation
S. Rominus Valsalam ;  Anish Sathyan ;  S.S. Shankar
Abstract:
According to the International Energy Agency (IEA) the worldpsilas energy needs would be well over 50% higher in 2030 than today at an average annual rate of 1.8% per year. Modern Information Technology based Supervisory Control and Data Acquisition Systems (SCADA) assume greater significance in this context to derive maximum efficiency in power plant operations by ensuring optimal use of available resources. In this paper, we present the salient features of scalable, distributed Intelligent SCADA System developed by Centre for Development of Advanced Computing, Thiruvananthapuram and being implemented in a chain of hydel power stations along the Teesta canal in West Bengal. Besides individual plant monitoring and control, the system facilitates co-ordinated remote monitoring and control of three power stations and their associated canal water flow from a central station. The building blocks of our SCADA technology are well proven in Steel plants, Thermal power plants, Power Distribution Automation Systems, Water treatment plants and other Process industries and Transportation systems. The overall philosophy for system development and implementation is one of distributed structure with redundancy built in at all levels. Advanced Human Machine Interface on modern computer systems, Intelligent Process Controllers, Distributed Control Nodes over the field bus and the plant optimization models depict the superiority of the system. Hydel specific optimization modules are implemented to identify and predict in advance the leakage in fluid flow circuits, in order to take counter measures at the appropriate instants. The system tries to utilize optimally the water flow in the canal for maximum power generation from the plants. The implemented system architecture provides a progressive path of adaptive migration to tomorrow's advanced Automation Systems Technology. After the SCADA system implementation, Power Stations -I, II & III has achieved an increase in power generation by utilizing the water at its maximum.
Published in: 2008 Annual IEEE India Conference
Date of Conference: 11-13 Dec. 2008
Date Added to IEEE Xplore: 27 January 2009
 ISBN Information:
Print ISBN: 978-1-4244-3825-9
CD-ROM ISBN: 978-1-4244-2747-5
Print ISBN: 978-1-4244-3825-9
 ISSN Information:
Print ISSN: 2325-940X
Electronic ISSN: 2325-9418
INSPEC Accession Number: 10478222
DOI: 10.1109/INDCON.2008.4768828
Publisher: IEEE
Conference Location: Kanpur, India


Towards a future SCADA
 Z. A. Vale ;  H. Morais ;  M. Silva ;  C. Ramos
Abstract:
Currently, power systems (PS) already accommodate a substantial penetration of DG and operate in competitive environments. In the future PS will have to deal with large-scale integration of DG and other distributed energy resources (DER), such as storage means, and provide to market agents the means to ensure a flexible and secure operation. This cannot be done with the traditional PS operation. SCADA (supervisory control and data acquisition) is a vital infrastructure for PS. Current SCADA adaptation to accommodate the new needs of future PS does not allow to address all the requirements. In this paper we present a new conceptual design of an intelligent SCADA, with a more decentralized, flexible, and intelligent approach, adaptive to the context (context awareness). Once a situation is characterized, data and control options available to each entity are re-defined according to this context, taking into account operation normative and a priori established contracts. The paper includes a case-study of using future SCADA features to use DER to deal with incident situations, preventing blackouts.
Published in: 2009 IEEE Power & Energy Society General Meeting
Date of Conference: 26-30 July 2009
Date Added to IEEE Xplore: 02 October 2009
Print ISBN: 978-1-4244-4241-6
Print ISSN: 1932-5517
INSPEC Accession Number: 10903822
DOI: 10.1109/PES.2009.5275561
Publisher: IEEE
Conference Location: Calgary, AB, Canada



Distribution system operation supported by contextual energy resource management based on intelligent SCADA
Author links open overlay panelZitaValeHugoMoraisPedroFariaCarlosRamos
GECAD – Knowledge Engineering and Decision Support Research Center, Polytechnic of Porto (IPP), R. Dr. António Bernardino de Almeida, 431, 4200-072 Porto, Portugal
Received 20 December 2011, Accepted 2 October 2012, Available online 22 November 2012.
Abstract
Future distribution systems will have to deal with an intensive penetration of distributed energy resources ensuring reliable and secure operation according to the smart grid paradigm. SCADA (Supervisory Control and Data Acquisition) is an essential infrastructure for this evolution. This paper proposes a new conceptual design of an intelligent SCADA with a decentralized, flexible, and intelligent approach, adaptive to the context (context awareness).
This SCADA model is used to support the energy resource management undertaken by a distribution network operator (DNO). Resource management considers all the involved costs, power flows, and electricity prices, allowing the use of network reconfiguration and load curtailment. Locational Marginal Prices (LMP) are evaluated and used in specific situations to apply Demand Response (DR) programs on a global or a local basis.
The paper includes a case study using a 114 bus distribution network and load demand based on real data.



Intelligent SCADA for Load control
 Filipe Fernandes ;  Tiago Sousa ;  Pedro Faria ;  Marco Silva ;  Hugo Morais ;  Zita A. Vale
 Abstract:
A supervisory control and data acquisition (SCADA) system is an integrated platform that incorporates several components and it has been applied in the field of power systems and several engineering applications to monitor, operate and control a lot of processes. In the future electrical networks, SCADA systems are essential for an intelligent management of resources like distributed generation and demand response, implemented in the smart grid context. This paper presents a SCADA system for a typical residential house. The application is implemented on MOVICON™11 software. The main objective is to manage the residential consumption, reducing or curtailing loads to keep the power consumption in or below a specified setpoint, imposed by the costumer and the generation availability.
Published in: 2010 IEEE International Conference on Systems, Man and Cybernetics
Date of Conference: 10-13 Oct. 2010
Date Added to IEEE Xplore: 22 November 2010
 ISBN Information:
Electronic ISBN: 978-1-4244-6588-0
Print ISBN: 978-1-4244-6586-6
CD-ROM ISBN: 978-1-4244-6587-3
 ISSN Information:
Print ISSN: 1062-922X
CD-ROM ISSN: 1062-922X
INSPEC Accession Number: 11665057
DOI: 10.1109/ICSMC.2010.5641983
Publisher: IEEE
Conference Location: Istanbul, Turkey



Concept design for a Web-based supervisory control and data-acquisition (SCADA) system
 Duo Li ;  Y. Serizawa ;  Mai Kiuchi
 Abstract:
Rapidly advancing hardware and software technologies have made it possible to develop a new generation of supervisory control and data-acquisition (SCADA) system. The Web-based SCADA system described here consists of intelligent RTUs, each of which has a modularized hardware architecture and supports HTTP protocol, and a distributed master station, which has a Web server/browser structure and decomposes the SCADA functions into multiple sets of Web site components. Both the hardware design and software development for this Web-based SCADA system have been carried out in accordance with well-proven architecture modules, allowing the system to benefit from numerous available technologies and giving it added flexibility and scalability.
Published in: IEEE/PES Transmission and Distribution Conference and Exhibition
Date of Conference: 6-10 Oct. 2002
Date Added to IEEE Xplore: 19 February 2003
Print ISBN: 0-7803-7525-4
INSPEC Accession Number: 7651965
DOI: 10.1109/TDC.2002.1178256
Publisher: IEEE
Conference Location: Yokohama, Japan, Japan


Artificial intelligence in short term electric load forecasting: a state-of-the-art survey for the researcher
Author links open overlay panelK.MetaxiotisA.KagiannasD.AskounisJ.Psarras
Department of Electrical and Computer Engineering, National Technical University of Athens, 9 Iroon Polytechniou str., Zografou 15773, Athens, Greece
Received 12 February 2002, Accepted 10 June 2002, Available online 15 October 2002.


Wanted: A more intelligent grid
Jay Giri ;  David Sun ;  Rene Avila-Rosales
Abstract:
This paper presents keys in avoiding total system collapse though enhancing grid reliability and stability with a better, smarter, faster SCADA system.
Published in: IEEE Power and Energy Magazine ( Volume: 7, Issue: 2, March-April 2009 )
Page(s): 34 - 40
Date of Publication: 24 February 2009 
 ISSN Information:
Print ISSN: 1540-7977
Electronic ISSN: 1558-4216
INSPEC Accession Number: 10477183
DOI: 10.1109/MPE.2008.931391
Publisher: IEEE
Sponsored by: IEEE Power & Energy Society