<template>
  <svg :height="height" alt="Sobeser" fill="none" viewBox="0 0 600 100" xmlns="http://www.w3.org/2000/svg">
    <metadata id="metadata8">image/svg+xml</metadata>
    <g>
      <title>Layer 1</title>
      <text stroke-dasharray="5,2,2,2" transform="matrix(2.49546 0 0 2.49546 -281.63 -28.2128)" stroke="#000"
            xml:space="preserve" text-anchor="start" font-family="'Azeret Mono'" font-size="44" id="svg_2" y="45"
            x="150" stroke-width="0" fill="#154EC1">SOBESER</text>
    </g>
    <defs>
      <linearGradient id="paint0_linear" gradientUnits="userSpaceOnUse" x1="0" x2="357.64" y1="56.1386" y2="56.1386">
        <stop :stop-color="colorsComputed.end"/>
        <stop :stop-color="colorsComputed.start" offset="1"/>
      </linearGradient>
    </defs>
  </svg>
</template>

<script lang="ts" setup>
import {computed} from 'vue'
import {useColors} from 'vuestic-ui'

const {getColor} = useColors()

const props = withDefaults(
  defineProps<{
    height?: number
    start?: string
    end?: string
  }>(),
  {
    height: 18,
    start: 'primary',
    end: undefined,
  },
)

const colorsComputed = computed(() => {
  return {
    start: getColor(props.start),
    end: getColor(props.end || props.start),
  }
})
</script>
