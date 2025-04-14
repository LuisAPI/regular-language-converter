from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Define the regular expression pattern based on your specification:
# Breakdown of the pattern:
# 1. (aa+bb)          -> (aa|bb)
# 2. (aba+bab+bbb)     -> (aba|bab|bbb)
# 3. (a+b)*            -> (?:a|b)*
# 4. (aa+bb)          -> (aa|bb)
# 5. (aa+bb)*         -> (?:(aa|bb))*
# 6. (aa+bb)*         -> (?:(aa|bb))*
# 7. (ab* ab* a)      -> ab*ab*a   (i.e. an "a", then zero or more "b", then "a", then zero or more "b", then "a")
# 8. (ab* ab* a)*     -> (?:ab*ab*a)*
# 9. (bbb+aaa)        -> (bbb|aaa)
# 10. (a+b)*          -> (?:a|b)*

pattern = re.compile(
    r'^(aa|bb)'                # Component 1
    r'(aba|bab|bbb)'           # Component 2
    r'(?:a|b)*'                # Component 3
    r'(aa|bb)'                 # Component 4
    r'(?:(aa|bb))*'            # Component 5; note: using non-capturing group is optional here
    r'(?:(aa|bb))*'            # Component 6
    r'(ab*ab*a)'               # Component 7
    r'(?:(ab*ab*a))*'          # Component 8
    r'(bbb|aaa)'               # Component 9
    r'(?:a|b)*$'               # Component 10
)

@app.route('/validate', methods=['POST'])
def validate():
    # Expect a JSON payload with "input_string"
    data = request.get_json()
    input_string = data.get('input_string', '')
    
    # Check if the input string fully matches the regular expression.
    if pattern.fullmatch(input_string):
        result = {
            'accepted': True,
            'message': 'The string is accepted according to the regex.'
        }
        return jsonify(result), 200
    else:
        result = {
            'accepted': False,
            'message': 'The string does not match the regex.'
        }
        return jsonify(result), 400

if __name__ == '__main__':
    app.run(debug=True)