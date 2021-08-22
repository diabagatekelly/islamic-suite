import json, os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def dataAnalysis():
    rule = request.json["ruleChosen"]

    ruleDetails = Tajweed.Select_dict_path(rule)
    surahData = {}

    for n in range(1, 115):
        occ = sum(item['surah'] == n for item in ruleDetails[0])
        print(occ)
        surahData[n] = occ
    
    Tajweed.Analysis_path({f"{rule}": surahData})
    
    return (jsonify(rule=rule, surahData=surahData))

@app.route("/view-graphs", methods=["GET", "POST"])
def viewGraphs():
    rule = request.form.get('selectedRule')
    print(rule)
    sortedRule={}
   
    if rule != None:
        with open("Tajweed Apis/analysis.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            sortedRule = jsonObject[rule]
    # plt.bar(*zip(*ruleData.items()))

            fig = plt.figure()

            plt.bar(range(len(sortedRule)), list(sortedRule.values()), align='center')
            plt.xticks(range(len(sortedRule)), list(sortedRule.keys()))
            plt.locator_params(axis='x', nbins=20)

            fig.suptitle(f"{rule}", fontsize=20)
            plt.xlabel('Surah #', fontsize=14)
            plt.ylabel('# of rules', fontsize=14)


            plt.show()
    return render_template("output.html", rule=rule, sortedRule=sortedRule)