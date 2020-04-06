# C.Reinhardtii-Project
Assembly logic formalisation
Due to the growing library of available parts at the Purton lab, 
we are working on making the repository as well as the design approach 
more accessible to the broader algal biotechnology community. 
Thus far, the constructs are designed in-silico on the Benchling bioinformatics platform. 
To enhance this part of the assembly process we have been developing a graphical user interface (GUI) 
to guide and facilitate the assembly process. Due to the standardised nature of the assembly, 
the logic can be formalised and presented in a simple design environment, where a user can customize
the cassette design for their specific purpose. Future availability of validated regulatory sequence 
data with expected expression outcome will also enhance the potential of such a platform for a more 
precise expression cassette design. The project is currently in early stages where we have managed to 
formalize the design logic, integrate the underlying parts repository database for sequence exploration 
as well as design a basic assembly bench module where level 0 parts can be chosen from the database and 
assembled into expression cassettes. The assembled cassette sequences, containing all the relevant fusion 
and restriction sites can then be inspected and extracted for further analysis. Additional features are also 
currently in development. For example, an assembly reaction calculator module, where once the desired plasmid 
parts are obtained, the assembly reaction stoichiometry is calculated based on DNA concentration. Additionally, 
we aim to integrate construct sequence file extraction in GenBank format (Benson et al., 2013), which would allow 
for sequence annotations of each element in the construct including restriction, fusion sites. As the framework 
is not yet suitable for deployment, we have been exploring the optimal approach to broaden availability, such as 
a web-based application. The web-based application could be integrated into existing C. reinhardtii resource 
repositories such as the Chlamydomonas Resource Center  (https://www.chlamycollection.org) for broader 
research support. 
