export {};

declare global {
  interface Window {
    dataLayer: any[];
  }

  var dataLayer: any[];

  function gtag(
    command: string,
    target: string | Date,
    config?: Record<string, any>
  ): void;
}
