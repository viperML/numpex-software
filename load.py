with open("projects.yml", "a") as f:

    for i in range(1, 100):
        entry = f"""
- name: Fake{i}
  description: |
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
      commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
      velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
      cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
      est laborum.
  documentation: https://example.com/
  discussion: https://example.com/discussion
  spack_package: https://example.com/spack
  guix_package: https://example.com/guix
"""

        f.write(entry)
