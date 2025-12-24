import { render, screen } from '@testing-library/react';
import App from './App';

test('renders habit tracker title', () => {
  render(<App />);
  const titleElement = screen.getByText(/habit garden/i);
  expect(titleElement).toBeInTheDocument();
});
