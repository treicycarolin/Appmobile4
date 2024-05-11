class Prototype:
  def __init__(self, name, num_pages, flow):
      self.name = name
      self.num_pages = num_pages
      self.flow = flow

  def display_info(self):
      print(f"Prototype: {self.name}")
      print(f"Number of pages: {self.num_pages}")
      print("Flow:")
      for i, page in enumerate(self.flow, start=1):
          print(f"Page {i}: {page}")

# Create prototype instance
prototype = Prototype("Shopping List App", 8, [
  "Welcome Page",
  "Login Page",
  "Me logged In",
  "Home",
  "Create New List Page",
  "List Items Page",
  "Add Items Page",
  "Download Items",
  "Share Shopping List"
])

# Display prototype information
prototype.display_info()