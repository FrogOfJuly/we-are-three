

label sleepers_station:
    $ state.sleepers_station = Namespace()

    layeredimage station:
        attribute base default

        group heatmap auto:
            attribute fine_heatmap
        
        attribute roommap
        attribute stress

    """
    Your ship matches velocity with a station. 
    
    The ship database could not find any matches for codes on the hull, meaning that this metal structure ages close to a century. 
    
    Indeed before the core ban.

    It's purpose is not apparent, but judging by visible signs of repurposing, 
    most likely the station was designed for asteroid surveys and later found herself involved in some kind of settling effort.
    """

    show station at top
    with dissolve

    # TODO: creepiness needed

    """
    There are no heat signatures visible. Engines are long dead, power source and life-systems are offline. 
    It seems like a space suite is mandatory for the exploration.
    """



    # TODO: Should here be an option for abandoning exploration?


    label .initial_conditions:

    menu: 
        "Who have you arrived with?"

        "You arrived with scavengers from the bar":
            $ state.sleepers_station.arrived_via_scavengers = True
            jump .with_smugglers

        "You arrived by yourself":
            $ state.sleepers_station.arrived_via_scavengers = False
            jump .alone


    

    label .with_smugglers:
        """
        No. Sadly I am not productive to have this written already. Go with other option.
        """
        jump .initial_conditions

    label .alone:
        """
        The station is yours to explore. However, you are but a one human. Your time is limited by the fact that your ship can be detected and followed. 
        
        If you spend here too much time, you can have company. 

        It could either be a scavenger, armed and ready to fight you for the loot, or a passerby who might notify authorities of your findings. 
        Space is an awful place to hide and once travelled to, this station is doomed to be looted for valuables at first and resmelted for metals later. 
        
        Do you want to perform scans and gather information before boarding? 

        Remember, they all take time. 
        """

        python:
            state.sleepers_station.scans = {"mapping", "c_th_scan", "f_th_scan", "radiation", "stress"}

            state.sleepers_station.compartment_mapping = False
            state.sleepers_station.coarse_thermal_scan = False
            state.sleepers_station.fine_thermal_scan    = False
            state.sleepers_station.stress_analysis     = False


        label .preliminary_information_gathering:
            
            menu: 
                "What scans do you want to perform?"

                "Do compartments mapping" if "mapping" in state.sleepers_station.scans: 
                    $ state.sleepers_station.scans.remove("mapping")
                    $ state.sleepers_station.compartment_mapping = True
                    show station roommap
                    with dissolve
                    # "Mapping is complete"
                    jump .preliminary_information_gathering
                "Do coarse thermal scanning" if "c_th_scan" in state.sleepers_station.scans:
                    $ state.sleepers_station.scans.remove("c_th_scan")
                    $ state.sleepers_station.coarse_thermal_scan = True
                    "It seems like some residual heat is still present. Few Kelvins evenly distributed over the whole hull, very likely that there is a ruptured RTG somewhere inside."
                    jump .preliminary_information_gathering
                "Do fine thermal scanning" if "f_th_scan" in state.sleepers_station.scans:
                    $ state.sleepers_station.scans.remove("f_th_scan")
                    $ state.sleepers_station.fine_thermal_scan = True
                    show station fineheatmap
                    with dissolve
                    # "Fine thermal scan is complete: significant gradients found in several compartments"
                    jump .preliminary_information_gathering
                "Do radiation emission scan" if "radiation" in state.sleepers_station.scans:
                    $ state.sleepers_station.scans.remove("radiation")
                    $ state.sleepers_station.radiation_emission_scan = True
                    "Radiation emission scan is complete: No significant emissions found"
                    jump .preliminary_information_gathering
                "Do stress analysis" if "stress" in state.sleepers_station.scans:
                    $ state.sleepers_station.scans.remove("stress")
                    $ state.sleepers_station.stress_analysis = True
                    show station stress
                    with dissolve
                    # "Hull stress is mapped: significant stress found, multiple punctures and forced doors"
                    jump .preliminary_information_gathering
                "Continue with boarding":
                    pass
            
            python:
                del state.sleepers_station.scans

        "What do want to take with you?"
        
        default Item = namedtuple('Item', 'name weight charges')  

        python: 
            state.sleepers_station.equipment         = {}
            state.sleepers_station.carrying_capacity = 50 # kg
            state.sleepers_station.load              = 0  # kg
            state.sleepers_station.time_spent        = 0  # hours
            items = { "bk"    : Item("Bolt cutter", 5, None)
                    , "torch" : Item("Plasma torch", 15, 10)
                    , "m_saw" : Item("Metal-cutting saw", 20, None)
                    , "expl"  : Item("Explosives", 10, 3)}
            it = None
            rem = None

        label .equipment_choice:
            python: 
                rem  = state.sleepers_station.carrying_capacity - state.sleepers_station.load

            menu:
                "
                What do you want to take with you?\n\n

                Your carrying capacity is [state.sleepers_station.carrying_capacity] kg.\n
                You are carrying [state.sleepers_station.load] kg and are able to carry [rem] kg more.\n
                "
                
                "Bring bolt cutter" if "bk" in items:
                    $ it = items["bk"]
                    $ state.sleepers_station.equipment[it.name] = it
                    $ state.sleepers_station.load += it.weight
                    $ del items["bk"]
                    jump .equipment_choice

                "Bring plasma torch" if "torch" in items:
                    $ it = items["torch"]
                    $ state.sleepers_station.equipment[it.name] = it
                    $ state.sleepers_station.load += it.weight
                    $ del items["torch"]
                    jump .equipment_choice
                
                "Bring plasma explosives" if "expl" in items:
                    $ it = items["expl"]
                    $ state.sleepers_station.equipment[it.name] = it
                    $ state.sleepers_station.load += it.weight
                    $ del items["expl"]
                    jump .equipment_choice

                "Bring metal-cutting saw" if "m_saw" in items:
                    $ it = items["m_saw"]
                    $ state.sleepers_station.equipment[it.name] = it
                    $ state.sleepers_station.load += it.weight
                    $ del items["m_saw"]
                    jump .equipment_choice
                
                "Go already!" if not bool(items):
                    pass

                "Go!" if bool(items): 
                    pass
            
            python:
                del rem
                del it
                del items

        jump the_end

        
        




        








