// Serves the static site from public/ and sends every other address to the main one.
// kitchenwhiz.in is the main address. www.kitchenwhiz.in, commercialkitchens.co.in
// and www.commercialkitchens.co.in redirect (301) to the same page on kitchenwhiz.in.
const MAIN_HOST = "kitchenwhiz.in";
const REDIRECT_HOSTS = new Set([
  "www.kitchenwhiz.in",
  "commercialkitchens.co.in",
  "www.commercialkitchens.co.in",
]);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (REDIRECT_HOSTS.has(url.hostname)) {
      url.protocol = "https:";
      url.hostname = MAIN_HOST;
      url.port = "";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
