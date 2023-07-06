export default function Footer() {
  return (
    <div className="absolute w-full border-t border-gray-200 bg-white py-5 text-center">
      <p className="text-gray-500">
        From the team{" "}
        <a
          className="font-medium text-gray-800 underline transition-colors"
          // TODO What to put here
          href="https://twitter.com/steventey"
          target="_blank"
          rel="noopener noreferrer"
        >
          DGenerationX
        </a>
      </p>
    </div>
  );
}
