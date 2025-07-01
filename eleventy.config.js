const { eleventyImageTransformPlugin } = require("@11ty/eleventy-img");

module.exports = async function(eleventyConfig) {
	const { EleventyRenderPlugin } = await import("@11ty/eleventy");
  eleventyConfig.addPlugin(EleventyRenderPlugin);
	eleventyConfig.addPlugin(eleventyImageTransformPlugin);


  eleventyConfig.addPassthroughCopy("bundle.css");
};