def generate_concept_HTML(concept_title, concept_description):
    html_text_1= '''
<div class= "concept">
  <div class= "concept-title">
    ''' + concept_title
    html_text_2= '''
  </div>
  <div class= "concept-description">
    ''' + concept_description
    html_text_3= '''
  </div>
</div> '''
    full_html_text= html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title= concept[0]
    concept_description= concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML= ""
    for concept in list_of_concepts:
        concept_HTML= make_HTML(concept)
        HTML= HTML + concept_HTML
    return HTML

Lesson_Concepts = [['Lists', 'Lists can be a sequence of anything even other lists'],
                   ['Nested Lists', 'Lists can have numbers, strings, or other lists inside them and elements can be accessed like strings, with the position number in brackets'],
                   ['Mutation', 'Elements in a list can be changed to a new value with an assignment statement which also changes the value of the list'],
                   ['Mutation Issue', 'If you introduce a new variable and it is assigned the same value as another variable when the value of one is changed the other is as well']]
                          
print make_HTML_for_many_concepts(Lesson_Concepts)                   
