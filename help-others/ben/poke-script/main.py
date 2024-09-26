from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import json


def main():

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()
    print("Driver created")
        # go to the google home page
    driver.get("https://pokemondb.net/pokedex/stats/gen3")
    driver.implicitly_wait(2)

    table = driver.find_element(By.XPATH, "//table[@id='pokedex']")
        # with open("page_source.html", "w+") as f:
        #     f.write(driver.page_source)

    rows = table.text.split("\n")[10:]
    #print("\n".join(rows))
    list_mons= {}
    castform = False
    deoxys = False
    for i in range(0, int(len(rows) / 2)):
        if not castform:
            mon_info = rows[2*i].split(" ")
            mon_stats = rows[2*i + 1].split(" ")
        else:
            mon_info = rows[2*i - 1].split(" ")
            mon_stats = rows[2*i].split(" ")
        ind = 1 if len(mon_stats) == 8 else 0
        name = mon_info[1]
        if name == "Nidoran♀":
            name = "Nidoran-f"
        elif name == "Nidoran♂":
            name = "Nidoran-m"
        elif name == "Mr.":
            name= "Mr-mime"
        elif name == "Castform":
            if castform:
                continue
            castform = True
        elif name.isnumeric() or name == "Form":
            continue
        if name == "Deoxys":
            mon_stats = rows[2*i + 1].split(" ")
            deoxys = True
        print(f"Info: {mon_info}")
        print(f"Stats: {mon_stats}")
        driver.get(f"https://pokemondb.net/pokedex/{name.lower()}")
        try:
            mon_gender = driver.find_element(By.XPATH, "//h2[text()='Breeding']/following-sibling::table[@class='vitals-table']//tr[2]/td/span[@class='text-blue']").text
        except NoSuchElementException:
            mon_gender = -1
        mon = {
            "name": name,
            "number": int(mon_info[0]),
            "BST": mon_stats[ind],
            "HP": mon_stats[ind + 1],
            "Attack": mon_stats[ind + 2],
            "Defense": mon_stats[ind + 3],
            "Sp. Atk": mon_stats[ind + 4],
            "Sp. Def": mon_stats[ind + 5],
            "Speed": mon_stats[ind + 6],
            "Male Gender Ratio": mon_gender,
        }
        list_mons[int(mon_info[0])] = mon

        if deoxys:
            break

    with open("pokemon-stats-gen3.json", "w+") as f:
        json.dump(list_mons, f, indent=4)

    print(list_mons)



if __name__ == "__main__":
    main()
