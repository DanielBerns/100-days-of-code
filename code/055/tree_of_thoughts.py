MAX_TOKENS = 1024
DEFAULT_TEMPERATURE = 0
DEFAULT_ANTHROPIC_MODEL_NAME = "claude-3-5-sonnet-20240620"


class AnthropicService:
    def __init__(self, model_name: str = None, anthropic: Anthropic = None):
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise ValueError("No valid API key found for Anthropic.")
        self.client = anthropic or Anthropic(
            api_key=os.environ["ANTHROPIC_API_KEY"])
        self.model_name = model_name or DEFAULT_ANTHROPIC_MODEL_NAME

    def generate_response(
        self, prompt: str, 
        max_tokens: int = MAX_TOKENS, 
        temperature: float = DEFAULT_TEMPERATURE
    ) -> str:
        msg = self.client.messages.create(
            model=self.model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return msg.content[0].text

class ThoughtNode:
    def __init__(self, thought, children=None):
        self.thought = thought
        self.children = children or []
    

class TreeOfThought:
    def __init__(self, root_prompt, ai_service=None, max_iterations=3, max_tokens=250):
        self.root = ThoughtNode(root_prompt)
        self.max_iterations = max_iterations
        self.ai_service = ai_service or AnthropicService()
        self.current_thoughts = [self.root]
        self.max_tokens = max_tokens
        
    def call_llm(self, prompt):
        try:
            response = self.ai_service.generate_response(
                prompt,
                max_tokens=self.max_tokens,
            )
            return response
        except Exception as e:
            print(f"Error calling LLM: {e}")
            return []
        
    
    def explore_thoughts(self, thought_nodes):
        new_thought_nodes = []
        for thought_node in thought_nodes:
            prompt = f"Given the current thought: '{thought_node.thought}', provide two concise next thoughts that evolve this idea further."
            response = self.call_llm(prompt)
            if response:
                new_thought_node = ThoughtNode(response)
                thought_node.children.append(new_thought_node)
                new_thought_nodes.append(new_thought_node)
        return new_thought_nodes
    
    def run(self):
        iteration = 0
        while self.current_thoughts and iteration < self.max_iterations:
            print(f"Iteration {iteration + 1}:")
            self.current_thoughts = self.explore_thoughts(
                self.current_thoughts)
            for thought_node in self.current_thoughts:
                print(f"Explored Thought: {thought_node.thought}")
            iteration += 1
            
    def update_starting_thought(self, new_thought):
        self.root = ThoughtNode(new_thought)
        self.current_thoughts = [self.root]

    def print_tree(self, node, level=0):
        indent = ' ' * (level * 2)
        thought_lines = node.thought.split('\n')
        for idx, line in enumerate(thought_lines):
            if idx == 0:
                print(f"{indent}- {line}")
            else:
                print(f"{indent}  {line}")
        for child in node.children:
            self.print_tree(child, level + 1)

            
if __name__ == "__main__":
    starting_prompt = "Think of a solution to reduce the operational costs of your business."
    tot = TreeOfThought(starting_prompt)
    tot.run()
    print("=" * 100)
    print("Final Tree of Thoughts:")
    tot.print_tree(tot.root)
