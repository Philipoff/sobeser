<template>
  <svg :height="height" alt="Sobeser" fill="none" viewBox="0 0 478 57" xmlns="http://www.w3.org/2000/svg">
 <metadata id="metadata8">image/svg+xml</metadata>
    <defs id="defs6">
  <clipPath clipPathUnits="userSpaceOnUse" id="clipPath18">
   <path clip-rule="evenodd" d="m0.00001,0l612,0l0,792l-612,0l0,-792z" id="path16"/>
  </clipPath>
      <clipPath clipPathUnits="userSpaceOnUse" id="clipPath30">
   <path clip-rule="evenodd" d="m0.00001,0l612,0l0,792l-612,0l0,-792z" id="path28"/>
  </clipPath>
 </defs>
    <g>
  <title>Layer 1</title>
      <g id="g10" transform="matrix(1.3333333,0,0,-1.3333333,0,1056)">
   <g id="g12">
    <g id="g14" clip-path="url(#clipPath18)">
     <text fill-rule="nonzero" fill="#000000" font-family="'Courier 10 Pitch'" font-size="10.56px" font-weight="normal"
           transform="matrix(1,0,0,-1,75.024,710.98)" id="text22">
      <tspan x="0 6.336 12.71424 18.9552 25.291201 31.55328 37.889278" y="0" id="tspan20">SOBESER</tspan>
     </text>
    </g>
   </g>
        <g id="g24">
    <g id="g26" clip-path="url(#clipPath30)"/>
   </g>
  </g>
      <text stroke-dasharray="5,2,2,2" transform="matrix(2.49546 0 0 2.49546 -281.63 -28.2128)" stroke="#000"
            xml:space="preserve" text-anchor="start" font-family="'Azeret Mono'" font-size="24" id="svg_2" y="31.54969"
            x="114.57973" stroke-width="0" fill="#000000">SOBESER</text>
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
