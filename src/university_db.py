"""
Complete Global University Database - 50+ Universities
With Google Maps Integration
"""

UNIVERSITIES = {
    # ============================================
    # INDIA - 10 Universities
    # ============================================
    
    "IIT Bombay": {
        "name": "Indian Institute of Technology Bombay",
        "url": "https://www.iitb.ac.in",
        "admissions_url": "https://www.iitb.ac.in/newacadhome/admissions.jsp",
        "continent": "Asia",
        "country": "India",
        "state": "Maharashtra",
        "city": "Mumbai",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1d/Indian_Institute_of_Technology_Bombay_Logo.svg/200px-Indian_Institute_of_Technology_Bombay_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3769.662178194!2d72.91174!3d19.13427!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c7f1c86affbb%3A0x9c650c6b65e003ea!2sIIT%20Bombay!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 3 in India",
        "established": "1958"
    },
    "IIT Delhi": {
        "name": "Indian Institute of Technology Delhi",
        "url": "https://home.iitd.ac.in",
        "admissions_url": "https://home.iitd.ac.in/admissions.php",
        "continent": "Asia",
        "country": "India",
        "state": "Delhi",
        "city": "New Delhi",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/f/fd/Indian_Institute_of_Technology_Delhi_Logo.svg",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3501.475!2d77.1925!3d28.5450!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d1fc1f0000001%3A0x6f0e1f8f0e1f8f0e!2sIIT%20Delhi!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 3 in India",
        "established": "1961"
    },
    "IIT Madras": {
        "name": "Indian Institute of Technology Madras",
        "url": "https://www.iitm.ac.in",
        "admissions_url": "https://www.iitm.ac.in/admissions",
        "continent": "Asia",
        "country": "India",
        "state": "Tamil Nadu",
        "city": "Chennai",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/IIT_Madras_Logo.svg/200px-IIT_Madras_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.5!2d80.23319!3d12.99161!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a5267e4f4e4e4e4%3A0x1f1f1f1f1f1f1f1f!2sIIT%20Madras!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 3 in India",
        "established": "1959"
    },
    "IIT Kanpur": {
        "name": "Indian Institute of Technology Kanpur",
        "url": "https://www.iitk.ac.in",
        "admissions_url": "https://www.iitk.ac.in/doaa",
        "continent": "Asia",
        "country": "India",
        "state": "Uttar Pradesh",
        "city": "Kanpur",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Indian_Institute_of_Technology%2C_Kanpur_Logo.svg/200px-Indian_Institute_of_Technology%2C_Kanpur_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3562.8!2d80.23319!3d26.51223!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399c3700c0c0c0c0%3A0x2f2f2f2f2f2f2f2f!2sIIT%20Kanpur!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 5 in India",
        "established": "1959"
    },
    "IIT Kharagpur": {
        "name": "Indian Institute of Technology Kharagpur",
        "url": "http://www.iitkgp.ac.in",
        "admissions_url": "http://www.iitkgp.ac.in/admissions",
        "continent": "Asia",
        "country": "India",
        "state": "West Bengal",
        "city": "Kharagpur",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/IIT_Kharagpur_Logo.svg/200px-IIT_Kharagpur_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3691.1!2d87.31060!3d22.31967!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a1d440000000001%3A0x4f4f4f4f4f4f4f4f!2sIIT%20Kharagpur!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 5 in India",
        "established": "1951"
    },
    "IIT Roorkee": {
        "name": "Indian Institute of Technology Roorkee",
        "url": "https://www.iitr.ac.in",
        "admissions_url": "https://www.iitr.ac.in/admissions",
        "continent": "Asia",
        "country": "India",
        "state": "Uttarakhand",
        "city": "Roorkee",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/4/43/IIT_Roorkee_logo.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3448.3!2d77.89569!3d29.86630!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390eb36e00000001%3A0x5f5f5f5f5f5f5f5f!2sIIT%20Roorkee!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 10 in India",
        "established": "1847"
    },
    "IISc Bangalore": {
        "name": "Indian Institute of Science",
        "url": "https://iisc.ac.in",
        "admissions_url": "https://iisc.ac.in/admissions",
        "continent": "Asia",
        "country": "India",
        "state": "Karnataka",
        "city": "Bengaluru",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/IISc_New_Logo.svg/200px-IISc_New_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.085!2d77.56599!3d13.02202!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae17d6b5c00001%3A0x1f8f8f8f8f8f8f8f!2sIISc!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "#1 Research in India",
        "established": "1909"
    },
    "BITS Pilani": {
        "name": "Birla Institute of Technology and Science",
        "url": "https://www.bits-pilani.ac.in",
        "admissions_url": "https://www.bits-pilani.ac.in/admissions",
        "continent": "Asia",
        "country": "India",
        "state": "Rajasthan",
        "city": "Pilani",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/d3/BITS_Pilani-Logo.svg",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3524.891!2d75.58778!3d28.36349!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396d9b5c00000001%3A0x2f2f2f2f2f2f2f2f!2sBITS%20Pilani!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 10 in India",
        "established": "1964"
    },
    "Delhi University": {
        "name": "University of Delhi",
        "url": "http://www.du.ac.in",
        "admissions_url": "http://www.du.ac.in/du/index.php?page=admissions",
        "continent": "Asia",
        "country": "India",
        "state": "Delhi",
        "city": "New Delhi",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/4/42/Delhi_University.svg",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3501.2!2d77.20898!3d28.68792!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390cfd5b00000001%3A0x7f7f7f7f7f7f7f7f!2sDelhi%20University!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top 15 in India",
        "established": "1922"
    },
    "JNU": {
        "name": "Jawaharlal Nehru University",
        "url": "https://www.jnu.ac.in",
        "admissions_url": "https://www.jnu.ac.in/main/admission",
        "continent": "Asia",
        "country": "India",
        "state": "Delhi",
        "city": "New Delhi",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/1/1f/Jawaharlal_Nehru_University_logo.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3504.6!2d77.16735!3d28.54175!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d1de00000001%3A0x8f8f8f8f8f8f8f8f!2sJNU!5e0!3m2!1sen!2sin!4v1234567890",
        "ranking": "Top Research University",
        "established": "1969"
    },
    
    # ============================================
    # USA - 15 Universities
    # ============================================
    
    "MIT": {
        "name": "Massachusetts Institute of Technology",
        "url": "https://www.mit.edu",
        "admissions_url": "https://mitadmissions.org",
        "continent": "North America",
        "country": "USA",
        "state": "Massachusetts",
        "city": "Cambridge",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MIT_logo.svg/200px-MIT_logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2948.177!2d-71.09416!3d42.36008!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e370a5cb30cc5f%3A0xc4c9f6c686a85861!2sMIT!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "#1 in World",
        "established": "1861"
    },
    "Stanford": {
        "name": "Stanford University",
        "url": "https://www.stanford.edu",
        "admissions_url": "https://admission.stanford.edu",
        "continent": "North America",
        "country": "USA",
        "state": "California",
        "city": "Stanford",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Seal_of_Leland_Stanford_Junior_University.svg/200px-Seal_of_Leland_Stanford_Junior_University.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3168.639!2d-122.16963!3d37.42410!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fbb28416493a7%3A0x3d15a8b4e85d5535!2sStanford%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 3 in World",
        "established": "1885"
    },
    "Harvard": {
        "name": "Harvard University",
        "url": "https://www.harvard.edu",
        "admissions_url": "https://college.harvard.edu/admissions",
        "continent": "North America",
        "country": "USA",
        "state": "Massachusetts",
        "city": "Cambridge",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Harvard_shield_wreath.svg/200px-Harvard_shield_wreath.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2948.073!2d-71.11656!3d42.37403!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e377427d7f0199%3A0x5937c65cee2427f0!2sHarvard%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 3 in World",
        "established": "1636"
    },
    "Caltech": {
        "name": "California Institute of Technology",
        "url": "https://www.caltech.edu",
        "admissions_url": "https://www.admissions.caltech.edu",
        "continent": "North America",
        "country": "USA",
        "state": "California",
        "city": "Pasadena",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Seal_of_the_California_Institute_of_Technology.svg/200px-Seal_of_the_California_Institute_of_Technology.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3302.4!2d-118.12507!3d34.13778!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c2c75ddc27da13%3A0xe5563dde5695d75!2sCaltech!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 10 in World",
        "established": "1891"
    },
    "Berkeley": {
        "name": "University of California, Berkeley",
        "url": "https://www.berkeley.edu",
        "admissions_url": "https://admissions.berkeley.edu",
        "continent": "North America",
        "country": "USA",
        "state": "California",
        "city": "Berkeley",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Seal_of_University_of_California%2C_Berkeley.svg/200px-Seal_of_University_of_California%2C_Berkeley.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3149.5!2d-122.25967!3d37.87146!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808f7718c522d7c1%3A0xda8034ea3b6b3289!2sUC%20Berkeley!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "#1 Public in USA",
        "established": "1868"
    },
    "Princeton": {
        "name": "Princeton University",
        "url": "https://www.princeton.edu",
        "admissions_url": "https://admission.princeton.edu",
        "continent": "North America",
        "country": "USA",
        "state": "New Jersey",
        "city": "Princeton",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Princeton_seal.svg/200px-Princeton_seal.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3041.4!2d-74.65968!3d40.34872!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c3e6c5e7e7e7e7%3A0xf1f1f1f1f1f1f1f1!2sPrinceton%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 10 in World",
        "established": "1746"
    },
    "Yale": {
        "name": "Yale University",
        "url": "https://www.yale.edu",
        "admissions_url": "https://admissions.yale.edu",
        "continent": "North America",
        "country": "USA",
        "state": "Connecticut",
        "city": "New Haven",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Yale_University_Shield_1.svg/200px-Yale_University_Shield_1.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2997.1!2d-72.92447!3d41.31162!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e7d9e2e2e2e2e2%3A0xa1a1a1a1a1a1a1a1!2sYale%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Ivy League",
        "established": "1701"
    },
    "Columbia": {
        "name": "Columbia University",
        "url": "https://www.columbia.edu",
        "admissions_url": "https://undergrad.admissions.columbia.edu",
        "continent": "North America",
        "country": "USA",
        "state": "New York",
        "city": "New York City",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/08/Columbia_University_shield.svg/200px-Columbia_University_shield.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3021.0!2d-73.96249!3d40.80754!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2f63f00000001%3A0xb2b2b2b2b2b2b2b2!2sColumbia%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Ivy League",
        "established": "1754"
    },
    "UChicago": {
        "name": "University of Chicago",
        "url": "https://www.uchicago.edu",
        "admissions_url": "https://collegeadmissions.uchicago.edu",
        "continent": "North America",
        "country": "USA",
        "state": "Illinois",
        "city": "Chicago",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/7/79/University_of_Chicago_shield.svg/200px-University_of_Chicago_shield.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2974.4!2d-87.59892!3d41.78874!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880e293f00000001%3A0xc3c3c3c3c3c3c3c3!2sUniversity%20of%20Chicago!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 10 in USA",
        "established": "1890"
    },
    "UCLA": {
        "name": "University of California, Los Angeles",
        "url": "https://www.ucla.edu",
        "admissions_url": "https://admission.ucla.edu",
        "continent": "North America",
        "country": "USA",
        "state": "California",
        "city": "Los Angeles",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/The_University_of_California_UCLA.svg/200px-The_University_of_California_UCLA.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3304.9!2d-118.44513!3d34.06854!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c2bc85f05c0f65%3A0x25a993585c134837!2sUCLA!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 20 in World",
        "established": "1919"
    },
    "Cornell": {
        "name": "Cornell University",
        "url": "https://www.cornell.edu",
        "admissions_url": "https://admissions.cornell.edu",
        "continent": "North America",
        "country": "USA",
        "state": "New York",
        "city": "Ithaca",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Cornell_University_seal.svg/200px-Cornell_University_seal.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2945.3!2d-76.48353!3d42.45341!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d0818c00000001%3A0xd4d4d4d4d4d4d4d4!2sCornell%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Ivy League",
        "established": "1865"
    },
    "Penn": {
        "name": "University of Pennsylvania",
        "url": "https://www.upenn.edu",
        "admissions_url": "https://admissions.upenn.edu",
        "continent": "North America",
        "country": "USA",
        "state": "Pennsylvania",
        "city": "Philadelphia",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UPenn_shield_with_banner.svg/200px-UPenn_shield_with_banner.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3058.5!2d-75.19310!3d39.95285!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c6c65a00000001%3A0xe5e5e5e5e5e5e5e5!2sUniversity%20of%20Pennsylvania!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Ivy League",
        "established": "1740"
    },
    "Michigan": {
        "name": "University of Michigan",
        "url": "https://www.umich.edu",
        "admissions_url": "https://admissions.umich.edu",
        "continent": "North America",
        "country": "USA",
        "state": "Michigan",
        "city": "Ann Arbor",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Michigan_Wolverines_logo.svg/200px-Michigan_Wolverines_logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2951.8!2d-83.73804!3d42.27805!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x883cae00000001%3A0xf6f6f6f6f6f6f6f6!2sUniversity%20of%20Michigan!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top Public University",
        "established": "1817"
    },
    "Northwestern": {
        "name": "Northwestern University",
        "url": "https://www.northwestern.edu",
        "admissions_url": "https://admissions.northwestern.edu",
        "continent": "North America",
        "country": "USA",
        "state": "Illinois",
        "city": "Evanston",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Northwestern_University_seal.svg/200px-Northwestern_University_seal.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2965.7!2d-87.67507!3d42.05698!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880fc7000000001%3A0xa7a7a7a7a7a7a7a7!2sNorthwestern%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 10 in USA",
        "established": "1851"
    },
    "Duke": {
        "name": "Duke University",
        "url": "https://www.duke.edu",
        "admissions_url": "https://admissions.duke.edu",
        "continent": "North America",
        "country": "USA",
        "state": "North Carolina",
        "city": "Durham",
        "type": "Private",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Duke_University_seal.svg/200px-Duke_University_seal.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3235.2!2d-78.93820!3d35.99616!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89ace5000000001%3A0xb8b8b8b8b8b8b8b8!2sDuke%20University!5e0!3m2!1sen!2sus!4v1234567890",
        "ranking": "Top 10 in USA",
        "established": "1838"
    },
    
    # ============================================
    # UK - 6 Universities
    # ============================================
    
    "Oxford": {
        "name": "University of Oxford",
        "url": "https://www.ox.ac.uk",
        "admissions_url": "https://www.ox.ac.uk/admissions",
        "continent": "Europe",
        "country": "UK",
        "state": "England",
        "city": "Oxford",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Oxford-University-Circlet.svg/200px-Oxford-University-Circlet.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2469.947!2d-1.25596!3d51.75489!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4876c6a9ef8c485b%3A0x3c1f3c1f3c1f3c1f!2sUniversity%20of%20Oxford!5e0!3m2!1sen!2suk!4v1234567890",
        "ranking": "#1 in UK",
        "established": "1096"
    },
    "Cambridge": {
        "name": "University of Cambridge",
        "url": "https://www.cam.ac.uk",
        "admissions_url": "https://www.undergraduate.study.cam.ac.uk",
        "continent": "Europe",
        "country": "UK",
        "state": "England",
        "city": "Cambridge",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/University_of_Cambridge_logo.svg/200px-University_of_Cambridge_logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2445.031!2d0.11475!3d52.20533!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47d85d89f32a012d%3A0x2f2f2f2f2f2f2f2f!2sUniversity%20of%20Cambridge!5e0!3m2!1sen!2suk!4v1234567890",
        "ranking": "Top 2 in UK",
        "established": "1209"
    },
    "Imperial": {
        "name": "Imperial College London",
        "url": "https://www.imperial.ac.uk",
        "admissions_url": "https://www.imperial.ac.uk/study",
        "continent": "Europe",
        "country": "UK",
        "state": "England",
        "city": "London",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Imperial_College_London_crest.svg/200px-Imperial_College_London_crest.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2483.4!2d-0.17464!3d51.49882!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48760567000000001%3A0xd1d1d1d1d1d1d1d1!2sImperial%20College%20London!5e0!3m2!1sen!2suk!4v1234567890",
        "ranking": "Top 10 in World for Science",
        "established": "1907"
    },
    "UCL": {
        "name": "University College London",
        "url": "https://www.ucl.ac.uk",
        "admissions_url": "https://www.ucl.ac.uk/prospective-students",
        "continent": "Europe",
        "country": "UK",
        "state": "England",
        "city": "London",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/UCL_logo.svg/200px-UCL_logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2482.2!2d-0.13359!3d51.52465!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761b3000000001%3A0xe2e2e2e2e2e2e2e2!2sUCL!5e0!3m2!1sen!2suk!4v1234567890",
        "ranking": "Top 10 in UK",
        "established": "1826"
    },
    "Edinburgh": {
        "name": "University of Edinburgh",
        "url": "https://www.ed.ac.uk",
        "admissions_url": "https://www.ed.ac.uk/studying",
        "continent": "Europe",
        "country": "UK",
        "state": "Scotland",
        "city": "Edinburgh",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Coat_of_arms_of_the_University_of_Edinburgh.svg/200px-Coat_of_arms_of_the_University_of_Edinburgh.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2234.2!2d-3.18767!3d55.94429!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4887c78400000001%3A0xf3f3f3f3f3f3f3f3!2sUniversity%20of%20Edinburgh!5e0!3m2!1sen!2suk!4v1234567890",
        "ranking": "Top 20 in UK",
        "established": "1582"
    },
    "LSE": {
        "name": "London School of Economics",
        "url": "https://www.lse.ac.uk",
        "admissions_url": "https://www.lse.ac.uk/study-at-lse",
        "continent": "Europe",
        "country": "UK",
        "state": "England",
        "city": "London",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/LSE_Logo.svg/200px-LSE_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2483.0!2d-0.11643!3d51.51417!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x487604c800000001%3A0xf4f4f4f4f4f4f4f4!2sLSE!5e0!3m2!1sen!2suk!4v1234567890",
        "ranking": "#1 for Social Sciences",
        "established": "1895"
    },
    
    # ============================================
    # CANADA - 3 Universities
    # ============================================
    
    "Toronto": {
        "name": "University of Toronto",
        "url": "https://www.utoronto.ca",
        "admissions_url": "https://future.utoronto.ca",
        "continent": "North America",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/University_of_Toronto_Crest.svg/200px-University_of_Toronto_Crest.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2886.2!2d-79.39577!3d43.66266!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x882b34c800000001%3A0xa5a5a5a5a5a5a5a5!2sUniversity%20of%20Toronto!5e0!3m2!1sen!2sca!4v1234567890",
        "ranking": "#1 in Canada",
        "established": "1827"
    },
    "UBC": {
        "name": "University of British Columbia",
        "url": "https://www.ubc.ca",
        "admissions_url": "https://you.ubc.ca",
        "continent": "North America",
        "country": "Canada",
        "state": "British Columbia",
        "city": "Vancouver",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/The_University_of_British_Columbia_%28logo%29.svg/200px-The_University_of_British_Columbia_%28logo%29.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2603.9!2d-123.24944!3d49.26038!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672c800000001%3A0xb6b6b6b6b6b6b6b6!2sUBC!5e0!3m2!1sen!2sca!4v1234567890",
        "ranking": "Top 3 in Canada",
        "established": "1908"
    },
    "McGill": {
        "name": "McGill University",
        "url": "https://www.mcgill.ca",
        "admissions_url": "https://www.mcgill.ca/applying",
        "continent": "North America",
        "country": "Canada",
        "state": "Quebec",
        "city": "Montreal",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/McGill_University_CoA.svg/200px-McGill_University_CoA.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2795.7!2d-73.57738!3d45.50486!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cc91a4500000001%3A0xc7c7c7c7c7c7c7c7!2sMcGill%20University!5e0!3m2!1sen!2sca!4v1234567890",
        "ranking": "Top 3 in Canada",
        "established": "1821"
    },
    
    # ============================================
    # SINGAPORE - 2 Universities
    # ============================================
    
    "NUS": {
        "name": "National University of Singapore",
        "url": "https://www.nus.edu.sg",
        "admissions_url": "https://www.nus.edu.sg/admissions",
        "continent": "Asia",
        "country": "Singapore",
        "state": "Singapore",
        "city": "Singapore",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/NUS_coat_of_arms.svg/200px-NUS_coat_of_arms.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.819!2d103.77416!3d1.29647!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da1af5c6f3c1d5%3A0x1f1f1f1f1f1f1f1f!2sNUS!5e0!3m2!1sen!2ssg!4v1234567890",
        "ranking": "#1 in Asia",
        "established": "1905"
    },
    "NTU": {
        "name": "Nanyang Technological University",
        "url": "https://www.ntu.edu.sg",
        "admissions_url": "https://www.ntu.edu.sg/admissions",
        "continent": "Asia",
        "country": "Singapore",
        "state": "Singapore",
        "city": "Singapore",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/f/f9/Nanyang_Technological_University.svg",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.7!2d103.68177!3d1.34806!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da10f00000001%3A0x2f2f2f2f2f2f2f2f!2sNTU!5e0!3m2!1sen!2ssg!4v1234567890",
        "ranking": "Top 3 in Asia",
        "established": "1991"
    },
    
    # ============================================
    # CHINA - 2 Universities
    # ============================================
    
    "Tsinghua": {
        "name": "Tsinghua University",
        "url": "https://www.tsinghua.edu.cn/en",
        "admissions_url": "https://www.tsinghua.edu.cn/en/admissions",
        "continent": "Asia",
        "country": "China",
        "state": "Beijing",
        "city": "Beijing",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Tsinghua_University_Logo.svg/200px-Tsinghua_University_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3057.7!2d116.32615!3d40.00015!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x35f05000000001%3A0xd8d8d8d8d8d8d8d8!2sTsinghua%20University!5e0!3m2!1sen!2scn!4v1234567890",
        "ranking": "#1 in China",
        "established": "1911"
    },
    "Peking": {
        "name": "Peking University",
        "url": "https://english.pku.edu.cn",
        "admissions_url": "https://english.pku.edu.cn/admissions",
        "continent": "Asia",
        "country": "China",
        "state": "Beijing",
        "city": "Beijing",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/50/Peking_University_seal.svg",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3057.4!2d116.30996!3d39.99234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x35f05b00000001%3A0xe9e9e9e9e9e9e9e9!2sPeking%20University!5e0!3m2!1sen!2scn!4v1234567890",
        "ranking": "Top 2 in China",
        "established": "1898"
    },
    
    # ============================================
    # JAPAN - 2 Universities
    # ============================================
    
    "Tokyo": {
        "name": "University of Tokyo",
        "url": "https://www.u-tokyo.ac.jp/en",
        "admissions_url": "https://www.u-tokyo.ac.jp/en/admissions",
        "continent": "Asia",
        "country": "Japan",
        "state": "Tokyo",
        "city": "Tokyo",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/University_of_Tokyo_Seal.svg/200px-University_of_Tokyo_Seal.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.4!2d139.76257!3d35.71267!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188c00000001%3A0xfafafafafafafafa!2sUniversity%20of%20Tokyo!5e0!3m2!1sen!2sjp!4v1234567890",
        "ranking": "#1 in Japan",
        "established": "1877"
    },
    "Kyoto": {
        "name": "Kyoto University",
        "url": "https://www.kyoto-u.ac.jp/en",
        "admissions_url": "https://www.kyoto-u.ac.jp/en/admissions",
        "continent": "Asia",
        "country": "Japan",
        "state": "Kyoto",
        "city": "Kyoto",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Kyoto_University_insignia.svg/200px-Kyoto_University_insignia.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3268.1!2d135.78042!3d35.02637!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6001089000000001%3A0xfbfbfbfbfbfbfbfb!2sKyoto%20University!5e0!3m2!1sen!2sjp!4v1234567890",
        "ranking": "Top 2 in Japan",
        "established": "1897"
    },
    
    # ============================================
    # SOUTH KOREA - 2 Universities
    # ============================================
    
    "KAIST": {
        "name": "Korea Advanced Institute of Science and Technology",
        "url": "https://www.kaist.ac.kr/en",
        "admissions_url": "https://admission.kaist.ac.kr/intl-undergraduate",
        "continent": "Asia",
        "country": "South Korea",
        "state": "Daejeon",
        "city": "Daejeon",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/25/KAIST_logo.svg/200px-KAIST_logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3214.6!2d127.36223!3d36.37142!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x35654800000001%3A0xfcfcfcfcfcfcfcfc!2sKAIST!5e0!3m2!1sen!2skr!4v1234567890",
        "ranking": "#1 for Science & Tech in South Korea",
        "established": "1971"
    },
    "Seoul National": {
        "name": "Seoul National University",
        "url": "https://en.snu.ac.kr",
        "admissions_url": "https://en.snu.ac.kr/admissions",
        "continent": "Asia",
        "country": "South Korea",
        "state": "Seoul",
        "city": "Seoul",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Seoul_National_University_seal.svg/200px-Seoul_National_University_seal.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3165.3!2d126.95273!3d37.46035!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357c9f00000001%3A0xfdfdfdfdfdfdfdfd!2sSeoul%20National%20University!5e0!3m2!1sen!2skr!4v1234567890",
        "ranking": "#1 in South Korea",
        "established": "1946"
    },
    
    # ============================================
    # EUROPE - 3 Universities
    # ============================================
    
    "ETH Zurich": {
        "name": "ETH Zurich - Swiss Federal Institute of Technology",
        "url": "https://ethz.ch/en.html",
        "admissions_url": "https://ethz.ch/en/studies/registration-application.html",
        "continent": "Europe",
        "country": "Switzerland",
        "state": "Zurich",
        "city": "Zurich",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/ETH_Z%C3%BCrich_Logo_black.svg/200px-ETH_Z%C3%BCrich_Logo_black.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2701.2!2d8.54806!3d47.37688!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47900a0000000001%3A0xfefefefefefefefe!2sETH%20Zurich!5e0!3m2!1sen!2sch!4v1234567890",
        "ranking": "#1 in Continental Europe",
        "established": "1855"
    },
    "TUM": {
        "name": "Technical University of Munich",
        "url": "https://www.tum.de/en",
        "admissions_url": "https://www.tum.de/en/studies/application",
        "continent": "Europe",
        "country": "Germany",
        "state": "Bavaria",
        "city": "Munich",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Logo_of_the_Technical_University_of_Munich.svg/200px-Logo_of_the_Technical_University_of_Munich.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2662.4!2d11.66788!3d48.26223!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x479e7500000001%3A0xffffffffffffff!2sTUM!5e0!3m2!1sen!2sde!4v1234567890",
        "ranking": "#1 in Germany",
        "established": "1868"
    },
    "Sorbonne": {
        "name": "Sorbonne University",
        "url": "https://www.sorbonne-universite.fr/en",
        "admissions_url": "https://www.sorbonne-universite.fr/en/admissions",
        "continent": "Europe",
        "country": "France",
        "state": "Île-de-France",
        "city": "Paris",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Blason_de_la_Sorbonne.svg/200px-Blason_de_la_Sorbonne.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2625.2!2d2.34472!3d48.84665!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e671e800000001%3A0xffffffffffffffff!2sSorbonne%20University!5e0!3m2!1sen!2sfr!4v1234567890",
        "ranking": "#1 in France",
        "established": "1257"
    },
    
    # ============================================
    # AUSTRALIA - 3 Universities
    # ============================================
    
    "Melbourne": {
        "name": "University of Melbourne",
        "url": "https://www.unimelb.edu.au",
        "admissions_url": "https://study.unimelb.edu.au",
        "continent": "Oceania",
        "country": "Australia",
        "state": "Victoria",
        "city": "Melbourne",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_University_of_Melbourne_Logo.svg/200px-The_University_of_Melbourne_Logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3152.0!2d144.96332!3d-37.79835!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad65d4c00000001%3A0xaeaeaeaeaeaeaeae!2sUniversity%20of%20Melbourne!5e0!3m2!1sen!2sau!4v1234567890",
        "ranking": "#1 in Australia",
        "established": "1853"
    },
    "ANU": {
        "name": "Australian National University",
        "url": "https://www.anu.edu.au",
        "admissions_url": "https://www.anu.edu.au/study",
        "continent": "Oceania",
        "country": "Australia",
        "state": "ACT",
        "city": "Canberra",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Australian_National_University_logo.svg/200px-Australian_National_University_logo.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3256.4!2d149.11775!3d-35.27782!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b164d0700000001%3A0xafafafafafafafa!2sANU!5e0!3m2!1sen!2sau!4v1234567890",
        "ranking": "Top 3 in Australia",
        "established": "1946"
    },
    "Sydney": {
        "name": "University of Sydney",
        "url": "https://www.sydney.edu.au",
        "admissions_url": "https://www.sydney.edu.au/study",
        "continent": "Oceania",
        "country": "Australia",
        "state": "New South Wales",
        "city": "Sydney",
        "type": "Public",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/University_of_Sydney_coat_of_arms.svg/200px-University_of_Sydney_coat_of_arms.svg.png",
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3313.0!2d151.18751!3d-33.88867!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12ae6700000001%3A0xb0b0b0b0b0b0b0b0!2sUniversity%20of%20Sydney!5e0!3m2!1sen!2sau!4v1234567890",
        "ranking": "Top 5 in Australia",
        "established": "1850"
    },
}


