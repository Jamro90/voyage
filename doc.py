
def sort_list(pchor_list):
    pchor_list_mod = []
    
    # deleting labels row
    pchor_list.pop(0)
    for pchor in pchor_list:
        # changing string in to array
        line = pchor.split(",")
        # removing indexing
        line.pop(0)
        pchor_list_mod.append(line)
    # sorting levels
    pchor_list_mod.sort()
    # making levels arrays
    sergant_list = []
    platoon_sergant_list = []
    corporal_1_list = []
    corporal_list = []
    private_1_list = []
    private_list = []

    # sorting levels
    for pchor in pchor_list_mod:
        if pchor[0] == "sierż. pchor.":
            sergant_list.append(pchor)
        
        elif pchor[0] == "plut. pchor.":
            platoon_sergant_list.append(pchor)
        
        elif pchor[0] == "st. kpr. pchor.":
            corporal_1_list.append(pchor)
        
        elif pchor[0] == "kpr. pchor.":
            corporal_list.append(pchor)
            
        elif pchor[0] == "st. szer. pchor.":
            private_1_list.append(pchor)
            
        elif pchor[0] == "szer. pchor.":
            private_list.append(pchor)
        
        else:
            print("nie działa")

    # making correct indexing
    i = 1
    for sergant in sergant_list:
        sergant.insert(0, i)
        i += 1
    for platoon_sergant in platoon_sergant_list:
        platoon_sergant.insert(0, i)
        i += 1
    for corporal_1 in corporal_1_list:
        corporal_1.insert(0, i)
        i += 1
    for corporal in corporal_list:
        corporal.insert(0, i)
        i += 1
    for private_1 in private_1_list:
        private_1.insert(0, i)
        i += 1
    for private in private_list:
        private.insert(0, i)
        i += 1
    
    # finale sorting algorithm
    num_sorted_list = []
    for sergant in sergant_list:
        num_sorted_list.append(sergant)
    for platoon_sergant in platoon_sergant_list:
        num_sorted_list.append(platoon_sergant)
    for corporal_1 in corporal_1_list:
        num_sorted_list.append(corporal_1)
    for corporal in corporal_list:
        num_sorted_list.append(corporal)
    for private_1 in private_1_list:
        num_sorted_list.append(private_1)
    for private in private_list:
        num_sorted_list.append(private)

