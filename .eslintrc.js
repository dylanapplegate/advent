module.exports = {
  extends: [
    'airbnb-typescript/base',
    'plugin:import/typescript',
    'plugin:prettier/recommended',
  ],
  plugins: ['@typescript-eslint', 'import'],
  parserOptions: {
    project: './tsconfig.json',
  },
  rules: {
    'prettier/prettier': [
      'error',
      {
        endOfLine: 'auto',
      },
    ],
    'import/extensions': 'off',
    'import/no-extraneous-dependencies': ['error', { devDependencies: true }],
  },
  ignorePatterns: ['.eslintrc.js', 'GEMINI.md'],
  // This is the core fix:
  overrides: [
    {
      // Target only the ESLint config files themselves
      files: [
        '.eslintrc.js',
        '**/*.config.js', // Include other config files like vite.config.js, etc.
        '**/*.config.cjs',
        '**/*.config.mjs',
      ],
      // Use a configuration that *doesn't* require a tsconfig.json file
      parserOptions: {
        project: null, // Explicitly disable typed linting for these files
        // Or remove it entirely if you don't need typed linting on them at all
      },
    },
    {
      // The rest of your project files (e.g., .ts, .tsx)
      files: ['**/*.ts', '**/*.tsx'],
      parserOptions: {
        // This is where you keep the project setting for type-aware rules
        project: './tsconfig.json',
      },
      // ... (Rest of your TypeScript rules)
    },
  ],

};