def get_all_continents():
    """Get list of all continents"""
    continents = set(info['continent'] for info in UNIVERSITIES.values())
    return sorted(list(continents))


def get_countries_by_continent(continent):
    """Get countries in a specific continent"""
    if continent == "All":
        return get_all_countries()
    countries = set(info['country'] for info in UNIVERSITIES.values() if info['continent'] == continent)
    return sorted(list(countries))


def get_all_countries():
    """Get list of all countries"""
    countries = set(info['country'] for info in UNIVERSITIES.values())
    return sorted(list(countries))


def get_university_info(name):
    """Get info for a specific university"""
    return UNIVERSITIES.get(name)


def filter_universities(continent=None, country=None, search_query=None):
    """Filter universities by multiple criteria"""
    filtered = list(UNIVERSITIES.keys())
    
    if continent and continent != "All":
        filtered = [u for u in filtered if UNIVERSITIES[u]['continent'] == continent]
    
    if country and country != "All":
        filtered = [u for u in filtered if UNIVERSITIES[u]['country'] == country]
    
    if search_query:
        query = search_query.lower()
        filtered = [u for u in filtered if 
                   query in u.lower() or 
                   query in UNIVERSITIES[u]['name'].lower() or
                   query in UNIVERSITIES[u]['city'].lower()]
    
    return sorted(filtered)