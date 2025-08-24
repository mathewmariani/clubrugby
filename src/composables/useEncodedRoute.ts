import { useRoute } from "vue-router";
import { computed } from "vue";

export function useEncodedRoute() {
  function encode(obj: any): string {
    const jsonString = JSON.stringify(obj);
    return btoa(unescape(encodeURIComponent(jsonString)));
  }

  function decode(str: string): any {
    try {
      const jsonString = decodeURIComponent(escape(atob(str)));
      return JSON.parse(jsonString);
    } catch (e) {
      console.error("Failed to decode Base64:", e);
      return null;
    }
  }

  const route = useRoute();
  function getDecodedQueryParam(paramName: string) {
    return computed(() => {
      const encoded = route.query[paramName] as string | undefined;
      if (!encoded) return null;
      return decode(encoded);
    });
  }

  return { encode, decode, getDecodedQueryParam };
}
