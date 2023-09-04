import json
from flask import jsonify
# The JSON data you provided
json_data ={"statement": "Law of Segregation\nThis law is based on the fact that the alleles do not show any blending\nand that both the characters are recovered as such in the F2\n generation\nthough one of these is not seen at the F1\n stage. Though the parents contain\ntwo alleles during gamete formation, the factors or alleles of a pair segregate\nfrom each other such that a gamete receives only one of the two factors. Of course, a homozygous parent produces all gametes that are similar\nwhile a heterozygous one produces two kinds of gametes each having\none allele with equal proportion.",
            "questions": [
    {
      "question_statement": "What do not show any blending?",
      "question_type": "MCQ",
      "answer": "alleles",
      "id": 1,
      "options": [
        "Phenotypes",
        "Different Genes",
        "Gene"
      ],
      "options_algorithm": "sense2vec",
      "extra_options": [
        "Recessive",
        "Genetic Variation"
      ],
      "context": "Law of Segregation\nThis law is based on the fact that the alleles do not show any blending\nand that both the characters are recovered as such in the F2\n generation\nthough one of these is not seen at the F1\n stage. Though the parents contain\ntwo alleles during gamete formation, the factors or alleles of a pair segregate\nfrom each other such that a gamete receives only one of the two factors. Though the parents contain\ntwo alleles during gamete formation, the factors or alleles of a pair segregate\nfrom each other such that a gamete receives only one of the two factors."
    },
    {
      "question_statement": "What is the only gamete that receives only one of the two factors?",
      "question_type": "MCQ",
      "answer": "gamete",
      "id": 2,
      "options": [
        "Chromosomes",
        "Sex Cells",
        "Diploid"
      ],
      "options_algorithm": "sense2vec",
      "extra_options": [
        "Genome",
        "Ovum",
        "Meiosis"
      ],
      "context": "Though the parents contain\ntwo alleles during gamete formation, the factors or alleles of a pair segregate\nfrom each other such that a gamete receives only one of the two factors. Though the parents contain\ntwo alleles during gamete formation, the factors or alleles of a pair segregate\nfrom each other such that a gamete receives only one of the two factors."
    },
    {
      "question_statement": "The alleles do not show any what?",
      "question_type": "MCQ",
      "answer": "blending",
      "id": 3,
      "options": [
        "Blend",
        "More Color",
        "Layering"
      ],
      "options_algorithm": "sense2vec",
      "extra_options": [
        "Darken",
        "Shimmer"
      ],
      "context": "Law of Segregation\nThis law is based on the fact that the alleles do not show any blending\nand that both the characters are recovered as such in the F2\n generation\nthough one of these is not seen at the F1\n stage."
    }
  ],
  "time_taken": 5.54791522026062
}

def parsing(outputtext):

    json_data = outputtext

    # Parse the JSON data
    data = json.dumps(json_data)
    data = json.loads(data)

    # Extract and store relevant information in variables
    statement = data["statement"]
    questions = data["questions"]
    out_dict = {}

    # Loop through the questions and extract their information
    for question in questions:
        question_number = question["id"]
        question_statement = question["question_statement"]
        answer = question["answer"]
        options = question["options"]
        extra_options = question["extra_options"]

        if question_number not in out_dict:
            out_dict[question_number] = {}

        out_dict[question_number]["Question:"] = question_statement #string
        out_dict[question_number]["Options:"] = options #list
        out_dict[question_number]["Correct Answer:"] = answer #string
        out_dict[question_number]["Other Options:"] = extra_options #list
    
    return out_dict
    

    """
        # You can print or process these variables as needed
        print(question_number, "Question Statement:", question_statement)
        print("Answer:", answer)
        print("Options:", options)
        print("Extra Options:", extra_options)
        print("\n")"""